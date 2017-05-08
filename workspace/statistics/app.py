from flask import Flask, render_template, flash, url_for, session, request, abort
import sqlite3
from Basketball import Basketball
from Basketball import Foffense
from Basketball import Fdefense
from Basketball import Golf
from Basketball import Hockey
from Basketball import Soccer
from Basketball import Tennis

app = Flask(__name__)


#from DatabaseManager import DatabaseManager


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

@app.route("/foffense", methods=['GET', 'POST'])
def foffense():
    Completions = ""
    Yards = ""
    Touchdown = ""
    Interception = ""
    Field_Goal = ""
    Extra_Points = ""

    cursor.execute('SELECT * FROM foffense')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        foffense_db = sqlite3.connect('sports.db',check_same_thread=False)
        add_cursor = foffense_db.cursor()
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
        foffense_db.commit()
        foffense_db.close()
        success = "Successfully added to database"
        return render_template('foffense.html', success=success)
    return render_template("foffense.html")

@app.route("/fdefense", methods=['GET', 'POST'])
def fdefense():
    Tackles = ""
    Fumbles = ""
    Sacks = ""
    Interception = ""

   
    cursor.execute('SELECT * FROM fdefense')
    if request.method == "POST":
        cursor.execute("PRAGMA busy_timeout = 10000")

        fdefense_db = sqlite3.connect('sports.db',check_same_thread=False)
        add_cursor = fdefense_db.cursor()
        #Footballdefense
        Tackles = request.form['Tackles']
        Fumbles = request.form['Fumbles']
        Sacks = request.form['Sacks']
        Interception = request.form['Interceptions'] 
        
        add_cursor.execute('''INSERT INTO fdefense(  
            tackles, fumbles, sacks, interceptions)
                Values(?,?,?,?)''', (  
            Tackles, Fumbles, Sacks, Interception ))
        fdefense_db.commit()
        fdefense_db.close()
        
        success = "Successfully added to database"
        return render_template('fdefense.html', success=success)
    return render_template("fdefense.html")

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
        Assists= request.form ['Assists']
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
    sixth = ""
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
    
@app.route("/footballResults")
def FootballResults():
    return render_template("footballResults.html")
    
@app.route("/bballresults/<string:sport>", methods=['GET', 'POST'])
def bballresults(sport="basketball"):
    FG = ""
    TPT = ""
    FT = ""
    REB = ""
    AST = ""
    STL = ""
    BLK = ""
    TO = ""
    PF = ""
    game = 0
    basketball_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from basketball")
        search_game_list = cursor.fetchall()
        print (search_game_list)
        for row in search_game_list:
            #FG = row[0] #user_id = None, why?
            game = row[1] #primary key
            FG = row[2]
            TPT = row[3]
            FT = row[4]
            REB = row[5]
            AST = row[6]
            STL = row[7]
            BLK = row[8]
            TO = row[9]
            PF = row[10]
            basketball = Basketball(FG, TPT, FT, REB, AST, STL, BLK, TO, PF)
            basketball_dict[game] = basketball #storing in Data Structure for printing purposes
        return render_template('bballresults.html', game=game, basketball_dict=basketball_dict)
    return render_template("bballresults.html")

@app.route("/foffenseResults/<string:sport>", methods=['GET', 'POST'])
def foffenseResults(sport="foffense"):
    CMP = ""
    YDS = ""
    TD = ""
    INTs = ""
    FG = ""
    XP = ""
    game =0
    foffense_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from foffense")
        search_game_list = cursor.fetchall()
        print (search_game_list)
        for row in search_game_list:
            game = row[1]
            CMP = row[2]
            YDS = row[3]
            TD = row[4]
            INTs = row[5]
            FG = row[6]
            XP = row[7]
            foffense = Foffense(CMP, YDS, TD, INTs, FG, XP)
            foffense_dict[game] = foffense #storing in Data Structure for printing purposes
        return render_template('foffenseResults.html', game=game, foffense_dict=foffense_dict)
    return render_template("foffenseResults.html")
    
