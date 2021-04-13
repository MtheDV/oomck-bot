import random

import flickrapi


class Flickr:

    def __init__(self):
        api_key = u'8e436801391bcdc8196053b454abd916'
        api_secret = u'e1c52d216198a82a'
        self.flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

    def search_photo(self, text):
        return self.flickr.photos.search(text=text, per_page='150')['photos']['photo'][int(random.random() * 150)]
