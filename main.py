import os
import json
import whisper
from pathlib import Path

# Function to recursively find audio files in the provided directory
def find_files(directory):
    media_ext = {'.mp3', '.wav','.mp4'}
    media_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if Path(file).suffix.lower() in media_ext:
                media_files.append(os.path.join(root, file))
    return media_files

# Function to transcribe a media file using the model
def transcribe_media(file_path, model):
    try:
        print(f"Transcribing: {file_path}")
        result = model.transcribe(file_path)
        print(result['text'])
        return result['text']
    except Exception as e:
        print(f"Error transcribing {file_path}: {e}")
        return None

# Function to save transcription in a JSON or text file
def save_transcription(output_dir, file_path, transcription, output_format='txt'):
    if transcription is None:
        return

    file_name = Path(file_path).stem
    if output_format == 'json':
        output_file = os.path.join(output_dir, f"{file_name}.json")
        with open(output_file, 'w') as json_file:
            json.dump({"file": file_path, "transcription": transcription , }, json_file, indent=4)
    else:  
        output_file = os.path.join(output_dir, f"{file_name}.txt")
        with open(output_file, 'w') as text_file:
            text_file.write(transcription)
    print(f"Saved transcription for {file_path} to {output_file}")

# Main function to process the directory
def main(input_directory, output_directory, output_format='txt'):
    # Load Whisper model
    model = whisper.load_model("tiny")

    media_files = find_files(input_directory)
    os.makedirs(output_directory, exist_ok=True)


    for media_file in media_files:
        transcription = transcribe_media(media_file, model)
        save_transcription(output_directory, media_file, transcription, output_format)


if __name__ == "__main__":
    input_directory = 'Input/'  
    output_directory = 'Output/'  
    output_format = 'text'  

    main(input_directory, output_directory, output_format)
