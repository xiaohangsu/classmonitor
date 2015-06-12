# -*- coding: utf-8 -*-

from flask import Flask, session, escape
from flask import request, url_for, render_template, jsonify, redirect
from db import userdb
import json
from newsCatalog import NEWSCATALOG
app = Flask(__name__)

@app.route("/")
def main_page():
  user = session['user']
  if user is not None:
    return render_template('index.html', path='/', user=session['user'])
  else:
    return redirect('/login')

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
        formJson = request.get_json()
        returnJson = userdb.login({ 'loginID': escape(formJson["loginID"]),
                                                   'password': escape(formJson['password']) })
        if returnJson.has_key("uuid"):
            session["user"] = userdb.get({"uuid": returnJson["uuid"]}).get("user", {})
        return jsonify(returnJson)

@app.route("/apiTemp/signup", methods=["POST"])
def apiTemp_signup():
    if request.method == "POST":
        formJson = request.get_json()
        returnJson = userdb.register({  'loginID': escape(formJson["loginID"]), \
                                                        'password': escape(formJson['password']), \
                                                        'name': escape(formJson["name"]) if formJson.has_key("name") else "", \
                                                        'subscribe': escape(formJson["subscribe"]) if formJson.has_key("subscribe") else [], \
                                                        'email': escape(formJson["email"] if formJson.has_key("email") else "")})
        return jsonify(returnJson)

@app.route("/apiTemp/update", methods=["POST"])
def apiTemp_update():
    if request.method == "POST": 
        formJson = request.get_json()
        returnJson = userdb.update({  'uuid': escape(formJson['uuid']) if formJson.has_key("uuid") else session["user"]["uuid"], \
                                                        'password': escape(formJson['password']) if formJson.has_key("password") else session["user"]["password"], \
                                                        'name': escape(formJson["name"]) if formJson.has_key("name") else session["user"]["name"], \
                                                        'subscribe': escape(formJson["subscribe"]) if formJson.has_key("subscribe") else session["user"]["subscribe"], \
                                                        'email': escape(formJson["email"]) if formJson.has_key("email") else session["user"]["email"] })
        return jsonify(returnJson)

@app.route("/apiTemp/get", methods=["POST"])
def apiTemp_get():
    if request.method == "POST":
        returnJson = userdb.get({  'uuid': session["user"]["uuid"] if session["user"].has_key("uuid") else "" })
        return jsonify(returnJson)

# return newsCatalog
@app.route("/apiTemp/getNewsCatalog", methods=["POST"])
def apiTemp_getNewsCatalog():
    if request.method == "POST":
        return jsonify(NEWSCATALOG)

@app.route("/apiTemp/logout", methods=["POST"])
def apiTemp_logout():
    session["user"] = None

@app.route("/apiTemp/<param>")
def apiTemp_default(param):
    return  "%s" % param

app.secret_key = '我有一头小毛驴我从来也不骑啊~'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

