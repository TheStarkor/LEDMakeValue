import firebase_admin
import time
import pygame
from firebase_admin import credentials
from firebase_admin import firestore

pygame.mixer.init()
alarm = pygame.mixer.Sound("alarm.wav")
cred = credentials.Certificate("./ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

while True:
    doc_ref = db.collection(u'Test').document(u'Pi')

    doc = doc_ref.get()
    flag = doc.to_dict()['Find']

    if flag == 1:
        print ('Finding!')
        alarm.play()
        doc_ref.set({u'Find': 0})
        print ('Done!')
    else:
        print ('Waiting..')

    time.sleep(3)