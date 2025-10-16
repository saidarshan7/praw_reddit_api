from dotenv import load_dotenv
import os
load_dotenv()
import praw 

# reddit = praw.Reddit(
client_id =os.getenv('client_id'),
client_secret =os.getenv('client_secret'),
user_agent =os.getenv('user_agent')
                    # )

print(client_id)
print(client_secret)
print(user_agent)