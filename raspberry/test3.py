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
    print(doc.to_dict())
    time.sleep(1)
# city = City.from_dict(doc.to_dict())
# print(city)