https://huggingface.co/openai/whisper-large-v3

Select the mode that aligns with your skill set and comfort level: Master or Grandmaster. Test assignment is considered completed if at least Master mode is done.

Deadline: 1 week.

Common Requirements for All Modes: · Send conformation about completion to alindor.tech@gmail.com. Conformation should contain: link to GitHub (do not forget to grant access by email above), link to server with Web Interface.

· Include API keys in the repository. All listed below API providers will not impose additional charges for overuse, that we don’t plan to do (hiring manager will test it few times). You may terminate your API keys after the test assignment has been reviewed.

· Add a README file to your repository explaining your work, the challenges you faced, and instructions on how to run your code. This is especially important for modes that don’t require a cloud engine and REST API. For modes with cloud engine and REST API, don’t forget to include link to your server.

· Develop a web interface for user input and output using frameworks like Flask or Django. The interface should allow the Hiring Manager to attach an audio file (Master, Grandmaster modes) containing a dialogue with at least 2 speakers.

· Example of audio file:

[Speaker_1]: Hello, Dave. How are you?

[Speaker_2]: Hi, Joseph. I’m good. Yesterday went for a run. What about you?

[Speaker_1]: I’m fine. Today I will read a book. I like reading.

· For your work to find any audio for testing, you can use any recording with at least two speakers, for example a podcast or interview.

So, in input of Web interface Hiring manager attaches audio with any human conversation. In output Hiring manager should get sentiment or psychological insights derived from the conversation, some insights about speakers. Please don’t provide summary of conversation, key words, etc. Output should be related to sentimental analysis. For example:

Line 1 in web interface: ‘[Speaker_2] likes a sport. It seems he cares about his health’.

Line 2 in web interface: ‘[Speaker_1] pretends to be smart’.

There are no strict requirements regarding the output format. Substance takes precedence – we're looking for interesting responses from OpenAI. However, if you're struggling with creativity, feel free to reference our MVP app for inspiration app demo and description of app and company's culture

Specific Requirements for Each Mode:

Master Mode:

0. Input is audio file.

1. Deepgram API for Speech to Text (free 200$ credits without credit card).

2. Utilize the OpenAI API for sentimental analysis (to get free credits it requires a $5 one-time top-up, but we, Alindor Corp., are committed to refund it upon invoice submission after at least formal execution of Master Mode)

3. Leverage a cloud engine (for example Google Cloud Platform offers sufficient number of free credits for VC engine) and develop a REST API for scalable processing.

Grandmaster Mode:

1. Everything, which is in Master, but instead of Deepgram API use open source diarization/transcription models such as WhisperX, etc.

2. Show more creativity on sentimental analysis. Test different prompts, methods, how to get creative and relevant insights from GPT model, which will be very valuable for users.