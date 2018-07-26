from urllib.request import urlopen

print (urlopen('https://www.pretzel.rocks/api/v1/playing/twitch/gameplayercole').read())
