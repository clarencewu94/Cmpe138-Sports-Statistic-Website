from flask import Flask, render_template, flash, url_for, session, request, abort
import sqlite3
from bball import Basketball


app = Flask(__name__)

# @ is a decorator which is a way to wrap a function and modifying its behavior
@app.route("/")
def main():
        return render_template("frontpage.html")


@app.route("/mainmenu")
def mainmenu():
    return render_template("mainmenu.html")

@app.route("/signup")
def signup():
    return render_template("signin.html")

@app.route("/session")
def sessionhub():
    return render_template("SessionHub.html")

@app.route('/basketball', methods=['GET', 'POST'])
def basketball():
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

    db = sqlite3.connect('sports.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM basketball')
    if request.method == "POST":
        basketball_db = sqlite3.connect('sports.db')
        add_cursor = basketball_db.cursor()
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
      
        add_cursor.execute('''INSERT INTO basketball(  
            field_goals, three_pointers, free_throws, rebounds, assists, steals, blocks, turnovers, personal_fouls)
            Values(?,?,?,?,?,?,?,?,?)''', (  #Basketball
            Field_Goal, Three_Point, Free_Throws, Rebounds, Assists, Steals, Blocks, Turnovers,Personal_Fouls ))
        basketball_db.commit()
        db.close()
        success = "Successfully added to database"
        return render_template('basketball.html', success=success)
    return render_template('basketball.html')
       
@app.route("/football")
def football():
    return render_template("football.html")

@app.route("/footballoffense", methods=['GET', 'POST'])
def footballoffense():
    Completions = ""
    Yards = ""
    Touchdown = ""
    Interception = ""
    Field_Goal = ""
    Extra_Points = ""

    db = sqlite3.connect('sports.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM foffense')
    if request.method == "POST":
        footballoffense_db = sqlite3.connect('sports.db')
        add_cursor = footballoffense_db.cursor()
        #FootballOffense
        Completions = request.form['Completions']
        Yards = request.form['Yards']
        Touchdown = request.form['Touchdown']
        Interception = request.form['Interception'] 
        Field_Goal = request.form['Field_Goal']
        Extra_Points = request.form['Extra_Points']
        
        add_cursor.execute('''INSERT INTO foffense(  
            completions, yards, touchdown, interception, field_goals, extra_points)
                Values(?,?,?,?,?,?)''', (  
            Completions, Yards, Touchdown, Interception, Field_Goal, Extra_Points ))
        footballoffense_db.commit()
        success = "Successfully added to database"
        return render_template('footballoffense.html', success=success)
    return render_template("footballoffense.html")

@app.route("/footballdefense")
def footballdefense():
    Tackles = ""
    Fumbles = ""
    Sacks = ""
    Interception = ""

    db = sqlite3.connect('sports.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM fdefense')
    if request.method == "POST":
        footballdefense_db = sqlite3.connect('sports.db')
        add_cursor = footballdefense_db.cursor()
        #Footballdefense
        Tackles = request.form['Tackles']
        Fumbles = request.form['Fumbles']
        Sacks = request.form['Sacks']
        Interception = request.form['Interception'] 
        
        add_cursor.execute('''INSERT INTO fdefense(  
            tackles, fumbles, sacks, interception)
                Values(?,?,?,?)''', (  
            Tackies, Fumbles, Sacks, Interception ))
        footballdefense_db.commit()
        success = "Successfully added to database"
        return render_template('footballdefense.html', success=success)
    return render_template("footballdefense.html")

@app.route("/soccer", methods=['GET', 'POST'])
def soccer():
    #Soccer
    Shots = ""
    Saves = ""
    Offside = ""
    Fouls = ""
    Assists = "" 
    Yellow_Cards = ""
    Red_Cards = ""
    
    db = sqlite3.connect('sports.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM soccer')
    if request.method == "POST":
        soccer_db = sqlite3.connect('sports.db')
        add_cursor = soccer_db.cursor()
        #Soccer
        Shots = request.form['Shots']
        Saves = request.form['Saves']
        Offside = request.form['Offside']
        Fouls = request.form['Fouls']
        Yellow_Cards = request.form['Yellow_Cards']
        Red_Cards = request.form['Red_Cards']
      
        add_cursor.execute('''INSERT INTO soccer(  
            shots, saves, offside, fouls, assists, yellow_cards, red_cards)
            Values(?,?,?,?,?,?,?)''', (  
            Shots, Saves, Offside, Fouls, Assists, Yellow_Cards, Red_Cards ))
        soccer_db.commit()
        success = "Successfully added to database"
        return render_template('soccer.html', success=success)
    return render_template('soccer.html')

