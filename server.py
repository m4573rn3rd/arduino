from flask import Flask, render_template, jsonify
import pymongo
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/temperature"
mongo = PyMongo(app)

client = pymongo.MongoClient('localhost',27017)
db = client['mydb']

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/data")
def data():
    line1 = db.trolley1
    line2 = db.trolley2

    #results1 = line1.find()
    #results2 = line2.find()
    results1 = line1.find_one()
    results2 = line2.find_one()
    return jsonify({'results': results1["temperature"]}), jsonify({'results': results2["temperature"]})

if __name__=='__main__':
    app.debug = True
    app.run(port=5000)