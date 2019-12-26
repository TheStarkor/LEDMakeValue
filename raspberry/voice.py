import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

while True:
  with mic as source:
    print('Say')
    audio = r.listen(source)
    message = r.recognize_google(audio, language='ko-KR')
    print('Check: ' + message)
