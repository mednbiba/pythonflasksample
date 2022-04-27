from flask import Blueprint, render_template,redirect, url_for,request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from project.azquery import user_exists
from .models import User
from . import db

import sys
import os
sys.path.insert(0, os.getcwd()+"/project")
import azquery








auth = Blueprint('auth', __name__)






####################LOGIN MODULE###################

@auth.route('/login')
def login():
    return render_template('login.html')
@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    print("a")
    if azquery.user_exists(email,password)==0:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    else:
        return redirect(url_for('main.profile'))



####################SIGNUP MODULE###################
@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password="generate_password_hash(password, method='sha256')")

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return 'Logout'


import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect(r"DRIVER={SQL Server};SERVER=nbiba.database.windows.net;DATABASE=myDB1;UID=azuresql;PWD=aezakmi1996X-")


# Create a cursor from the connection
cursor = cnxn.cursor()
def user_exists(a,b):
    x=0
    cursor.execute("select * from users where email = ? AND password = ?",[a,b])
    row = cursor.fetchone()
    if row:
        x=1
    return x
     
def user_create(a,b,c,d):
    x=0
    with cnxn.cursor() as cursor:
        cursor.execute("INSERT INTO dbo.users([id], [email], [password], [name]) VALUES(?,?,?,?)",[a,b,c,d])
        x=1
    return x




        



