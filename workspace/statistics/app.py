from flask import Flask, render_template, flash, url_for, session, request, abort
import sqlite3
from bball import Basketball


app = Flask(__name__)


db = sqlite3.connect('sports.db', check_same_thread=False)
cursor = db.cursor()

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

    cursor.execute('SELECT * FROM basketball')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        basketball_db = sqlite3.connect('sports.db',check_same_thread=False)
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
        basketball_db.close()
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

 
    cursor.execute('SELECT * FROM foffense')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        footballoffense_db = sqlite3.connect('sports.db',check_same_thread=False)
        add_cursor = footballoffense_db.cursor()
        #FootballOffense
        Completions = request.form['Completions']
        Yards = request.form['Yards']
        Touchdown = request.form['Touchdown']
        Interception = request.form['Interception'] 
        Field_Goal = request.form['Field_Goal']
        Extra_Points = request.form['Extra_Points']
        
        add_cursor.execute('''INSERT INTO foffense(  
            completions, yards, touchdowns, interceptions, field_goals, extra_points)
                Values(?,?,?,?,?,?)''', (  
            Completions, Yards, Touchdown, Interception, Field_Goal, Extra_Points ))
        footballoffense_db.commit()
        footballoffense_db.close()
        success = "Successfully added to database"
        return render_template('footballoffense.html', success=success)
    return render_template("footballoffense.html")

@app.route("/footballdefense", methods=['GET', 'POST'])
def footballdefense():
    Tackles = ""
    Fumbles = ""
    Sacks = ""
    Interception = ""

   
    cursor.execute('SELECT * FROM fdefense')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        footballdefense_db = sqlite3.connect('sports.db',check_same_thread=False)
        add_cursor = footballdefense_db.cursor()
        #Footballdefense
        Tackles = request.form['Tackles']
        Fumbles = request.form['Fumbles']
        Sacks = request.form['Sacks']
        Interception = request.form['Interceptions'] 
        
        add_cursor.execute('''INSERT INTO fdefense(  
            tackles, fumbles, sacks, interceptions)
                Values(?,?,?,?)''', (  
            Tackles, Fumbles, Sacks, Interception ))
        footballdefense_db.commit()
        footballdefense_db.close()
        
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
    
   
    cursor.execute('SELECT * FROM soccer')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        soccer_db = sqlite3.connect('sports.db',check_same_thread=False)
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
        soccer_db.close()
        success = "Successfully added to database"
        return render_template('soccer.html', success=success)
    return render_template('soccer.html')

@app.route("/tennis", methods=['GET', 'POST'])
def tennis():
     #tennis
    winners = ""
    double_faults = ""
    aces = ""
    serves = ""
    net_faults = "" 
    
  
    cursor.execute('SELECT * FROM tennis')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        tennis_db = sqlite3.connect('sports.db',check_same_thread=False)
        add_cursor = tennis_db.cursor()
        #tennis
        winners = request.form['Winners']
        double_faults = request.form['Double_Faults']
        aces = request.form['Aces']
        serves = request.form['Serves']
        net_faults = request.form['Net_Faults']
      
        add_cursor.execute('''INSERT INTO tennis(  
            winners, double_faults, aces, serves, net_faults)
            Values(?,?,?,?,?)''', (  
           winners, double_faults, aces, serves, net_faults ))
        tennis_db.commit()
        tennis_db.close()
        success = "Successfully added to database"
        return render_template('tennis.html', success=success)
    return render_template('tennis.html')

