from library import app
#from library import db
from flask import render_template, redirect, flash, url_for, session, request, abort
import sqlite3
from Publication import Publication

app.secret_key = 'you-will-never-guess'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    error = None;
    #cursor = db.get_db_cursor
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials, Try again'
        else:
            session['logged_in'] = True
            flash('Successfully Logged in!')
            return redirect(url_for('mainmenu'))
    return render_template('frontpage/frontpage.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Successfully Logged Out!')
    return redirect(url_for('login'))
    
@app.route('Session', methods=['GET', 'POST'])
def session():
    if request.method == 'POST'
        return redirect(url_for('SessionHub'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    #Basketball
    Field_Goal = ""
    Three_Point = ""
    Free_Throws = ""
    Rebounds = ""
    Assists = ""
    Steals = ""
    Blocks = ""
    Turnovers =""
    Personal_Fouls = ""
    #Football
    Completion =" "
    Yards = ""
    Yards_Per_Attempt = ""
    Touchdown = ""
    Interception = ""
    #Tennis
    Aces = ""
    DoubleFaults = ""
    1st_serve_in = ""
    1st_serve_inWon= ""
    2nd_serve_Points = ""
    Wins = ""
    UnforcedErrors = ""
    NetPointsWon = ""
    BreakPointsWon = ""
    #Soccer
    Shots = ""
    Assists = ""
    Goals = ""
    Saves = ""
    Fowls = "" 
    YellowCards = ""
    RedCards = ""
    #Hockey
    Shots_Attempted = ""
    BlockedbyDefence = ""
    Shots_Off = ""
    Pipes = "" 
    Shots_made = ""
    Goals_Saved = ""

    db = sqlite.connect('Stats.db')
     cursor = db.cursor()
    cursor.execute('SELECT * FROM Stats ORDER BY Stat_name DESC LIMIT 1')
    if request.method == "POST"
        add_db = sqlite3.connect('Stats.db')
        add_cursor = add.db.cursor()
        
    if request.method == "POST":
        #insert form information to Books Table and Author Table
        add_db = sqlite3.connect('database.db')
        add_cursor = add_db.cursor()
        year = request.form['year']
        title = request.form['title']
        book_title = request.form['book_title']
        pages = request.form['pages']
        author_name = request.form['author_name']
        add_cursor.execute('''INSERT INTO Books(datestamp, Book_Title, Title, Pages, Book_ID)
                      VALUES(?,?,?,?,?)''', (year,book_title, title, pages, book_id))
        add_cursor.execute('''INSERT INTO Author(Author_Name, Book_ID)VALUES(?,?)''', 
                    (author_name, book_id))
        add_db.commit()
        success = "Successfully added to database"
        return render_template('book/add.html', success=success)
    return render_template('book/add.html')


