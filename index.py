import csv
import time

from tweet import Tweet

def print_tweet_list(tweets):
    for tweet in tweets:
        tweet.print_tweet()

def objectify_tweets(file):
    tweet_list = []
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            tweet = Tweet(row[0], row[1], row[2], row[3], row[4], row[5])
            tweet_list.append(tweet)
    tweet_list.pop(0)
    return tweet_list

def tokenize_tweet_list(tweet_list):
    word_list = []
    for tweet in tweet_list:
        words = tweet.get_word_tokens()
        for word in words:
            word_list.append((word, tweet.tweetID))
    return word_list

def print_index(index):
    for i in index:
        print i
        print index[i]
        print 'times: ' + str(len(index[i])) + '\n'

def index_tokens_dict(token_list):
    index = {}
    for token in token_list:
        if token[0] in index:
            index[token[0]].append(token[1])
        else:
            index[token[0]] = [token[1]]
    return index

def get_max_term(index):
    x = 0
    while x < 10:
        max_len = 0
        term = ""
        for i in index:
            if max_len < len(index[i]):
                max_len = len(index[i])
                term = i
        del index[term]
        print("term: " + term)
        print("max len: " + str(max_len) + '\n')
        x += 1

def sort_index(index):
    x = 0
    while x < 21:
        max_len = 0
        term = ""
        for i in index:
            if max_len < len(index[i]):
                max_len = len(index[i])
                term = i


        # instead of just deleting this, add the thing to a new
        # index that is sorted and return it at end

        # I think index[term] is the postings list itself
        # and term is the term that represents that postings list.
        del index[term]

        # Add that index to a new thing that will end up being an ordered index.
        # Do it in a different function maybe, then save that new index to a new CSV file
        # Then in another python file, we can then search a term and browse tweets that contain that term.

        print("term: " + term)
        print("max len: " + str(max_len) + '\n')
        x += 1

t0 = time.clock()

tweet_list = objectify_tweets('./final_timelines/nytimes.csv')
token_list = tokenize_tweet_list(tweet_list)
index = index_tokens_dict(token_list)
#get_max_term(index)
sort_index(index)

print time.clock(), ' total elapsed time.'