@app.route("/golf", methods=['GET', 'POST'])
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
    fourteenth = ""
    fifteenth = ""
    sixteenth = ""
    seventeenth = ""
    eighteenth = ""
    
   
    cursor.execute('SELECT * FROM golf')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        golf_db = sqlite3.connect('sports.db',check_same_thread=False)
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
        fourteenth = request.form['fourteenth']
        fifteenth = request.form['fifteenth']
        sixteenth = request.form['sixteenth']
        seventeenth = request.form['seventeenth']
        eighteenth = request.form['eighteenth']
      
        add_cursor.execute('''INSERT INTO golf(  
            course_name, first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, eighteenth)
            Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (  
            course_name, first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, eighteenth))

        golf_db.commit()
        golf_db.close()
        success = "Successfully added to database"
        return render_template('golf.html', success=success)
    return render_template('golf.html')


@app.route("/hockey", methods=['GET', 'POST'])
def hockey():
    #hockey
    Goals = ""
    Defence_Blocked_Shots  = ""
    Off_Target_Shots = ""
    Goals_Stopped = ""
    
    cursor.execute('SELECT * FROM hockey')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        hockey_db = sqlite3.connect('sports.db',check_same_thread=False)
        add_cursor = hockey_db.cursor()
        #hockey
        Goals = request.form['Goals']
        Defence_Blocked_Shots = request.form['Defence_Blocked_Shots']
        Off_Target_Shots = request.form['Off_Target_Shots']
        Goals_Stopped = request.form['Goals_Stopped']

        add_cursor.execute('''INSERT INTO hockey(  
            goals, defence_blocked_shots, off_target_shots, goals_stopped)
            Values(?,?,?,?)''', (  
            Goals, Defence_Blocked_Shots, Off_Target_Shots, Goals_Stopped))
        hockey_db.commit()
        hockey_db.close()
        success = "Successfully added to database"
        return render_template('hockey.html', success=success)
    return render_template('hockey.html')

@app.route("/resulthub")
def resulthub():
    return render_template("ResultHub.html")
    
@app.route("/bballresults/<int:game>", methods=['GET', 'POST'])
def bballresults(game):
    FG = ""
    TPT = ""
    FT = ""
    REB = ""
    AST = ""
    STL = ""
    BLK = ""
    TO = ""
    PF = ""
    basketball_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from basketball")
        search_game_list = cursor.fetchall()
        for row in search_game_list:
            FG = row[0]
            TPT = row[1]
            FT = row[2]
            REB = row[3]
            AST = row[4]
            STL = row[5]
            BLK = row[6]
            TO = row[7]
            PF = row[8]
        basketball = Basketball(FG, TPT, FT, REB, AST, STL, BLK, TO, PF)
        basketball_dict[game] = basketball #storing in Data Structure for printing purposes
        return render_template('bballresults.html', game=game, basketball_dict=basketball_dict)
    return render_template("bballresults.html")

@app.route("/foffenseResults/<int:game>", methods=['GET', 'POST'])
def foffenseResults(game):
    CMP = ""
    YDS = ""
    TD = ""
    INTs = ""
    FG = ""
    XP = ""
    foffense_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from foffense")
        search_game_list = cursor.fetchall()
        for row in search_game_list:
            CMP = row[0]
            YDS = row[1]
            TD = row[2]
            INTs = row[3]
            FG = row[4]
            XP = row[5]
        football = foffense(CMP, YDS, TD, INTs, FG, XP)
        foffense_dict[game] = football #storing in Data Structure for printing purposes
        return render_template('foffenseResults.html', game=game, foffense_dict=foffense_dict)
    return render_template("foffenseResults.html")
    
@app.route("/fdefenseResults/<int:game>", methods=['GET', 'POST'])
def fdefenseResults(game):
    tackles = ""
    fumbles = ""
    sacks = ""
    interception = ""
    fdefense_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from fdefense")
        search_game_list = cursor.fetchall()
        for row in search_game_list:
            tackles = row[0]
            fumbles = row[1]
            sacks = row[2]
            inteception = row[3]
        football = fdefense(tackles, fumbles, sacks, interception)
        fdefense_dict[game] = football #storing in Data Structure for printing purposes
        return render_template('fdefenseResults.html', game=game, fdefense_dict=fdefense_dict)
    return render_template("fdefenseResults.html")
    
@app.route("/soccerResults/<int:game>", methods=['GET', 'POST'])
def soccerResults(game):
    shows = ""
    saves = ""
    offsides = ""
    fouls = ""
    assists = ""
    yellow_cards = ""
    red_cards = ""
    soccer_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from soccer")
        search_game_list = cursor.fetchall()
        for row in search_game_list:
            shows = row[0]
            saves = row[1]
            offsides = row[2]
            fouls = row[3]
            assists = row[4]
            yellow_cards = row[5]
            red_cards = row[6]
            
        soccers = soccer(shows, saves, offsides, fouls, assists, yellow_cards, red_cards)
        soccer_dict[game] = soccers #storing in Data Structure for printing purposes
        return render_template('soccerResults.html', game=game, soccer_dict=soccer_dict)
    return render_template("soccerResults.html")

if __name__ == "__main__":
	app.run(debug=True)
