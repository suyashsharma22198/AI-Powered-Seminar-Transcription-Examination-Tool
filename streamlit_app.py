import streamlit as st

import os
from transcript_vid import transcribe_video
from google import genai
from dotenv import load_dotenv



# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your environment or .env file.")
client = genai.Client()

st.title("AI-Powered Seminar Transcription & Examination Tool")

# Tabs for different functionalities
tabs = st.tabs(["Transcription", "Summary", "MCQ Generation"])

# Transcription Tab
with tabs[0]:
    st.header("Transcription")

    # File uploader
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"], key="transcription")

    if uploaded_file is not None and 'transcription_text' not in st.session_state:
        temp_video_path = "./data/temp_video.mp4"
        with open(temp_video_path, "wb") as f:
            f.write(uploaded_file.read())
        st.text("Transcribing the video... This may take a while.")
        try:
            output_file_path = "./transcription/transcription_result.txt"
            result = transcribe_video(temp_video_path, output_file_path)
            transcription = result
            st.session_state['transcription_text'] = transcription
            st.subheader("Transcription:")
            st.text_area("Transcription Text", transcription, height=300, key="transcription_text")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
        finally:
            if os.path.exists(temp_video_path):
                os.remove(temp_video_path)
    elif 'transcription_text' in st.session_state:
        st.subheader("Transcription:")
        st.text_area("Transcription Text", st.session_state['transcription_text'], height=300, key="transcription_text")

# Summary Tab
with tabs[1]:
    st.header("Summary Generation")

    if 'transcription_text' not in st.session_state:
        st.warning("Please complete the transcription first.")
        st.stop()
    transcription = st.session_state['transcription_text']
    if st.button("Generate Summary"):
        st.text("Generating summary... Please wait.")
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Summarize the following text:\n{transcription}"
            )
            summary = getattr(response, 'text', None) or getattr(response, 'result', None) or "No summary generated."
            st.subheader("Summary:")
            st.markdown(summary)
        except Exception as e:
            st.error(f"An error occurred while generating the summary: {str(e)}")

# MCQ Generation Tab
with tabs[2]:
    st.header("MCQ Generation")

    if 'transcription_text' not in st.session_state:
        st.warning("Please complete the transcription first.")
        st.stop()
    transcription = st.session_state['transcription_text']
    if st.button("Generate MCQs"):
        st.text("Generating MCQs... Please wait.")
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Generate multiple-choice questions based on the following text:\n{transcription}"
            )
            mcqs = getattr(response, 'text', None) or getattr(response, 'result', None) or "No MCQs generated."
            st.subheader("Generated MCQs:")
            st.markdown(mcqs)
        except Exception as e:
            st.error(f"An error occurred while generating MCQs: {str(e)}")