@app.route("/fdefenseResults/<string:sport>", methods=['GET', 'POST'])
def fdefenseResults(sport = "fdefense"):
    tackles = ""
    fumbles = ""
    sacks = ""
    interception = ""
    game =0
    fdefense_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from fdefense")
        search_game_list = cursor.fetchall()
        print (search_game_list)
        for row in search_game_list:
            game = row[1]
            tackles = row[2]
            fumbles = row[3]
            sacks = row[4]
            interception = row[5]
            fdefense = Fdefense(tackles, fumbles, sacks, interception)
            fdefense_dict[game] = fdefense #storing in Data Structure for printing purposes
        return render_template('fdefenseResults.html', game=game, fdefense_dict=fdefense_dict)
    return render_template("fdefenseResults.html")
    
@app.route("/soccerResults/<string:sport>", methods=['GET', 'POST'])
def soccerResults(sport="soccer"):
    shots = ""
    saves = ""
    offsides = ""
    fouls = ""
    assists = ""
    yellow_cards = ""
    red_cards = ""
    game= 0;
    soccer_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from soccer")
        search_game_list = cursor.fetchall()
        print (search_game_list)

        for row in search_game_list:
            game = row[1]
            shots = row[2]
            saves = row[3]
            offsides = row[4]
            fouls = row[5]
            assists = row[6]
            yellow_cards = row[7]
            red_cards = row[8]
            soccer = Soccer(shots, saves, offsides, fouls, assists, yellow_cards, red_cards)
            soccer_dict[game] = soccer #storing in Data Structure for printing purposes
        return render_template('soccerResults.html', game=game, soccer_dict=soccer_dict)
    return render_template("soccerResults.html")

@app.route("/tennisResults/<string:sport>", methods=['GET', 'POST'])
def tennisResults(sport="tennis"):
    winners = ""
    double_faults = ""
    aces = ""
    serves = ""
    net_faults = "" 
    game= 0;
    tennis_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from tennis")
        search_game_list = cursor.fetchall()
        print (search_game_list)
        for row in search_game_list:
            game = row[1]
            winners = row[2]
            double_faults = row[3]
            aces = row[4]
            serves = row[5]
            net_faults = row[6]
            tennis = Tennis(winners, double_faults, aces, serves, net_faults)
            tennis_dict[game] = tennis #storing in Data Structure for printing purposes
        return render_template('tennisResults.html', game=game, tennis_dict=tennis_dict)
    return render_template("tennisResults.html")
    
@app.route("/hockeyResults/<string:sport>", methods=['GET', 'POST'])
def hockeyResults(sport="hockey"):
    goals = ""
    defence_blocked_shots  = ""
    off_target_shots = ""
    goals_stopped = ""
    game= 0;
    hockey_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from hockey")
        search_game_list = cursor.fetchall()
        print (search_game_list)
        for row in search_game_list:
            game = row[1]
            goals = row[2]
            defense_blocked_shots = row[3]
            off_target_shots = row[4]
            hockey = Hockey(goals, defence_blocked_shots, off_target_shots, goals_stopped)
            hockey_dict[game] = hockey #storing in Data Structure for printing purposes
        return render_template('hockeyResults.html', game=game, hockey_dict=hockey_dict)
    return render_template("hockeyResults.html")
    
@app.route("/golfResults/<string:sport>", methods=['GET', 'POST'])
def golfResults(sport="golf"):
    course_name = ""
    first = ""
    second = ""
    third = ""
    fourth = "" 
    fifth = "" 
    sixth = ""
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
    game= 0;
    golf_dict = {}
    search_game_list = []
    if request.method == "GET":
        cursor.execute("select * from golf")
        search_game_list = cursor.fetchall()
        print (search_game_list)
        for row in search_game_list:
            game = row[1]
            course_name = row[2]
            first = row[3]
            second = row[4]
            third = row[5]
            fourth = row[6]
            fifth = row[7]
            sixth = row[8]
            seventh = row[9]
            eighth = row[10]
            ninth = row[11]
            tenth = row[12]
            eleventh = row[13]
            twelfth = row[14]
            thirteenth = row[15]
            fourteenth = row[16]
            fifteenth = row[17]
            sixteenth = row[18]
            seventeenth = row[19]
            eighteenth = row[20]
            golf = Golf(course_name, first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, eighteenth)
            golf_dict[game] = golf #storing in Data Structure for printing purposes
        return render_template('golfResults.html', game=game, golf_dict=golf_dict)
    return render_template("golfResults.html")


if __name__ == "__main__":
	app.run(debug=True)
