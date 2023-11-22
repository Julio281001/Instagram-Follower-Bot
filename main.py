from instagramBot import InstagramBot

bot = InstagramBot()

bot.sign_in()
bot.find_account(input('Enter an username: '))
bot.follow()