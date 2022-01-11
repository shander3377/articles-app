from flask import Flask, request, jsonify
import csv


all_articles = []
with open("articles.csv") as f:
 reader = csv.reader(f)
 data = list(reader)
 all_articles = data[1:]

 liked_Articles = []
 disliked_Articles = []

 @app.route("/getArticle")
def getArticle():
    return jsonify({"data": all_articles[0], "status": "success"}) 

@app.route('/likedArticles', methods = ["POST"])
def likedMovies():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_Articles.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route('/dislikedArticles', methods = ["POST"])
def likedMovies():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_Articles.append(movie)
    return jsonify({
        "status": "success"
    }), 201


