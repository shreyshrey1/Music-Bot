import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = 'shreyshrey1'
util.prompt_for_user_token(username, client_id='fb611220c5974bf3a1472de90c359dfc',client_secret='67294c80b4274ffc80dad0943500a566',redirect_uri='http://localhost:8888')

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print track['name'] + ' - ' + track['artists'][0]['name']
else:
    print "Can't get token for", username