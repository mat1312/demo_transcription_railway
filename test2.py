import re
import streamlit as st
import requests
from fpdf import FPDF
from openai import OpenAI
import os
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Imposta la chiave API di OpenAI dalla variabile d'ambiente


def extract_video_id(url):
    """
    Estrae l'ID del video dall'URL di YouTube.
    Supporta vari formati (es. "watch?v=" e "youtu.be").
    """
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    return None

def get_transcript(video_id):
    """
    Chiama l'API per ottenere la trascrizione del video.
    """
    url_api = "https://youtube-transcript3.p.rapidapi.com/api/transcript"
    querystring = {"videoId": video_id}
    headers = {
        "x-rapidapi-key": "1ac68e958emsh472c7a5ef3b8eb1p19e189jsn5e6523bb2aa8",
        "x-rapidapi-host": "youtube-transcript3.p.rapidapi.com"
    }
    response = requests.get(url_api, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Errore durante la richiesta all'API. Controlla l'ID del video o i parametri della richiesta.")
        return None

def transcript_to_text(transcript_json):
    """
    Converte il JSON della trascrizione in una stringa unica.
    Accede alla chiave "transcript" del JSON.
    """
    text = ""
    transcript_entries = transcript_json.get("transcript", [])
    for entry in transcript_entries:
        text += entry.get("text", "") + "\n"
    return text

def analyze_transcript(transcript_text):
    """
    Invia la trascrizione a ChatGPT per l'analisi e la formattazione.
    """
    prompt = f"""formattami questo trascrizione, formattata e strutturata bene, con evidenziati chi sta parlando in questo momento. NON TRALASCIARE NULLA, NON RIASSUMERE NULLA, RIPORTAMI TUTTE LE PAROLE DETTE. Correggi solo la punteggiatura e alcune parole senza senso; se devi farlo, apporta cambiamenti MINIMALI, e cerca di capire sempre chi sta parlando in quel momento.

Transcript:
{transcript_text}"""
    try:
        completion = client.chat.completions.create(
            model="o1-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        st.error(f"Errore durante l'analisi della trascrizione: {e}")
        # In caso di errore, restituisco la trascrizione originale
        return transcript_text

def create_pdf(transcript_text):
    pdf = FPDF()
    pdf.add_page()
    # Utilizza un font Unicode (assicurati di avere "DejaVuSans.ttf" nella stessa cartella)
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)
    pdf.multi_cell(0, 10, transcript_text)
    try:
        pdf_str = pdf.output(dest="S")
        pdf_bytes = pdf_str.encode("latin1")
    except UnicodeEncodeError:
        pdf_str = pdf.output(dest="S")
        pdf_bytes = pdf_str.encode("latin1", errors="replace")
    return pdf_bytes

# Interfaccia Streamlit
st.title("Trascrizione Video YouTube in PDF")

video_url = st.text_input("Inserisci l'URL del video YouTube:")

if st.button("Estrai trascrizione, analizza e genera PDF"):
    video_id = extract_video_id(video_url)
    if not video_id:
        st.error("Impossibile estrarre l'ID del video. Controlla l'URL inserito.")
    else:
        transcript_json = get_transcript(video_id)
        if transcript_json:
            transcript_text = transcript_to_text(transcript_json)
            with st.spinner("Analizzando trascrizione tramite ChatGPT..."):
                analyzed_transcript = analyze_transcript(transcript_text)
            pdf_bytes = create_pdf(analyzed_transcript)
            st.success("Trascrizione analizzata e PDF generato con successo!")
            st.download_button(
                label="Scarica PDF",
                data=pdf_bytes,
                file_name="trascrizione.pdf",
                mime="application/pdf"
            )
