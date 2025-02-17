import streamlit as st
import os
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from fpdf import FPDF

# Import LangChain
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Imposta la chiave API di OpenAI (assicurati di averla esportata nelle variabili d'ambiente)
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=openai_api_key, model_name="gpt-4")  # Modifica il modello se necessario

st.title("Analizzatore di Trascrizioni YouTube")

# Input per l'URL del video YouTube
video_url = st.text_input("Inserisci l'URL di YouTube:")

def estrai_video_id(url):
    """
    Estrae l'ID del video da una URL di YouTube.
    Supporta formati come:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

if st.button("Elabora Video"):
    video_id = estrai_video_id(video_url)
    if not video_id:
        st.error("URL non valido. Assicurati di inserire un link di YouTube corretto.")
    else:
        # Prova a recuperare la trascrizione in inglese
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        except (NoTranscriptFound, TranscriptsDisabled):
            st.warning("Trascrizione in inglese non trovata, provo con l'italiano...")
            try:
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['it'])
            except Exception as e:
                st.error(f"Errore durante il recupero della trascrizione in italiano: {e}")
                transcript_list = None
        except Exception as e:
            st.error(f"Errore durante il recupero della trascrizione: {e}")
            transcript_list = None

        if transcript_list:
            # Unisci le parti della trascrizione in un unico testo
            transcript_text = " ".join([entry['text'] for entry in transcript_list])
            st.info("Trascrizione recuperata correttamente. Procedo con il chunking...")

            # Suddividi il testo in chunk
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            chunks = text_splitter.split_text(transcript_text)
            st.write(f"Numero di chunk generati: {len(chunks)}")

            # Definisci il template per formattare ogni chunk
            prompt_template = PromptTemplate(
                input_variables=["chunk"],
                template=(
                    "Sei un assistente esperto in analisi e formattazione di trascrizioni. "
                    "Riceverai un frammento di una trascrizione di un video YouTube. "
                    "Analizza e formatta il testo aggiungendo i nomi dei parlanti, separando chiaramente i turni di parola, "
                    "mantenendo l'ordine cronologico e utilizzando un formato leggibile. \n\n"
                    "Frammento:\n{chunk}\n\n"
                    "Trascrizione formattata:"
                )
            )

            chain = LLMChain(llm=llm, prompt=prompt_template)

            formatted_chunks = []
            for i, chunk in enumerate(chunks):
                st.write(f"Analizzo chunk {i+1} di {len(chunks)}...")
                try:
                    formatted_chunk = chain.run(chunk=chunk)
                except Exception as e:
                    st.error(f"Errore nell'analisi del chunk {i+1}: {e}")
                    formatted_chunk = chunk  # Fallback sulla porzione originale
                formatted_chunks.append(formatted_chunk)

            # Unisci i chunk formattati
            combined_transcript = "\n\n".join(formatted_chunks)
            
            # Fase finale: unisci i chunk in un testo coerente
            st.info("Riunisco i chunk in un'unica trascrizione formattata...")
            final_prompt_template = PromptTemplate(
                input_variables=["transcript"],
                template=(
                    "Sei un assistente esperto in analisi e formattazione di trascrizioni. "
                    "Di seguito trovi una trascrizione parzialmente formattata, composta da più sezioni. "
                    "Uniscile in un unico testo coerente, correggi eventuali discontinuità, "
                    "aggiungi i nomi dei parlanti ove necessario e assicurati che il testo sia ben formattato e leggibile.\n\n"
                    "Trascrizione parziale:\n{transcript}\n\n"
                    "Trascrizione finale formattata:"
                )
            )
            final_chain = LLMChain(llm=llm, prompt=final_prompt_template)
            try:
                final_transcript = final_chain.run(transcript=combined_transcript)
            except Exception as e:
                st.error(f"Errore nella finalizzazione della trascrizione: {e}")
                final_transcript = combined_transcript  # Fallback

            # Gestione encoding: converto il testo in modo che contenga solo caratteri supportati da latin-1
            final_transcript_encoded = final_transcript.encode("latin1", errors="replace").decode("latin1")
            
            # Genera il PDF con la trascrizione formattata
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, final_transcript_encoded)
            pdf_bytes = pdf.output(dest="S").encode("latin1")
            
            st.success("Analisi completata!")
            st.download_button(
                label="Scarica PDF della trascrizione",
                data=pdf_bytes,
                file_name="trascrizione.pdf",
                mime="application/pdf"
            )
