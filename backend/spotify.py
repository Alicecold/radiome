import spotipy
import spotipy.util as util
import sys
import secret as app

token = ''
user = ''

def login(this):
    if len(sys.argv) > 1:
        this.user = sys.argv[1]
    else:
        this.user = 'alicecold'
    this.token = util.prompt_for_user_token(this.user,'user-read-currently-playing',client_id=app.CLIENT_ID,client_secret=app.CLIENT_SECRET,redirect_uri=app.REDIRECT_URL)

def get_current_playing(this):
    if this.token:
        sp = spotipy.Spotify(auth=token)
        sp.user(this.user)
        current = sp.currently_playing(market=None)['item']
        name = current['name']
        album = current['album']['name']
        artists = current['artists']
        artist = artists[0]['name']
        for artistIndex in range (1, len(artists)):
            artist += ', ' + artists[artistIndex]['name']
        print 'Currently Playing: \n', name, '-', artist, '(' + album + ')'
        return 'Currently Playing: \n' + name + ' - ' + artist + ' (' + album + ')'
    else:
        print "Can't get token for", this.user
        return "unable to accept user"