from index import app, url
from flask import request, render_template
import json

from .login import cklogin


@app.route('/home', methods=['POST', 'GET'])
@cklogin()
def ControlPanel():
    if request.method == 'GET':
        return render_template('home.html', )
