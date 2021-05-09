#imports
from deploy import *
from flask import Flask, render_template, redirect, url_for, send_from_directory

#disclaimers
print("\n FOR WINDOWS USERS IGNORE FCTNL \n" )

#variables
app = Flask(__name__)
route = app.route
run = app.run

#syntax samples 
#@route("/")
#route()
#run()
#instructions()
#homepage()
#deploy

#provides instructions
def instructions():
    print("Hello welcome to easy flask, a really crappy library I made, type \n ---- \n homepage() \n run() \n ----- to get started, @app.route() is now @route(), deploy, deploys the app (Requires configuration).")

#sets up a basic homepage 
def homepage():
    @app.route("/", methods = ["POST", "GET"])
    def index():
        return render_template("index.html")
    