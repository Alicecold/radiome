from __future__ import print_function
from builtins import range
import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
import sys
import secret as app

# Hakk to avoid AttributeError
import os
import json

token = ''
user = ''

def login(this):
    print(this.user)
    if len(sys.argv) > 1:
        this.user = sys.argv[1]
    else:
        this.user = 'alicecold'
    print(this.user)
    scope = 'user-read-currently-playing'
    this.token = util.prompt_for_user_token(this.user, scope,client_id=app.S_CLIENT_ID,client_secret=app.S_CLIENT_SECRET,redirect_uri=app.S_REDIRECT_URL)

def get_current_playing(this):
    if this.token:
        sp = spotipy.Spotify(auth=token)
        current = sp.currently_playing(market=None)
        if current:
            song = sp.currently_playing(market=None)['item']
            name = song['name']
            album = song['album']['name']
            artists = song['artists']
            artist = artists[0]['name']
            for artistIndex in range (1, len(artists)):
                artist += ', ' + artists[artistIndex]['name']
            return '' + name + ' - ' + artist + ' (' + album + ')'
        else:
            return  "currently not playing anything"
    else:
        print("Can't get token for", this.user)
        return "unable to accept user"