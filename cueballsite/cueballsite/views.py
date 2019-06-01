import pyrebase

config = {
    'apiKey': "AIzaSyDnRM1b-dOfkqmaQ94BJyG-0lCo114LPmA",
    'authDomain': "reminders-56e2c.firebaseapp.com",
    'databaseURL': "https://reminders-56e2c.firebaseio.com",
    'projectId': "reminders-56e2c",
    'storageBucket': "reminders-56e2c.appspot.com",
    'messagingSenderId': "708737581745",
    'appId': "1:708737581745:web:2f01846c6569d039"
  };
 
firebase = pyrebase.initialize_app(config);
auth = firebase.auth()
