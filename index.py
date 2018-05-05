from flask import Flask, jsonify
from flask import render_template, redirect, request, url_for
from pymongo import MongoClient
import requests

app = Flask(__name__)

mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']


@app.route('/')
def index():
    return render_template('bootstraptemplate.html')


@app.route('/userlogin', methods=['POST', 'GET'])
def userlogin():
    users = db.users.find()

    list_of_users = []
    for i in users:
        list_of_users.append(i)

    if request.method == 'POST':
        for i in list_of_users:
            if i['email'] == request.form['email']:
                if i['password'] == request.form['psw']:
                    return redirect(url_for('success'))
                else:
                    return redirect(url_for('index'))
            else:
                return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/userregistration', methods=['POST', 'GET'])
def userregistration():
    if request.method == 'POST':
        email_id = request.form['email']
        password = request.form['psw']
        post = {'email': email_id, 'password': password}
        db.users.insert(post)
        return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('newfeeds.html')


@app.route("/trial")
def trial():
    a = db.data.find_one({"id": 0})
    return str(a['a'])


@app.route("/category/<cat>")
def category(cat):
    r = requests.get("https://newsapi.org/v2/everything?q=" + cat + "&sortBy=publishedAt&apiKey=e8704cf44921496593e63fc898537993")
    item = {"articles": r.json()['articles']}
    return jsonify({"data": item})


if __name__ == '__main__':
    app.run(debug=True)
