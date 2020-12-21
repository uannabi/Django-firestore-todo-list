# Django with firebase database firestore

## installation process 
By default this project can run by sqlit3 

### To enable firestore please follow bellow instruction :
- Rename .env-sample to .env
- Add path of to .env FIREBASE_ORM_CERTIFICATE 'serviceAccountKey.json' 
- Add FIREBASE_ORM_BUCKET_NAME = '<BUCKET_NAME>.appspot.com' to .env 
- Run pip3 install -r requriment.txt
- python3 manage.py runserver 
