#  TwitterSearchReplyBot

Python script to search Twitter for a phrase / hashtag / whatever and reply to a returned result with random pre-defined phrases. I did this on Ubuntu 16.04, but Python anywhere would work, I guess. I stupidly screwed up my Python versions - don't make my mistake and install it properly or use a suitable venv.

## Prerequisites

- Python (3.6+)
- Twython

### Install

#### Python 3 and pip

<code>python ––version</code>

If nothing is returned or version is lower than 3.6 add a new repo (this repo is usually more current than official):

<block>sudo apt update <br>
sudo apt install software-properties-common <br>
sudo add-apt-repository ppa:deadsnakes/ppa  <br>
sudo apt update</block>

And install...

<code>sudo apt install Installpython3.8 && sudo apt install pip3 -y</code>


Do <code>python -- version</code> again and check if the new version was installed. If you had python 2 installed previously it might show that old version because we've not updated .env. in which case check the Python 3 version using python3 --version and use <code>$ python3 ... </code> if you're lazy and don't want to set things up as they should be.

## Tywthon

Install using pip

either <code>pip install twython</code> or <code>pip3 install twython</code> (depending on the situation as described above).

<code>pip install twython</code>

## Twitter_Auto_Reply

<i>TODO: Move to github repo</i>

<code>git clone https://github.com/hamboneZA/TwitterSearchReplyBot.git</code>

#### Auth Params

Append the Twitter API credentials to auth.py (there's some guidance in in the file):

<code>nano auth.py</code>

#### Define Responses

<i>TODO: a responses.txt so adding replies is less technical.</i>

Add all the possible responses to twitter_app.py

<code>nano twitter_app.py</code>
<code/>rand_message = ['Did you mean "unpredictable?"', 'Did you mean "inconsistent"?', 'Did you mean "temperamental"?', 'Did you mean "unreliable"?',]</code>


Responses should be surrounded by single-quotes and separated by a comma. If a literal single-quote is expected to print in the reply it should be escaped like \'. The final response must be followed by a comma. All replies must be surrounded by [ ].

.... Done!

Run the script and enter the search terms when prompted.

<code>python twitter_app.py</code>

You may need to make the file executable, so do <code>sudo chmod -x twitter_app.py</code> Script will search every 5 seconds and reply with one of the random phrases set until it is stopped with a Ctrl+C interrupt.
