from flask import Flask, render_template, request, url_for
import pickle
import numpy as np


app = Flask(__name__)

model = pickle.load(open('IPLModel.pkl', 'rb'))
@app.route('/')
def hello_world1():
    return render_template("index.html")

@app.route('/home')
def hello_world2():
    return render_template("index.html")

@app.route('/gallery')
def photos():
    return render_template("gallery.html")

@app.route('/prediction')
def predict():
    return render_template("pred.html")

@app.route('/predicted',methods=['POST','GET'])
def predict2():
    batting_team = request.form['batting_team']
    print(batting_team)
    bowling_team = request.form['bowling_team']
    runs = int(request.form['runs'])
    overs = float(request.form['overs'])
    wickets = int(request.form['wickets'])
    runs_last_5 = int(request.form['runs_last_5'])
    wickets_last_5 = int(request.form['wickets_last_5'])

    prediction_array = []
    #batting team
    if batting_team == 'Chennai Super Kings':
        prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
    elif batting_team == 'Delhi Capitals':
        prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
    elif batting_team == 'Punjab Kings':
        prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
    elif batting_team == 'Kolkata Knight Riders':
        prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
    elif batting_team == 'Mumbai Indians':
        prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
    elif batting_team == 'Rajasthan Royals':
        prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
    elif batting_team == 'Royal Challengers Bangalore':
        prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
    elif batting_team == 'Sunrisers Hyderabad':
        prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
    # Bowling Team
    if bowling_team == 'Chennai Super Kings':
        prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
    elif bowling_team == 'Delhi Capitals':
        prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
    elif bowling_team == 'Punjab Kings':
        prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
    elif bowling_team == 'Kolkata Knight Riders':
        prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
    elif bowling_team == 'Mumbai Indians':
        prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
    elif bowling_team == 'Rajasthan Royals':
        prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
    elif bowling_team == 'Royal Challengers Bangalore':
        prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
    elif bowling_team == 'Sunrisers Hyderabad':
        prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
    prediction_array = prediction_array + [runs, wickets, overs, runs_last_5, wickets_last_5]
    prediction_array = np.array([prediction_array])
    prediction = model.predict(prediction_array)
    return render_template("pred.html", pred=int(prediction))




if __name__ == '__main__':
    app.run(debug=True)
