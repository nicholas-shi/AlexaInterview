import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def convertFile(fileName):
    credentials = "AIzaSyCX_sgS4Y5tyZJ29dfPwmJmO-uvalIpZHA"
    # Instantiates a client
    client = speech.SpeechClient(credentials=credentials)

    # The name of the audio file to transcribe
    # file_name = os.path.join(
    #     os.path.dirname(fileName))
    file_name = "C:\\Users\\Nicholas\\Desktop\\Scraper\\Recording.m4a"

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))

convertFile('Recording.m4a')