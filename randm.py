import tweepy
import settings

class NoResultsException(Exception):
    pass

class CacheManager:
    """
    Caches previous posts that have been responded to
    """
    cache_list = []

    def is_cached(self, tweet):
        return False


class TwitterConnectionManager:
    """
    Manages connection to Twitter API, including querying results and posting
    to Twitter
    """
    logged_in = False

    def __init__(self):
        self.login()
        self.cache = CacheManager()

    def login(self):
        if not self.logged_in:
            self.auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
            self.auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
            self.api = tweepy.API(self.auth)
            logged_in = True

        return self.api

    def all_tweeted_at(self):
        tweets = self.api.home_timeline()

    def post_reply(self, msg, tweet):
        msg = '@%s %s' % (tweet.author.screen_name, msg)
        self.api.update_status(msg, tweet.id)

    def find_quotes(self, search):

        page = 0
        results = []

        while not page or len(results):
            page += 1
            results = self.api.search(search, 'en', rpp=100)

            for result in results:

                if self.cache.is_cached(result):
                    continue

                return result

        raise NoResultsException('Could not find any results!')


class RandMReferenceGenerator:
    """
    Generates phrases and appropriate responses to those phrases
    """
    quote_map = {
        'What is my purpose?': 'You pass butter'
    }

    def __init__(self):
        pass

    def test_reference(self, reference):
        """
        Test a provided quote to see if it needs correction, or whether it is
        missing a response. These are the ones we want to reply to.
        """
        pass

class RandM:
    """
    The Rick and Morty Reference Driver. The main application.
    """

    def __init__(self):
        self.connection = TwitterConnectionManager()
        self.ref_gen = RandMReferenceGenerator()

    def find_next_quote(self):
        # TODO: all quotes
        quote = list(self.ref_gen.quote_map.keys())[0]

        return self.connection.find_quotes(quote)

    def post_reply(self, msg, tweet):
        self.connection.post_reply(msg, tweet)

    def mortify(self):
        """
        Find the next plausible post and reply to it
        """
        tweet = self.find_next_quote()
        msg = list(self.ref_gen.quote_map.values())[0]
        self.post_reply(msg, tweet)

if __name__ == '__main__':
    randm = RandM()
    result = randm.mortify()
