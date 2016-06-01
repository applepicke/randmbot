import tweepy
import settings

class TwitterConnectionManager:
    """
    Manages connection to Twitter API, including querying results and posting
    to Twitter
    """
    logged_in = False

    def __init__(self):
        self.login()

    def login(self):
        if not self.logged_in:
            self.auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
            self.auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

            self.api = tweepy.API(self.auth)

        return self.api

#
#
# class CacheManager:
#     """
#     Caches previous posts that have been responded to
#     """
#     pass
#
# class RandMReferenceGenerator:
#     """
#     Generates phrases and appropriate responses to those phrases
#     """
#     pass
#
# class RandM:
#     """
#     The Rick and Morty Reference Driver. The main application.
#     """
#
#     def __init__(self):
#         pass

if __name__ == '__main__':
    manager = TwitterConnectionManager()
