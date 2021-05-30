from instascrape import *
url = 'https://www.instagram.com/explore/locations/213264682/almaty-kazakhstan/'
almaty = Location(url)
almaty.scrape()
print(f"Almaty location tag has {almaty.amount_of_posts:,} posts")

posts = almaty.get_recent_posts(amt=1)
# id = '1308525991'
# for post in posts:
print(posts[0].to_dict(True))

# joe = Profile(id)
# joe.scrape()
google_post = Post('https://www.instagram.com/p/CPXwkbaHTht/')
google_post.scrape()
print(google_post.to_dict(True))

# joe = Profile("joebiden")
# joe.scrape()
# posts = joe.get_posts(webdriver=webdriver, login_first=True, amount=10, scrape=True)
# print(posts)
# scraped_posts, unscraped_posts = scrape_posts(posts, headers=headers, pause=10)
