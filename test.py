import pygn
from pygn import createRadio
clientID = '1583510492-53167BEABBED3ED8E1CF71F85230E1AF'
userID = '280729569058437012-F8B3D95D64EA8DD505BA40697C34A407'

def mood():
    playlist = pygn.createRadio(clientID=clientID, userID=userID, mood='42960', genre = '36056', popularity ='1000', count='10')
    print(playlist)

def test():
    metadata = pygn.search(clientID=clientID, userID=userID, artist='Kings Of Convenience', album='Riot On An Empty Street', track='Homesick')
    print(metadata)


mood()