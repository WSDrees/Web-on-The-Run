__author__ = 'Chris Lynch'

import sys
from firebase import firebase

#Change the name of the Firebase connection here
_firebase_name = 'mariocarts'

firebase = firebase.FirebaseApplication('https://' + _firebase_name + '.firebaseio.com/', None)

if __name__ == '__main__':
    def __init__():
        print('Firebase Test Complete.')