#Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
An access token is an object that describes the security context of a process or thread.
The information in a token includes the identity and privileges of the user account associated with the process or thread.
When a user logs on, the system verifies the user's password by comparing it with information stored in a security database. ' \
'If the password is authenticated, the system produces an access token. ' \
Every process executed on behalf of this user has a copy of this access token.

access token for twitter.
Consumer Key="WFAZDVa09hdbfjiCXcY6JMv2bl"
Consumer Secret="yW5yjTLaGn01cp1FUdbdJpoaOAOnhfhdsjb9BKmeKOGoRbZRqc"
Access Token="10111302136758995264-6v8QrVAfGpUvNBhgndjdk5HyNUHP7A"
Access Token Secret="droig2cci9D3B3cDushIYGbWPyj4hCBKC6hwTD0mnfnZkqD"

#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.
c:\users\A-1>nslookup google.com
server: unknown
Addresses: 192.168.43.1

Non-authoritative answer:
Name: google.com
Addresses: 2404:6800:4002:802::200e
           172.217.31.14

c:\users\A-1>nslookup facebook.com
server: unknown
Addresses: 192.168.43.1

Non-authoritative answer:
Name: facebook.com
Addresses: 2a03:2880:f12f:83:face:b00c:25de
           157.240.16.35

c:\users\A-1>nslookup twitter.com
server: unknown
Addresses: 192.168.43.1

Non-authoritative answer:
Name: twitter.com
Addresses: 64:ff9b::68f4:2ac1
           64:ff9b::68f4:2a81
            104.244.42.1
            104.244.42.65


#Q.3- Using Tweepy library try to extract tweets from Twitter.
import tweepy
consumer_key='WFAZDVa09HUpEiChsggsY6JMv2bl'
consumer_secret='yW5yjTLaGn01cp1FUdbdJpoaOhfjdhgkdVdUu6BKmeKOGoRbZRqc'
access_token='1011130213875649526-mnf,dsnmfQrVAfGpUvNB1f4iRQg5HyNUHP7A'
access_token_secret='droig2cci9D3B3hkdshfkdIYGbWPyj4hCBKC6hwTD0hRZkqD'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
n=str(input("enter any HASH tag for search:"))
tweets=api.search(n,lang='en',count='10',tweet_mode='extended')
print("tweets")
for tweet in tweets:
    print("*************************")
    print(tweet.full_text)
    print("*************************")

#Q.4- What is a difference between library and API . Figure it out with examples.
LIBRARY=In computing, a library is a collection of similar objects that are stored for occasional use -
    most frequently, programs in source code or object code form, data files, scripts, templates, fonts, and physical storage units such as tape cartridges.
    Here are some common types of libraries.
API=An application programming interface (API) is a particular set of rules ('code') and specifications that software programs can follow to communicate with each other.
It serves as an interface between different software programs and facilitates their interaction, similar to the way the user
interface facilitates interaction between humans and computers.



