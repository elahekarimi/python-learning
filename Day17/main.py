class User:
    def __init__(self, user_id, username, ):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("123", "elahe")
user_2 = User("124", "goli")
user_1.follow(user_2)
# print(user_1.username)
# print(user_1.id)
print(user_1.followers)
print(user_1.following)

# user_1.id = "123"
# user_1.username = "angela"
# print(user_1.username)
# print(user_1.id)
