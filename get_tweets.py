import csv
import time

def read_index(path):
    index = {}
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            # term = row[0]
            # postings_str = row[1]
            index[row[0]] = row[1]
    return index

def get_postings_list(index, term):
    postings_str = ''
    for i in index:
        if i == term:
            postings_str = index[i]
    list = postings_str.split(' ')
    del list[-1]
    return list

def get_tweet_list(path, postings_list):
    tweets = {}
    matches = {}
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            tweet = row[0]
            id = row[5]
            tweets[row[5]] = row[0]

    for t in tweets:
        if t in postings_list:
            matches[t] = tweets[t]

    print(len(matches))

index = read_index('./indexes/realDonaldTrump.csv')
postings_list = get_postings_list(index, 'great')
print('len: ' + str(len(postings_list)))
tweet_list = get_tweet_list('./final_timelines/realDonaldTrump.csv', postings_list)
