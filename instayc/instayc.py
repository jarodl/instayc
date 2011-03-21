import os
from ConfigParser import SafeConfigParser, NoOptionError
from getpass import getpass
from instapaperlib import Instapaper
from feedparser import parse
from operator import itemgetter

OPTIONS = {
    'config_filename': os.environ.get('HOME', '') + os.sep + '.instayc',
    'feeds': {
        'yc': 'http://news.ycombinator.com/rss'
    },
}

class Instayc:

    section = 'instayc'

    def __init__(self):
        self.insta = None
        self.config = self.loadConfig()

    def loadConfig(self):
        config = SafeConfigParser()
        filename = OPTIONS.get('config_filename')

        if os.path.exists(filename):
            config.read(filename)
        else:
            with open(filename, 'wb') as configfile:
                config.add_section(self.section)
                config.set(self.section, 'interests', '')
                config.write(configfile)
        return config

    def saveConfig(self):
        with open(OPTIONS.get('config_filename'), 'wb') as configfile:
            self.config.write(configfile)

    def requires_login(fn):
        def wrapped(self):
            try:
                self.authorize(self.config.get(self.section, 'email'),
                    self.config.get(self.section, 'password'))
            except NoOptionError:
                self.login()
            fn(self)
        return wrapped

    def authorize(self, email, password):
        self.insta = Instapaper(email , password)
        (code, message) = self.insta.auth()
        if code == 403:
            self.login()
        else:
            self.config.set(self.section, 'email', email)
            self.config.set(self.section, 'password', password)
            self.saveConfig()

    def login(self):
        email = raw_input('Instapaper email: ')
        password = getpass('Instapaper password: ')
        self.authorize(email, password)

    def add_interests(self, interests):
        current_interests = self.config.get(self.section, 'interests')
        if current_interests == '':
            current_interests = interests
        else:
            current_interests = current_interests + ', ' + interests
        self.config.set(self.section, 'interests', current_interests)
        self.saveConfig()

    @requires_login
    def update(self):
        print "Updating..."
        posts = parse(OPTIONS['feeds']['yc']).entries
        interests = self.config.get(self.section, 'interests').split(',')

        def map(words):
            mapping = []
            for word in words:
                mapping.append((word.strip(), 1))
            return mapping

        def reduce(mapping):
            counted = {}
            for word, count in mapping:
                counted[word] = counted.get(word, 0) + count
            return counted

        found = []
        for post in posts:
            title = str(post['title'].encode('utf-8'))
            title_words = [word.lower() for word in title.split(' ')]
            title_words.extend(interests)
            counted = reduce(map(title_words))
            matches = [word for word, count in counted.items() if count > 1]
            if matches:
                found.append((post['link'], title))
                self.insta.add_item(post['link'], title)
        print "Added %d article(s) to Instapaper: \n" % len(found)
        for link, title in found:
            print title
        print ''
