from library import app
#from library import db
from flask import render_template, redirect, flash, url_for, session, request, abort
import sqlite3
from Publication import Publication

app.secret_key = 'you-will-never-guess'

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None;
    #cursor = db.get_db_cursor
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials, Try again'
        else:
            session['logged_in'] = True
            flash('Successfully Logged in!')
            return redirect(url_for('login'))
    return render_template('login/login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Successfully Logged Out!')
    return redirect(url_for('login'))