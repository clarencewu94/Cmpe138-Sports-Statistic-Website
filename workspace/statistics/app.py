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

    db = sqlite3.connect('Stats.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Basketball')
    if request.method == "POST":
        basketball_db = sqlite3.connect('Stats.db')
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
      
        add_cursor.execute('''INSERT INTO Basketball(  
            #Basketball
            Field_Goal, Three_Point, Free_Throws, Rebounds, Assists, Steals, Blocks, Turnovers,Personal_Fouls,
          
                Values(?,?,?,?,?,?,?,?,?)''', (  #Basketball
            Field_Goal, Three_Point, Free_Throws, Rebounds, Assists, Steals, Blocks, Turnovers,Personal_Fouls ))
        add_db.commit()
        success = "Successfully added to database"
        return render_template('basketball.html', success=success)
    return render_template('basketball.html')


@app.route("/football")
def football():
	return render_template("football.html")

@app.route("/footballoffense")
def footballoffense():
	return render_template("footballoffense.html")

@app.route("/footballdefense")
def footballdefense():
	return render_template("footballdefense.html")

@app.route("/soccer")
def soccer():
	return render_template("soccer.html")

@app.route("/tennis")
def tennis():
	return render_template("tennis.html")

@app.route("/golf")
def golf():
	return render_template("golf.html")

@app.route("/hockey")
def hockey():
	return render_template("hockey.html")

@app.route("/results")
def results():
	return render_template("Results.html")

if __name__ == "__main__":
	app.run(debug=True)
