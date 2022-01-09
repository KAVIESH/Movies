from flask import Flask, jsonify, request
import csv

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]

likedMovies = []
notLikedMovies = []
didNotWatch = []

app = Flask(__name__)

@app.route('/get-movies')
def getMovies():
    return jsonify({
        "data": allMovies[0],
        "status": "success",
    })

@app.route('/not-liked', methods = ["POST"])
def notLiked():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    notLikedMovies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route('/did-not-watch', methods = ["POST"])
def notLiked():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    didNotWatch.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route('/liked', methods = ["POST"])
def notLiked():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        "status": "success"
    }), 201


if (__name__=='__main__'):
    app.run()
