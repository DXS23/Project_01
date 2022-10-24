import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
songs = random.sample(my_favorite_songs, 3)
time = (songs[0][1] + songs[1][1] + songs[2][1])
print(*songs)
print('Три песни звучат:', round(time, 2), 'минут.')
