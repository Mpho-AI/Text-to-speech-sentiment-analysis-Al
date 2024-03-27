const recordButton = document.getElementById('recordButton');
const stopButton = document.getElementById('stopButton');
const uploadButton = document.getElementById('uploadButton');
const audioPlayer = document.getElementById('audioPlayer');

let recorder;
let audioChunks = [];

recordButton.addEventListener('click', startRecording);
stopButton.addEventListener('click', stopRecording);
uploadButton.addEventListener('click', uploadRecording);

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            recorder = new MediaRecorder(stream);
            recorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };
            recorder.onstop = () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                const audioUrl = URL.createObjectURL(audioBlob);
                audioPlayer.src = audioUrl;
                uploadButton.disabled = false;
            };
            recorder.start();
            recordButton.disabled = true;
            stopButton.disabled = false;
        })
        .catch(error => {
            console.error('Error accessing microphone:', error);
        });
}

function stopRecording() {
    if (recorder.state === 'recording') {
        recorder.stop();
        recordButton.disabled = false;
        stopButton.disabled = true;
    }
}

function uploadRecording() {
    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
    const formData = new FormData();
    formData.append('file', audioBlob);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(transcript => {
        console.log('Transcription:', transcript);
        // Handle transcription response as needed
    })
    .catch(error => {
        console.error('Error uploading recording:', error);
    });
}
