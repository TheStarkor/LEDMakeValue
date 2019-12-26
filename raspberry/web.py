import firebase_admin
import time
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

while True:
    doc_ref = db.collection(u'Test').document(u'Pi')

    doc = doc_ref.get()
    flag = doc.to_dict()['Find']

    if flag == 1:
        print ('찾는중')
        doc_ref.set({u'Find': 0})   
        print ('완료')
    else:
        print ('대기중')

    time.sleep(3)
# city = City.from_dict(doc.to_dict())
# print(city)