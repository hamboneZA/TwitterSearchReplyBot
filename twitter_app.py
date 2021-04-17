#! python
######################################################################################################
# Author: James Hamilton
# Date :  17.05.2021
# Description: Interactively search Twitter for a phrase and reply to tweets.
# This script will ask for a search term and then reply a randomly selected
# tweet in intervals. DO NOT run this unattended without either modifying the
# code below to run in a responsible way.
######################################################################################################

# We're going to import a Twitter API library - Twython. 
from twython import Twython

# We're calling a function to randomise the replies we send and time
import random
import time

# We're now going to fetch out API credentials from the auth.py file.
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# ... and tell Twython to use them. 
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# We'll set the stage to record and inform the actions we're about to do
ids_replied_to = []
with open('ids_replied_to.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]
        # add item to the list
        ids_replied_to.append(current_place)

# OK, now we're going to search for something using a simple API search. You
# could use an advanced search too, I think.
print('')
print('')
search_term = input('Find what? ')

results = twitter.cursor(twitter.search, q=search_term)

print('')
print('Finding that now....')
print('')

# These are the tweets the bot can send
rand_message = ['REPLY 1', 'REPLY 2', 'etc...',]

for result in results:

    name = result['user']
    screen_name = name['screen_name']

    creation_date = result['created_at']

    tweet_txt = result['text']

    id = result['id']

    print('Twitter User:', screen_name)
    print('Posted:')
    print(tweet_txt)
    print('at:')
    print(creation_date)
    print('')

  
# Now, a reply will be sent to tweets in time descending order that have not
# already been replied to.
    id = str(id)
    if id in ids_replied_to:
        print('')
        print('Skipped as already replied to')
        print('')
        print('')
    else:
        twitter_handle = '@' + screen_name
        message = twitter_handle + " " + random.choice(rand_message)
        twitter.update_status(status=message, in_reply_to_status_id=id)
        print("Tweeted: %s" % message)
	# The reply has been sent, now we make a record that we replied so we 
	# don't reply to our own tweet (or the one we replied to, again).
        id = int(id)
        ids_replied_to.append(id)
        with open('ids_replied_to.txt', 'w') as filehandle:
            filehandle.writelines("%s\n" % place for place in ids_replied_to)
	# Twitter doesn't like it when bots reply either too quickly, or too
	# too many times (relevant if you only have a few random tweets.
        time.sleep(5)
	# So, we wait X seconds before searching for replying to the next tweet

