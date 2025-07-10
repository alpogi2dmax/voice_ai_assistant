import struct
import pvporcupine
import pyaudio

from utils.audio import record_audio
from utils.stt import transcribe_audio
from utils.llm import ask_gpt
from utils.tts import speak_text

def main():
    print('Initializing wake word engine...')
    porcupine = pvporcupine.create(
        access_key = 'YOUR_ACCESS_KEY_HERE',
        keywords=['computer']
    )
    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print('Listening for wake word ("computer")... Pres Ctrl+C to quit.')

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from ('h' * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)

            if result >= 0:
                print('Wake word detected! Listening for your input...')

                audio = record_audio()
                text = transcribe_audio(audio)
                print(f'You said: {text}')

                if text.lower() in ['exit', 'quit', 'stop']:
                    print('Goodbye!')
                    break

                response = ask_gpt(text)
                print(f'GPT says: {response}')
                speak_text(response)

                print('\nWaiting for wake word again...')
            
    except KeyboardInterrupt:
        print('Exiting...')
    finally: 
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()

if __name__ == '__main__':
    main()


# from utils.audio import record_audio
# from utils.stt import transcribe_audio
# from utils.llm import ask_gpt
# from utils.tts import speak_text

# def main():
#     print('Press Ctrl+C to quit.')
#     while True:
#         try:
#             audio = record_audio()
#             text = transcribe_audio(audio)
#             print(f'You said: {text}')
        
#             if text.lower() in['exit', 'quit', 'stop']:
#                 print('Goodbye!')
#                 break

#             response = ask_gpt(text)
#             print(f'GPT says: {response}')
#             speak_text(response)

#         except KeyboardInterrupt:
#             print('Exiting...')
#             break

# if __name__ == '__main__':
#     main()