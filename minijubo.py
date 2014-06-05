from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from flask.helpers import url_for
from userhash import check_password, hash_password 
import os

""" Database """ 
from sqlalchemy import Column, Integer, String, Table
from models import Jubo, User
from models import db_session

""" Flask App"""
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/jubo')
def jubo():
    jubo_am = db_session.query(Jubo).first() 
    return render_template('jubo.html', jubo_am = jubo_am)
    
@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/admin')
def admin():
    if session['username'] == 'admin':
        return "Admin Mode"
        """render_template('admin.html')"""
    return redirect(url_for('admin_login'))

@app.route('/admin_login', methods=['GET', 'POST'])

def admin_login():
    if request.method == 'POST':
        id = request.form['username']
        pw = request.form['password']
    
        db_session.rollback()
        check_user = db_session.query(User).filter(User.id == id).first()
        
        if check_password(check_user.password, pw):
            session['username'] = id
            return redirect(url_for('admin'))
            
    else:
        return "Admin Login Page"
        """return render_template('admin_login.html')"""

@app.route('/admin_test')
def admin_test():
    db_session.rollback()
    create_user = User(id='admin', password=hash_password('password')) 
    db_session.add(create_user)
    db_session.commit()
    
if __name__ == "__main__":
    app.run(port=80, debug=True)
    """app.run(host="0.0.0.0", port=80, debug=True)"""