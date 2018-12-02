import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Tweet:
    def __init__(self, tweet, date, time, favorites, retweets, tweetID):
        self.tweet = tweet
        self.date = date
        self.time = time
        self.favorites = favorites
        self.retweets = retweets
        self.tweetID = tweetID
        self.hashtags = []
        self.ats = []

    def print_tweet(self):
        print('Tweet ID: ' + self.tweetID)
        print('Tweet: ' + self.tweet)
        print('Date: ' + self.date)
        print('Time: ' + self.time)
        print('Hashtags: ' + str(self.hashtags))
        print('Ats: ' + str(self.ats))
        print('Favorites: ' + self.favorites)
        print('Retweets: ' + self.retweets + '\n')

    def encode_tweets(self):
        self.tweet = self.tweet.encode('ascii', 'ignore')
        self.date = self.date.encode('ascii', 'ignore')
        self.time = self.time.encode('ascii', 'ignore')
        self.favorites = self.favorites.encode('ascii', 'ignore')
        self.retweets = self.retweets.encode('ascii', 'ignore')
        self.tweetID = self.tweetID.encode('ascii', 'ignore')
        self.hashtags = str(self.hashtags).encode('ascii', 'ignore')
        self.ats = str(self.ats).encode('ascii', 'ignore')

    def strip_symbols(self):
        filtered_sentence = ""
        symbols = ['.', ',', '/', '*', '+', '-', '\`', '\'', '\"',
                    '``', '\'s', '-', '--', '!', '?', '\'d', '\'re',
                    ';', ':', '|', '[', ']', '\'m', '(', ')', '\'t'
                    'ca', 'n\'t', '...', '\'ll', '&', '^', 'I', '!',
                    ':', '$', '%', '=', '@', 'get', 'would']
        words = word_tokenize(self.tweet)
        for word in words:
            if word not in symbols:
                filtered_sentence += word
                filtered_sentence += ' '
        self.tweet = filtered_sentence

    def get_hashtags(self):
        self.hashtags = re.findall(r"#(\w+)", self.tweet)
        self.tweet = re.sub(r"#(\w+)", '', self.tweet)

    def get_ats(self):
        self.ats = re.findall(r"@(\w+)", self.tweet)
        self.tweet = re.sub(r"@(\w+)", '', self.tweet)

    def get_word_tokens(self):
        return word_tokenize(str(self.tweet).decode("utf8"))

    def strip_stop_words(self):
        stop_words = set(stopwords.words("english"))
        filtered_tweet = ""
        words = word_tokenize(str(self.tweet).decode("utf8"))
        for word in words:
            if word not in stop_words:
                filtered_tweet += word
                filtered_tweet += " "
        self.tweet = filtered_tweet

    def strip_hyperlinks(self):
        self.tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', self.tweet)

    def split_date(self):
        temp = self.date
        self.date = temp.split()[0]
        self.time = temp.split()[1]

    def lower_tweet(self):
        self.tweet = self.tweet.lower()

    def set_id(self, val):
        self.tweetID = val
