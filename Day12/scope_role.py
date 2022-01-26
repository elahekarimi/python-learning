# b=15
# def eli():
#     a=2
#     print(a)
#     def goli():
#         print(b)
#     goli()
# eli()
game_enemy=3
def create_enemy():
    enemys=["skeleton", "zombi", "alien"]
    if game_enemy < 5:
        new_enemy=enemys[0]
    print(new_enemy)
create_enemy()