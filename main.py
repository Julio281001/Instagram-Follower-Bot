from instagramBot import InstagramBot

username = input('Enter a username:')

bot = InstagramBot()

bot.sign_in()
bot.find_account(username)
bot.follow()