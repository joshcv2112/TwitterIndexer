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

# This isn't really being used anymore!
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
    sorted_index = {}
    while x < 100:
        max_len = 0
        term = ""

        for i in index:
            if max_len < len(index[i]):
                max_len = len(index[i])
                term = i

        sorted_index[term] = index[term]
        del index[term]
        x += 1
    return sorted_index

def save_index(index, path):
    with open('./indexes/realDonaldTrump.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['term', 'postings_list'])
        for term in index:
            postings_list = index[term]
            postings_str = ""
            for id in postings_list:
                postings_str += id
                postings_str += " "
            csv_writer.writerow([term, postings_str])
    print('Index saved to: ' + path)

t0 = time.clock()

tweet_list = objectify_tweets('./final_timelines/realDonaldTrump.csv')
token_list = tokenize_tweet_list(tweet_list)
index = index_tokens_dict(token_list)
index = sort_index(index)
save_index(index, './indexes/realDonaldTrump.csv')

print time.clock(), ' total elapsed time.'
