import csv, os
from tweet import Tweet

def print_tweet_list(tweets):
    for tweet in tweets:
        tweet.print_tweet()

def objectify_tweets(file):
    tweet_list = []
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            tweet = Tweet(row[0], row[1], row[1], row[2], row[3], row[4])
            tweet_list.append(tweet)
    # 1st element in tweet_list contains column titles
    tweet_list.pop(0)
    return tweet_list

def reformat_tweets(tweets):
    i = 0
    for tweet in tweets:
        tweet.split_date()
        tweet.get_hashtags()
        tweet.get_ats()
        tweet.lower_tweet()
        tweet.set_id(str(i))
        tweet.strip_hyperlinks()
        tweet.strip_stop_words()
        tweet.strip_symbols()
        tweet.encode_tweets()
        i += 1
    return tweets

# TODO: Make this call format_data(file) for each .csv file in path
def format_all_in_directory(path):
    print("Formatting all data in: " + path)
    for root,dirs,files in os.walk(path):
        for file in files:
           if file.endswith(".csv"):
               format_data(file)

# Function that is used to call all the other formatting methods
def format_data(file):
    print("START Formatting data in: " + file)
    tweets = objectify_tweets('./timelines/' + file)
    tweets = reformat_tweets(tweets)
    save_tweets(tweets, file)
    print("DONE formatting data in: " + file)

def save_tweets(tweet_list, file):
    print("Saving tweets to: ./final_timelines/" + file)
    with open('./final_timelines/' + file, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['tweet', 'date', 'time',
                            'favorites', 'retweets',
                            'tweetID', 'hashtags', 'ats'])
        for tweet in tweet_list:
            csv_writer.writerow([tweet.tweet, tweet.date, tweet.time,
                                 tweet.favorites, tweet.retweets, tweet.tweetID,
                                 tweet.hashtags,tweet.ats])

format_all_in_directory('./timelines')

# Just to format realDonaldTrump's tweets
# format_data('./timelines/realDonaldTrump.csv')
