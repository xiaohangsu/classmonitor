# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, url_for, render_template
from db import userdb
import json
app = Flask(__name__)

@app.route("/")
def main_page():
  return render_template('index.html', path='/')

@app.route("/login")
def  login():
    return render_template('login.html', path='/login')

@app.route("/register")
def  register():
    return render_template('register.html', path='/register')

@app.route("/api/<param>")
def api_default(param):
    return  "%s" % param

@app.route("/apiTemp/login", methods=["POST"])
def apiTemp_login():
    if request.method == "POST":
        returnJson = userdb.login({ 'loginID': request.form["loginID"],
                                                   'password': request.form['password']})
        return json.dumps(returnJson)

@app.route("/apiTemp/signup", methods=["POST"])
def apiTemp_signup():
    if request.method == "POST":
        print request.form
        returnJson = userdb.register({  'loginID': request.form["loginID"], \
                                                        'password': request.form["password"], \
                                                        'name': request.form["name"], \
                                                        'subscribe': request.form["subscribe"], \
                                                        'email': request.form["email"]})
        return json.dumps(returnJson)

@app.route("/apiTemp/update", methods=["POST"])
def apiTemp_update():
    if request.method == "POST":
        returnJson = userdb.register({  'password': request.form["password"], \
                                                        'name': request.form["name"], \
                                                        'subscribe': request.form["subscribe"], \
                                                        'email': request.form["email"]})
        return json.dumps(returnJson)

@app.route("/apiTemp/get", methods=["POST"])
def apiTemp_get():
    if request.method == "POST":
        returnJson = userdb.register({  'uuid': request.form["uuid"]})
        return json.dumps(returnJson)

@app.route("/apiTemp/<param>")
def apiTemp_default(param):
    return  "%s" % param

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