@app.route("/tennis")
def tennis():
     #tennis
    winners = ""
    double_faults = ""
    aces = ""
    serves = ""
    net_faults = "" 
    
    db = sqlite3.connect('sports.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM tennis')
    if request.method == "POST":
        tennis_db = sqlite3.connect('sports.db')
        add_cursor = tennis_db.cursor()
        #tennis
        winners = request.form['winners']
        double_faults = request.form['double_faults']
        aces = request.form['aces']
        serves = request.form['serves']
        net_faults = request.form['net_faults']
      
        add_cursor.execute('''INSERT INTO tennis(  
            winners, double_faults, aces, serves, net_faults)
            Values(?,?,?,?,?)''', (  
           winners, double_faults, aces, serves, net_faults ))
        tennis_db.commit()
        success = "Successfully added to database"
        return render_template('tennis.html', success=success)
    return render_template('tennis.html')

@app.route("/golf")
def golf():
    #golf
    course_name = ""
    first = ""
    second = ""
    third = ""
    fourth = "" 
    fifth = "" 
    seventh = ""
    eighth = ""
    ninth = ""
    tenth = ""
    eleventh = "" 
    twelfth = "" 
    thirteenth = ""
    fourtheenth = ""
    fifteenth = ""
    sixteenth = ""
    seventeenth = ""
    eighteenth = ""
    
    db = sqlite3.connect('sports.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM golf')
    if request.method == "POST":
        golf_db = sqlite3.connect('sports.db')
        add_cursor = golf_db.cursor()
        #golf
        course_name = request.form['course_name']
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']
        fourth = request.form['fourth']
        fifth = request.form['fifth']
        sixth = request.form['sixth']
        seventh = request.form['seventh']
        eighth = request.form['eighth']
        ninth = request.form['ninth']
        tenth = request.form['tenth']
        eleventh = request.form['eleventh']
        twelfth = request.form['twelfth']
        thirteenth = request.form['thirteenth']
        fourtheenth = request.form['fourtheenth']
        fifteenth = request.form['fifteenth']
        sixteenth = request.form['sixteenth']
        seventeenth = request.form['seventeenth']
        eighteenth = request.form['eighteenth']
      
        add_cursor.execute('''INSERT INTO golf(  
            course_name, first, second, third, fourth. fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourtheenth, fifteenth, sixteenth, seventeenth, eighteenth)
            Values(?,?,?,?,?)''', (  
            course_name, first, second, third, fourth. fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourtheenth, fifteenth, sixteenth, seventeenth, eighteenth))

        golf_db.commit()
        success = "Successfully added to database"
        return render_template('golf.html', success=success)
    return render_template('golf.html')


@app.route("/hockey")
def hockey():
    #hockey
    goals = ""
    defence_blocked_shots  = ""
    off_target_shots = ""
    goals_stopped = ""
    
    db = sqlite3.connect('sports.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM hockey')
    if request.method == "POST":
        hockey_db = sqlite3.connect('sports.db')
        add_cursor = hockey_db.cursor()
        #hockey
        goals = request.form['goals']
        defence_blocked_shots = request.form['defence_blocked_shots']
        off_target_shots = request.form['off_target_shots']
        goals_stopped = request.form['goals_stopped']

        add_cursor.execute('''INSERT INTO hockey(  
            goals, defence_blocked_shots, off_target_shots, goals_stopped)
            Values(?,?,?,?)''', (  
            goals, defence_blocked_shots, off_target_shots, goals_stopped))
        hockey_db.commit()
        success = "Successfully added to database"
        return render_template('hockey.html', success=success)
    return render_template('hockey.html')

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
	app.run(debug=True)
