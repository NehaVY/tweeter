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
<<<<<<< HEAD
 
 This Python program allows users to post tweets to Twitter interactively using the Tweepy library. It authenticates with the Twitter API using API keys and tokens and prompts the user to enter tweets. The program checks for empty inputs and allows users to post multiple tweets until they type "exit" to quit. It posts the tweet using the client.create_tweet() method and displays the Tweet ID for confirmation. Error handling ensures that issues are gracefully managed without crashing the program.
 
 ![image](https://github.com/user-attachments/assets/78059ed8-0112-4700-9a99-b8ed8540af66)
 
 

**Viewing the Tweet**

![image](https://github.com/user-attachments/assets/cf51d256-10dd-4eae-98ec-5b4ad2f39889)
=======
 ![image](https://github.com/user-attachments/assets/78059ed8-0112-4700-9a99-b8ed8540af66)
 This Python program allows users to post tweets to Twitter interactively using the Tweepy library. It authenticates with the Twitter API using API keys and tokens and prompts the user to enter tweets. The program checks for empty inputs and allows users to post multiple tweets until they type "exit" to quit. It posts the tweet using the client.create_tweet() method and displays the Tweet ID for confirmation. Error handling ensures that issues are gracefully managed without crashing the program.

**Viewing the Tweet**
![image](https://github.com/user-attachments/assets/cf51d256-10dd-4eae-98ec-5b4ad2f39889)


**Deleting the Tweet**


![image](https://github.com/user-attachments/assets/cdfabf74-1adf-4a25-a773-e9d9e45703a5) 
 -
 **Checking if the Tweet is deleted**
![image](https://github.com/user-attachments/assets/e961bfe2-8787-44b3-9b91-b98521ddf63d)
>>>>>>> 2d2901b05ee40eeab41873e952d097bb3cda4538


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
The code authenticates for posting a tweet by using OAuth 1.0a credentials to authorize API requests on behalf of your Twitter account.
authentication = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(authentication)

**Authentication  for Deleting the tweet**.

This setup uses OAuth 1.0a credentials to authenticate your access to Twitter's API via the tweepy.Client. With this, you can make authorized requests, including deleting tweets, ensuring secure interaction with your Twitter account.

clients = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

**Error Handling**

Includes robust error handling for various API responses, such as unauthorized access, rate limits, and tweet not found errors.
**Error handling in posting the tweet**
![image](https://github.com/user-attachments/assets/a642690c-ca18-45ab-bf7a-7af6998f1deb)

**Error handling in delete the tweet**
![image](https://github.com/user-attachments/assets/371b66a7-0b00-4bf6-a05d-991d53f8cf52)




