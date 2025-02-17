
import streamlit as st
from openai import OpenAI
import openai
import os
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from fpdf import FPDF

# Imposta la chiave API di OpenAI (assicurati di averla esportata nelle variabili d'ambiente)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
        try:
            # Prima prova: tenta di ottenere la trascrizione in inglese
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        except (NoTranscriptFound, TranscriptsDisabled) as e:
            st.warning("Trascrizione in inglese non trovata, provo con l'italiano...")
            try:
                # Seconda prova: tenta di ottenere la trascrizione in italiano
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
            
            st.info("Trascrizione recuperata correttamente. Inoltrando alle API di OpenAI per l'analisi...")
            
            # Prepara i messaggi per il completamento chat
            system_msg = {
                "role": "system",
                "content": (
                    "Sei un assistente esperto in analisi e formattazione di trascrizioni. "
                    "Riceverai la trascrizione di un video YouTube. Analizza e formatta il testo "
                    "aggiungendo i nomi dei parlanti e separando chiaramente i turni di parola. "
                    "Mantieni l'ordine cronologico e utilizza un formato leggibile."
                )
            }
            user_msg = {
                "role": "user",
                "content": f"Trascrizione originale:\n\n{transcript_text}\n\nPer favore, analizza e formatta la trascrizione secondo le indicazioni."
            }
            
            try:
                # Chiamata alle API di OpenAI
                response = client.chat.completions.create(
                    model="gpt-4o-mini",  # Modifica il modello se necessario
                    messages=[system_msg, user_msg],
                )
                formatted_transcript = response.choices[0].message.content.strip()
            except Exception as e:
                st.error(f"Errore durante l'analisi con OpenAI: {e}")
                formatted_transcript = transcript_text  # Fallback sulla trascrizione originale
            
            st.success("Analisi completata!")

            # **SOLUZIONE 1: Converti il testo in modo che contenga solo caratteri supportati da latin-1**
            formatted_transcript = formatted_transcript.encode("latin1", errors="replace").decode("latin1")
            
            # Genera il PDF con la trascrizione formattata
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, formatted_transcript)
            
            # Ottieni il PDF come bytes
            pdf_bytes = pdf.output(dest="S").encode("latin1")
            
            st.download_button(
                label="Scarica PDF della trascrizione",
                data=pdf_bytes,
                file_name="trascrizione.pdf",
                mime="application/pdf"
            )
