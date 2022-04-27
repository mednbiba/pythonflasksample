from flask import Blueprint, render_template
from . import db
import socket

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html',test="--------"+socket.gethostname()+"---------"+"</br>")

@main.route('/profile')
def profile():
    return render_template('profile.html',tba="--------"+socket.gethostname()+"---------"+"</br>")