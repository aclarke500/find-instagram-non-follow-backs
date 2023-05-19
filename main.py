def get_users(filename):
    temp=[]
    with open(filename, "r") as file:
        for line in file:
            temp.append(line.strip())
    return temp

followers=get_users("adam_followers.csv")
following=get_users("adam_followings.csv")
followers.sort()
following.sort()
print(followers, following)

non_follow_backs = []

# for followee in following:
#     found = False
#     for follower in followers:
#         if follower == followee:
#             found = True
#     if not found:
#         non_follow_backs.append(followee)
# print(len(non_follow_backs))

for followee in following:
    if followers.count(followee) == 0:
        non_follow_backs.append(followee)

with open('non_follow_backs.csv', "w") as file:
    for n in non_follow_backs:
        file.write(n+"\n")
print(len(non_follow_backs))