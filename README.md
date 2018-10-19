# weplay
We are playing music together... but what?

# Run backend
```
    cd backend
    python server.py
```

## Secret?

You'll a secret.py with the following:

```
#SPOTIFY
S_CLIENT_ID = <your spotify client id>
S_CLIENT_SECRET = <your spotify client secret>
S_REDIRECT_URL = 'http://localhost:8888/' # Or whatever redirect you wish for

#FIREBASE ADMIN
FB_API_KEY = <your firebase api key>
FB_AUTH_DOMAIN = <the domain of your firebase thingamajing>
FB_DATABASE_URL = <the domain of you firebase dbs>
FB_PROJECT_ID = <your firebase project id>
FB_STORAGE_BUCKET = <your firebase storage bucket id>
FB_MESSAGING_SENDER_ID = <your firebase messaging sender id>

#FIREBASE CREDENTIALS JSON LOCATION
FB_CREDENTIALS = <where you put your credentials json file>
```
Needless to say, you also need the firebase credentials json provided by firebase

## Still not working?

You also need spotipy installed, as well as firebase admin sdk

# Run frontend
```
    npm install
    npm run dev
```

currently using lite-server. That might change in the future

# TODO

## Backend
* Removing spotipy dependency 
* Go from python2 -> python3

## Frontend
* Creating an... you know, _actual_ frontend

