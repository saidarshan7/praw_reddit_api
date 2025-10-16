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


all_reddit = reddit.subreddit('all')
posts =all_reddit.hot(limit=100)

dict = {
    "title":[],
    "subreddit":[],
    "score":[],
    "id":[],
    "created":[],
    "body":[]
}

for submission in posts:
    dict["title"].append(submission.title)
    dict["subreddit"].append(submission.subreddit)
    dict["score"].append(submission.score)
    dict["id"].append(submission.id)
    dict["created"].append(submission.created)
    dict["body"].append(submission.selftext)


def_all = pd.DataFrame(dict)
def_all.head().to_markdown()

# len(def_all['subreddit'].unique)
df.to_csv('golang_subreddit_posts.csv')
def_all.to_csv('all_reddit_posts')







    






    






