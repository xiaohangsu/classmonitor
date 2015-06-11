# -*- coding: utf-8 -*-

from flask import Flask, session, escape
from flask import request, url_for, render_template
from db import userdb
import json
app = Flask(__name__)

@app.route("/")
def main_page():
  return render_template('index.html')

@app.route("/api/<param>")
def api_default(param):
    return  "%s" % param

@app.route("/apiTemp/login", methods=["POST"])
def apiTemp_login():
    if request.method == "POST":
        returnJson = userdb.login({ 'loginID': escape(request.form["loginID"]),
                                                   'password': escape(request.form['password']) })
        if returnJson.has_key("uuid"):
            session["user"] = userdb.get({"uuid": returnJson["uuid"]})
        return json.dumps(returnJson)

@app.route("/apiTemp/signup", methods=["POST"])
def apiTemp_signup():
    if request.method == "POST":
        returnJson = userdb.register({  'loginID': escape(request.form["loginID"]), \
                                                        'password': escape(request.form['password']), \
                                                        'name': escape(request.form["name"]) if request.form.has_key("name") else "", \
                                                        'subscribe': escape(request.form["subscribe"]) if request.form.has_key("subscribe") else [], \
                                                        'email': escape(request.form["email"] if request.form.has_key("email") else "")})
        return json.dumps(returnJson)

@app.route("/apiTemp/update", methods=["POST"])
def apiTemp_update():
    if request.method == "POST":
        returnJson = userdb.update({  'password': escape(request.form['password']), \
                                                        'name': escape(request.form["name"]), \
                                                        'subscribe': escape(request.form["subscribe"]), \
                                                        'email': escape(request.form["email"])})
        return json.dumps(returnJson)

@app.route("/apiTemp/get", methods=["POST"])
def apiTemp_get():
    if request.method == "POST":
        returnJson = userdb.get({  'uuid': request.form["uuid"]})
        return json.dumps(returnJson)

@app.route("/apiTemp/<param>")
def apiTemp_default(param):
    return  "%s" % param

app.secret_key = '我有一头小毛驴我从来也不骑啊~'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

