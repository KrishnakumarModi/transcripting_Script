# Transcription project Using Whisper

This project leverages OpenAI's Whisper model to automatically transcribe audio into text. Whisper is a state of the art speech to text model capable of transcribing multiple languages with high accuracy.

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
