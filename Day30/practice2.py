facebook_post = [
    {'like': 20, 'comments': 10},
    {'like': 10, 'comments': 2, 'share': 2},
    {'like': 2, 'comments': 5, 'share': 3},
    {'share': 3, 'comments': 1},
    {'share': 3, 'comments': 5},
    {'like': 4, 'comments': 6},
]
total = 0
for post in facebook_post:
    try:
        total = total + post['like']
    except KeyError:
        pass
print(total)
