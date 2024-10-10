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
 ![image](https://github.com/user-attachments/assets/78059ed8-0112-4700-9a99-b8ed8540af66)
 This Python program allows users to post tweets to Twitter interactively using the Tweepy library. It authenticates with the Twitter API using API keys and tokens and prompts the user to enter tweets. The program checks for empty inputs and allows users to post multiple tweets until they type "exit" to quit. It posts the tweet using the client.create_tweet() method and displays the Tweet ID for confirmation. Error handling ensures that issues are gracefully managed without crashing the program.

**Viewing the Tweet**
![image](https://github.com/user-attachments/assets/cf51d256-10dd-4eae-98ec-5b4ad2f39889)


**Deleting the Tweet**


![image](https://github.com/user-attachments/assets/cdfabf74-1adf-4a25-a773-e9d9e45703a5) 
 -
 **Checking if the Tweet is deleted**
![image](https://github.com/user-attachments/assets/e961bfe2-8787-44b3-9b91-b98521ddf63d)


