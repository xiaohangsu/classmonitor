# -*- coding: utf-8 -*-

from flask import Flask, session, escape
from flask import request, url_for, render_template, jsonify
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
        formJson = request.get_json()
        returnJson = userdb.login({ 'loginID': escape(formJson["loginID"]),
                                                   'password': escape(formJson['password']) })
        if returnJson.has_key("uuid"):
            session["user"] = userdb.get({"uuid": returnJson["uuid"]})
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
        returnJson = userdb.update({  'password': escape(formJson['password']), \
                                                        'name': escape(formJson["name"]), \
                                                        'subscribe': escape(formJson["subscribe"]), \
                                                        'email': escape(formJson["email"])})
        return jsonify(returnJson)

@app.route("/apiTemp/get", methods=["POST"])
def apiTemp_get():
    if request.method == "POST":
        formJson = request.get_json()
        returnJson = userdb.get({  'uuid': formJson["uuid"]})
        return jsonify(returnJson)

@app.route("/apiTemp/<param>")
def apiTemp_default(param):
    return  "%s" % param

app.secret_key = '我有一头小毛驴我从来也不骑啊~'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

