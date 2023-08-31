playlist = {
    'title': 'patagonia bus', 
    'author': 'Patagonia', 
    'songs': [
      {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
      {'title': 'song2', 'artist': ['djblue'], 'duration': 3.75},
      {'title': 'song3', 'artist': ['sting'], 'duration': 6.5},
   ]
}

total_length = 0
for song in playlist['songs']:
    print(song['artist'])
    total_length += song['duration']
print(total_length)