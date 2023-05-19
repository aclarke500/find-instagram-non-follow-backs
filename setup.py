# Importing Libraries
import instaloader
import pandas as pd

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
bot.login(user="username", passwd="password")
print(1)
# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'summer.clarkee')
print(2)
# Retrieving the usernames of all followers
# followers = [follower.username for follower in profile.get_followers()]
print(1)
# Converting the data to a DataFrame
# followers_df = pd.DataFrame(followers)
print(1)
# Storing the results in a CSV file
# followers_df.to_csv('followers.csv', index=False)
print(1)
# Retrieving the usernames of all followings
followings = [followee.username for followee in profile.get_followees()]
print(1)
# Converting the data to a DataFrame
followings_df = pd.DataFrame(followings)
print('egg')
# Storing the results in a CSV file
followings_df.to_csv('followings.csv', index=False)