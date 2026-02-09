# AI-Powered Transcription Application

## Overview
This project is an AI-powered transcription tool that converts audio or video files into accurate, readable text. It is designed for professionals, students, and examiners who need fast, reliable transcripts for seminars, interviews, lectures, podcasts, and more. The application also supports advanced features such as generating seminar-based multiple-choice questions (MCQs) with answers and automatic seminar summary generation, making it a valuable tool for education, examination, and content review.

## Key Features
- **AI-Powered Transcription:** Converts speech in audio/video files to text using state-of-the-art AI models.
- **Seminar Summary Generation:** Automatically produces concise summaries of seminar content for quick review.
- **Seminar-Based MCQ Generation with Answers:** Creates multiple-choice questions (with correct answers) from seminar transcripts to aid in learning, assessment, and examination preparation.
- **User-Friendly Interface:** Simple web interface for uploading files and downloading results.
- **No Setup Required:** Runs locally with a single command; minimal dependencies.

## Use Cases
- **Education:** Students and teachers can transcribe lectures and seminars, generate summaries for revision, and create MCQs (with answers) for self-assessment, quizzes, or exams.
- **Examination:** Examiners and educators can automatically generate MCQs with answers from seminar content to create tests and assessments efficiently.
- **HR & Training:** HR professionals can generate MCQs (with answers) from seminars or any video content to quiz participants and assess their awareness or understanding of the material presented.
- **Research:** Researchers can quickly transcribe interviews or focus groups and extract key points or quiz questions.
- **Content Creation:** Podcasters, journalists, and media professionals can obtain transcripts for editing, publishing, or SEO.
- **Accessibility:** Makes spoken content accessible to those with hearing impairments or language barriers.

## Setup Guide

### Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning the repository)

### Environment Variables
If your application requires API keys or other secrets, copy `.env.example` to `.env` and fill in your values. The `.env` file is ignored by git for security.

### Installation Steps
1. **Clone the repository** (or download the source code):
   ```bash
   git clone <your-repo-url>
   cd BCGx_transcription
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```
3. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```
4. **Access the app:**
   - Open the provided local URL in your browser (usually http://localhost:8501)

## How It Works
1. **Upload:** Select and upload your audio or video file.
2. **Transcription:** The AI model processes the file and generates a transcript.
3. **Summary & MCQ:** Optionally, generate a summary or MCQs (with answers) from the transcript for seminar review, assessment, or examination.
4. **Download:** Save the transcript, summary, or MCQs for your records.

## Project Structure
```
BCGx_transcription/
├── streamlit_app.py           # Main Streamlit web app
├── transcript_vid.py          # Transcription logic
├── requirement.txt            # Python dependencies
├── transcription/
│   └── transcription_result.txt  # Output transcript
├── data/                      # (Optional) Data storage
└── ARCHITECTURE.md            # Architecture and design doc
```

## Contributing
Pull requests and suggestions are welcome! Please open an issue to discuss your ideas or report bugs.

## License
This project is for educational and demonstration purposes.

---

**Empower your learning, research, and content creation with AI-driven transcription and seminar analysis!**
