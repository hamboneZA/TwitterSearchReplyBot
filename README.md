Twitter Search and Reply

Python script to search Twitter for a phrase / hashtag / whatever and reply to a returned result with random pre-defined phrases.

Prerequisites

git - to clone this repo (you can fetch it in other ways, of course)

python3

Twython

Install

Python 3 and pip

python ––version


If nothing is returned or version is lower than 3.6 add a new repo (this repo is usually more current than official):

sudo apt update 
sudo apt install software-properties-common 
sudo add-apt-repository ppa:deadsnakes/ppa 
sudo apt update


And install...

sudo apt install Installpython3.8 && sudo apt install pip3 -y


Do python -- version again and check if the new version was installed. If you had python 2 installed previously it might show that old version because we've not updated .env. in which case check the Python 3 version using python3 --version.

Tywthon

Install using pip

either pip install twython or pip3 install twython (depending on the situation as described above).

pip install twython   # if python --version returns v3 +
pip3 install twython


Twitter_Auto_Reply

TODO: Move to github repo

git clone https://box.keepwalking.life/cloud/index.php/s/HWRggWbDa4DxpR2

Auth Params

Append the Twitter API credentials to auth.py:

nano auth.py


Define Responses

TODO: a responses.txt so adding replies is less technical.

Add all the possible responses to twitter_app.py

#These are the tweets the bot can send
rand_message = ['Did you mean "unpredictable?"', 'Did you mean "inconsistent"?', 'Did you mean "temperamental"?', 'Did you mean "unreliable"?',]


Responses should be surrounded by single-quotes and separated by a comma. If a literal single-quote is expected to print in the reply it should be escaped like \'. The final response must be followed by a comma. All replies must be surrounded by [ ].

.... Done!

Run the script and enter the search terms when prompted.

python3 twitter_app.py 


or

python twitetr_app.py


Script will search every 15 seconds and reply with one of the random phrases set until it is stopped with a Ctrl+C interrupt.
