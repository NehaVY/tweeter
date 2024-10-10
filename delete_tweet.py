import tweepy

# Set up Twitter API credentials
consumer_key = '6mXkLnNjtRzjgf8GMuF9I4sA2'  # API Key
consumer_secret = 'oTnp7jjr4DddF5uzGdmxtgbKgjnyoRHse5kspRLxC76F1s2QWl'  # API Key Secret
access_token = '1844361782988566529-ohjorxrUwjKMnhVo7VFKAk2qt68HUr'  # Access Token
access_token_secret = 'IUvdztod9YITr8U870PUIn7gbp5RlIrGzB3iKWjTOrihE'  # Access Token Secret

# Authenticate to Twitter using OAuth1
authentication = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

# Create the  API object
api = tweepy.API(authentication)

# Function to delete a tweet
def deletingMytweets():
    while True:
        try:
            # Fetching user input to get the Tweet ID
            tweets_id = input("Enter the Tweet ID you want to delete (or type 'exit' to exit): ")

            # To Exit from  program
            if tweets_id.lower() == 'exit':
                print("Exiting the program.")
                break

            # Checks empty Tweet ID
            if not tweets_id.strip():
                print("Empty Tweet ID is not Accepted, Provide Tweet ID to continue.")
                continue

            # Deleting the tweet
            api.destroy_status(tweets_id)
            print(f"Tweet with ID {tweets_id}  is deleted !")

        except tweepy.NotFound:
            print(f"Tweet with ID {tweets_id} is not found. Please check your Tweet ID once again.")
        except tweepy.Forbidden as e:
            print(f" You don't have permission to delete this tweet. {e}")
        except tweepy.TooManyRequests:
            print("You have exceeded Rate Limit. Try again after some time.")
        except tweepy.TweepyException as e:
            # Handles all other errors during the deletion 
            print(f"Failed to delete tweet: {e}")
        except Exception as e:
            # Catch  all other exceptions
            print(f"An unexpected error occurred: {e}")

# Run the tweet deletion function
if __name__ == "__main__":
    deletingMytweets()
