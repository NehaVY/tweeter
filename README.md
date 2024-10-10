# Twitter API Project for Posting and Deleting Tweets

## Project Overview

This project is a **Twitter API Project** built using the [Twitter API](https://developer.twitter.com/en/docs). It allows users to perform two main functions: posting new tweets and deleting existing tweets by interacting with the Twitter API.

## Features

- **Posting Tweets**: Input a message to post directly to your Twitter account.
- **Deleting Tweets**: Remove a tweet from your Twitter timeline by providing its Tweet ID.
- **Basic Error Handling**: Ensures smooth operation by catching common errors like invalid Tweet IDs or permission issues.

## Installation

### Prerequisites

- **Python 3.8** installed on your system.
- A Twitter Developer account with access to API credentials, 

 ## Setting up a Twitter Developer Account
 ## 1. Create a Twitter Account

Sign up for a Twitter account at [Twitter.com](https://twitter.com/) if you don’t have one.

## 2. Apply for a Developer Account

Go to the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard) and apply for a developer account. Choose the account type based on your use case (Hobbyist, Academic, or Business).


 
- **Generate API Keys**:

    Go to Projects & Apps → Your App → Keys and Tokens.
    Generate the following keys and tokens:API Key,API Secret Key,Bearer Token,Access Token
    and Access Token Secret
    
## 3. Project Details

 **Posting the Tweet**
 
 This Python program allows users to post tweets to Twitter interactively using the Tweepy library. It authenticates with the Twitter API using API keys and tokens and prompts the user to enter tweets. The program checks for empty inputs and allows users to post multiple tweets until they type "exit" to quit. It posts the tweet using the client.create_tweet() method and displays the Tweet ID for confirmation. Error handling ensures that issues are gracefully managed without crashing the program.
 
 ![image](https://github.com/user-attachments/assets/78059ed8-0112-4700-9a99-b8ed8540af66)
 
 

**Viewing the Tweet**

![image](https://github.com/user-attachments/assets/cf51d256-10dd-4eae-98ec-5b4ad2f39889)


**Deleting the Tweet** 

This Python program uses the Tweepy library to allow users to delete their tweets via the Twitter API. After authenticating with OAuth1 using Twitter API credentials, the program prompts the user to input a Tweet ID to delete. It checks for valid input and deletes the tweet using api.destroy_status(). The program handles common errors like invalid Tweet IDs, permission issues, and rate limits, ensuring a smooth and interactive process. The loop continues until the user types "exit" to quit the program.


![image](https://github.com/user-attachments/assets/cdfabf74-1adf-4a25-a773-e9d9e45703a5) 
 -
 **Checking if the Tweet is deleted**
  
  
  The Post Good Morning All is deleted.
  
![image](https://github.com/user-attachments/assets/e961bfe2-8787-44b3-9b91-b98521ddf63d)

## 4. Authentication and Error Handling

We  have to give the credentials for authentication.
This allows the program to perform actions like posting and deleting tweets on behalf of the authenticated user.

**Authentication  for Posting the tweet**.

authentication = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(authentication)

**Authentication  for Deleting the tweet**.

clients = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

**Error Handling**

The program is designed to handle errors in a systematic approach, ensuring it doesn’t crash while providing helpful feedback. For instance, if a tweet can’t be found, it uses the tweepy.NotFound exception to let users know. When users exceed their API limits, the tweepy.TooManyRequests exception kicks in to inform them about the rate limit issue. Permission problems are managed with the tweepy.Forbidden exception, explaining why certain tweets can't be deleted. General Tweepy-related errors and unexpected issues are caught by tweepy.TweepyException and a general Exception block, respectively.

