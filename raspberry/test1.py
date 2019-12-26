import modi
import time
import speech_recognition as sr

bundle = modi.MODI()
time.sleep(1)

speaker = bundle.speakers[0]

r = sr.Recognizer()
mic = sr.Microphone()

while True:
  with mic as source:
    print('Say')
    audio = r.listen(source)
    message = r.recognize_google(audio, language='ko-KR')
    print('Check: ' + message)
    speaker.tune(1318,0)
    if (message == "문성" or message == "중학교"):
      for i in range(2) :
        speaker.tune(1318,100) #F_MI_6
        time.sleep(0.2)
        speaker.tune(1318,0) #F_MI_6
        time.sleep(0.05)
        speaker.tune(1318,100) #F_MI_6
        time.sleep(0.2)
        speaker.tune(1318,0) #F_MI_6
        time.sleep(0.05)
        speaker.tune(1318,100) #F_MI_6
        time.sleep(0.45)
        speaker.tune(1318,0) #F_MI_6
        time.sleep(0.05)
      speaker.tune(1318,100) #F_MI_6
      time.sleep(0.25)
      speaker.tune(1567,100) #F_SOL_6
      time.sleep(0.25)
      speaker.tune(1046,100) #F_DO_6
      time.sleep(0.25) 
      speaker.tune(1174,100) #F_RE_6
      time.sleep(0.25)
      speaker.tune(1318,100) #F_MI_6
      time.sleep(1)  
    time.sleep(0.001)
    message = ""



