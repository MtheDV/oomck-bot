import twitter


class VinTwitter:
    """
    Class for getting tweets from vin_twitter
    """

    def __init__(self):
        self.api = twitter.Api(consumer_key="aVIKoxmo5ESrbMiaeWURD1aLA",
                               consumer_secret="ashUBQyRMbCvTONTvzqIhIftoAJ6UYRaXxiYKNyyBkgtUMSFdp",
                               access_token_key="1381726009691541506-w7dAINdKQh5XkbKFA3ZtzmBlEK84yo",
                               access_token_secret="JOPKFLl5nHL2O9XrniE5RIg5Admfmz0j091MGBqdNxb0n")

    def search(self, term, count, result_type):
        return self.api.GetSearch(term=term, count=count, lang='en', result_type=result_type)
