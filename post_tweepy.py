import tweepy

# Twitter API credentials
consumer_key = '6mXkLnNjtRzjgf8GMuF9I4sA2'  # API Key
consumer_secret = 'oTnp7jjr4DddF5uzGdmxtgbKgjnyoRHse5kspRLxC76F1s2QWl'  # API Key Secret
access_token = '1844361782988566529-ohjorxrUwjKMnhVo7VFKAk2qt68HUr'  # Access Token
access_token_secret = 'IUvdztod9YITr8U870PUIn7gbp5RlIrGzB3iKWjTOrihE'  # Access Token Secret
bearer_token = "AAAAAAAAAAAAAAAAAAAAAJJWwQEAAAAASt4q3RBhorzip%2FP1MW3r7CCG2O0%3DfWrACcegytQqG6b0FoAAYO9sDhlUejzRrqZIdUrGMKsFNy5khV"  # Bearer Token

# Create a Tweepy client
clients = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Function to create and post a tweet
def postingMytweet():
    while True:
        try:
            # Get the tweet you want to display
            Mytweet = input("Enter your tweet (or type 'exit' to quit): ")

            # Condition for Exit
            if Mytweet.lower() == 'exit':
                print("Exited.")
                break

            # Checks if empty tweet is being posted
            if not Mytweet.strip():
                print(" Please try again. Add your tweet this time")
                continue

            # Posts the exact tweet we are trying to display
            response = clients.create_tweet(text=Mytweet)
            print("  Posted successfully!")

            # To display the tweet ID
            print(f"Tweet ID: {response.data['id']}")
        
        except tweepy.TweepyException as e:
            # Handles all errors during the tweet process
            print(f"Error occurred: {e}")
        except Exception as e:
            # Catches all other exceptions
            print(f"An unexpected error occurred: {e}")

# Run the tweet posting function
if __name__ == "__main__":
    postingMytweet()
