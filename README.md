# Transcription project Using Whisper

This project leverages OpenAI's Whisper model to automatically transcribe audio into text. Whisper is a state of the art speech to text model capable of transcribing multiple languages with high accuracy. The script features a recursive search method that scans a specified folder and its subfolders for audio files. Once the search is complete, the results are saved to a chosen directory. Additionally, you can select the output format, either as a text file or a JSON file, to suit your preferences

## Requirements

Before you begin, ensure that you have the following:

- `Python 3.12` or higher
- `whisper` library
- `chocolatey` for choco
- `ffmpeg` for audio processing

### Install Dependencies

You can install the required Python libraries with the following commands:

```bash
pip install -U openai-whisper
pip install git+https://github.com/openai/whisper.git 
choco install ffmpeg
