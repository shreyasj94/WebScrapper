import requests
from bs4 import BeautifulSoup
import smtplib
import pandas as pd


df = pd.read_csv (r'tiktok_influencer_usernames.csv')
print (df)

# Export username into URL

def info():

    URL = 'https://www.tiktok.com/@stacyclips?'
    headers = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    page=requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    likes = soup.find(title="Likes").get_text()
    followers = soup.find(title="Followers").get_text()
    following = soup.find(title="Following").get_text()


    print (likes.strip())
    print(followers.strip())
    print(following.strip())

# Export Results into csv

info()





