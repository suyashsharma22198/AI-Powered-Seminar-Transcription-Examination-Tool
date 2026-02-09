import whisper
import sys

def transcribe_video(video_path, output_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)

    # Write the transcription result to a text file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    # print("Transcription written to", output_path)
    return result["text"]
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python transcript_vid.py <video_path> <output_path>")
        sys.exit(1)

    video_path = sys.argv[1]
    output_path = sys.argv[2]
    transcribe_video(video_path, output_path)
