# BCG BI&A Take-Home Assessment

## Problem Statement

### What problem does this application address?

Manual transcription of audio and video content is time-consuming, error-prone, and costly. Many professionals, such as journalists, researchers, and content creators, need accurate transcripts for interviews, meetings, lectures, or media production. This application automates the transcription process, making it faster, more accessible, and cost-effective.

### Who is this for?

- Journalists and media professionals
- Researchers and students
- Content creators and podcasters
- Anyone needing quick, accurate transcripts from audio/video files

## Key Design Decisions

- **Streamlit for UI**: Chosen for its simplicity and ability to quickly build shareable web apps with minimal setup.
- **AI-Powered Transcription**: Utilizes a speech-to-text AI model to convert audio/video to text, making AI central to the solution.
- **File Upload & Result Download**: Users can upload their own files and download the resulting transcript, supporting a wide range of use cases.
- **Minimal Dependencies**: Designed to run locally with a single command, requiring only Python and a few packages (see `requirement.txt`).

## Architecture Overview

- **Frontend**: Streamlit app for file upload, progress display, and transcript download.
- **Backend**: Python script leveraging an AI speech-to-text model (e.g., OpenAI Whisper, Google Speech-to-Text, or similar) for transcription.

## What I'd Improve with More Time

- **Cloud Deployment**: Host the app online for true zero-setup access.
- **Support for More Languages**: Expand transcription to multiple languages and dialects.
- **Speaker Diarization**: Identify and label different speakers in the transcript.
- **Enhanced Error Handling**: More robust handling of file types, size limits, and edge cases.
- **User Authentication**: Allow users to save and manage their transcripts securely.

---

This document summarizes the problem, design choices, and future improvements for the BCG BI&A Take-Home Assessment AI-powered transcription application.
