import speech_recognition as sr

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = recognizer.listen(source)
    return audio