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
        #Basketball
        Field_Goal = request.form['Field_Goal']
        Three_Point = request.form['Three_Point']
        Free_Throws = request.form['Free_Throws']
        Rebounds = request.form['Rebounds']
        Assists = request.form['Assists']
        Steals = request.form['Steals']
        Blocks = request.form['Blocks']
        Turnovers = request.form['Turnovers']
        Personal_Fouls = request.form['Personal_Fouls']
        #Football
        Completion = request.form['Completion']
        Yards = request.form['Yards']
        Yards_Per_Attempt = request.form['Yards_Per_Attempt']
        Touchdown = request.form['Touchdown']
        Interception = request.form['Interception']
        #Tennis
        Aces = request.form['Aces']
        DoubleFaults = request.form['DoubleFaults']
        1st_serve_in = request.form['1st_serve_in']
        1st_serve_inWon = request.form['1st_serve_inWon']
        2nd_serve_Points = request.form['2nd_serve_Points']
        Wins = request.form['Wins']
        UnforcedErrors = request.form['UnforcedErrors']
        NetPointsWon = request.form['NetPointsWon']
        BreakPointsWon = request.form['BreakPointsWon']
        #Soccer
        Shots = request.form['Shots']
        Assists = request.form['Assists']
        Goals = request.form['Goals']
        Save = request.form['Save']
        Fowls = request.form['Fowls']
        YellowCards = request.form['YellowCards']
        RedCards = request.form['RedCards']
        #Hockey
        Shots_Attempted = request.form['Shots_Attempted']
        BlockedbyDefence = request.form['BlockedbyDefence']
        Shots_Off = request.form['Shots_Off']
        Pipes = request.form['Pipes']
        Shots_made = request.form['Shots_made']
        Goals_Saved = request.form['Goals_Saved']
        #For Stats
        db_cursor.execute('''INSERT INTO Stats(  
            #Basketball
            Field_Goal, Three_Point, Free_Throws, Rebounds, Assists, Steals, Blocks, Turnovers,Personal_Fouls,
            #Football
            Completion, Yards, Yards_Per_Attempt, Touchdown,Interception
            #Tennis
            Aces,DoubleFaults, 1st_serve_in, 1st_serve_inWon, 2nd_serve_Points, Wins,UnforcedErrors,NetPointsWon,BreakPointsWon 
            #Soccer
            Shots, Assists,Goals,Save,Fowls,YellowCards,RedCards 
            #Hockey
            Shots_Attempted,BlockedbyDefence, Shots_Off, Pipes,Shots_made,Goals_Saved) 
                Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (  #Basketball
            Field_Goal, Three_Point, Free_Throws, Rebounds, Assists, Steals, Blocks, Turnovers,Personal_Fouls,
            #Football
            Completion, Yards, Yards_Per_Attempt, Touchdown,Interception
            #Tennis
            Aces,DoubleFaults, 1st_serve_in, 1st_serve_inWon, 2nd_serve_Points, Wins,UnforcedErrors,NetPointsWon,BreakPointsWon 
            #Soccer
            Shots, Assists,Goals,Save,Fowls,YellowCards,RedCards 
            #Hockey
            Shots_Attempted,BlockedbyDefence, Shots_Off, Pipes,Shots_made,Goals_Saved))
            add_db.commit()
            success = "Successfully added to database"
               return render_template('SessionHub/SessionHub.html', success=success)
    return render_template('SessionHub/SessionHub.html')

       

