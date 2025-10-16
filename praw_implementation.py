from dotenv import load_dotenv
from tabulate import tabulate
import os
load_dotenv()
import praw 
import pandas as pd

reddit = praw.Reddit(
client_id =os.getenv('client_id'),
client_secret =os.getenv('client_secret'),
user_agent =os.getenv('user_agent')
                    )

# print(client_id)
# print(client_secret)
# print(user_agent)



golang_subreddit = reddit.subreddit('Golang')

golang_posts = golang_subreddit.top(limit=10)

for post in golang_posts:
    print(post.title)
    print(post.subreddit)
    print(post.id)
    print(post.url)
    print(post.selftext)



    print("\n")
   
    

dict =  {
    "title":[],
    "subreddit":[],
    "id":[],
    "url":[],
    "comments":[],
    "body":[]
}

for submission in golang_posts:
    dict["title"].append(submission.title)
    dict["subreddit"].append(submission.subreddit)
    dict["id"].append(submission.id)
    dict["url"].append(submission.url)
    dict["body"].append(submission.body)


df = pd.DataFrame(dict)

print(df.head().to_markdown())





    






