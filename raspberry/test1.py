import modi
import time

bundle = modi.MODI()
time.sleep(1)

mic = bundle.mics[0]
speaker = bundle.speakers[0]

while True:
    speaker.tune(1318,0)
    vol = mic.volume()
    print(vol)
    if vol >= 30 :
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
