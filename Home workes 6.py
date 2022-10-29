import random
my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
songs = list(my_favorite_songs.items())
songs = random.sample(songs, 3)
time = (songs[0][1] + songs[1][1] + songs[2][1])
print(*songs)
print('Три песни звучат:', round(time, 2), 'минут.')

# Отлично. Вот мой вариант
time = 0
for song in sample(tuple(my_favorite_songs), 3):
    print(song)
    time += my_favorite_songs[song]

print(f'Три песни звучат {round(time, 2)}')
