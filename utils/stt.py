import speech_recognition as sr

def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Error connecting to the Speech Recognition service."
    