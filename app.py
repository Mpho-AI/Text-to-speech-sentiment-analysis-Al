from flask import Flask, request, render_template
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch





app = Flask(__name__)
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

# Initialize Whisper large-v3 model
model_id = "openai/whisper-large-v3"
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id)
model.to(device)
processor = AutoProcessor.from_pretrained(model_id)
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    device=device,
)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Handle file upload and transcription
    # Assume the transcribed text is stored in 'transcribed_text'

    # Perform sentiment analysis on transcribed text
    transcribed_text = request.form['transcribed_text']
    sentiment_insights = classifier(transcribed_text)
    
    # Render the template with transcribed text and sentiment insights
    return render_template('transcription.html', transcribed_text=transcribed_text, sentiment_insights=sentiment_insights)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('error.html', message='No file part')
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('error.html', message='No selected file')
    
    # Save the uploaded audio file
    audio_path = 'uploaded_audio.wav'  # Change this path as needed
    file.save(audio_path)
    
    # Perform speech-to-text transcription
    try:
        result = pipe(audio_path)
        transcript = result["text"]
        return render_template('transcript.html', transcript=transcript)
    except Exception as e:
        return render_template('error.html', message=f'Transcription failed: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
