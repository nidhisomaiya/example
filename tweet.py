import os
import tweepy
from flask import Flask, render_template, request


app = Flask("Twitter")
port = int(os.environ.get("PORT", 5000))

with open("credentials.txt", "r") as file:
    consumer_key = file.readline().split()[2]
    consumer_secret = file.readline().split()[2]
    access_token = file.readline().split()[2]
    access_token_secret = file.readline().split()[2]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/timeline", methods = ["GET"])
def timeline():
    tweets_from_timeline = api.home_timeline()
    return render_template("main.html", tweets_from_timeline=tweets_from_timeline)

@app.route("/tweet", methods = ["POST"])
def tweet():
    text = request.form["Tweet"]
    post_tweet = api.update_status(text)
    response = "Your tweet was sent successfully: {}".format(text)
    return render_template("main.html", response = response)


app.run(host = '0.0.0.0', port=port, debug=True)
