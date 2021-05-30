from instascrape import *

google = Profile('https://www.instagram.com/kassymzhan_assim/')
google_post = Post('https://www.instagram.com/p/CPL1NLWhRqn/')
google_hashtag = Hashtag('https://www.instagram.com/explore/tags/btw/')

google.scrape()
google_post.scrape()
google_hashtag.scrape()

print(google.followers)
# print(google_post['hashtags'])
print(google_hashtag.amount_of_posts)