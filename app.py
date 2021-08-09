import numpy as np
from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict",methods=['POST'])
def predict():
    # for rendering results on HTML GUI
    if request.method=="POST":
        data1=request.form["danceability"]
        data2=request.form["energy"]
        data3=request.form["loudness"]
        data4=request.form["speechiness"]
        data5=request.form["acoustiness"]
        data6=request.form["instrumentalness"]
        data7=request.form["liveness"]
        data8=request.form["valence"]
        data9=request.form["tempo"]
        data10=request.form["genre"]


    arr=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
    pred=model.predict([arr])
    return render_template("predict.html",data=pred)

if __name__== "__main__":
    app.run(debug=True)

