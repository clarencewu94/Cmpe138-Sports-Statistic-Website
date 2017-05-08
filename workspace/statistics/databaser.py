import sqlite3
conn = sqlite3.connect('sports.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS user''')
c.execute('''CREATE TABLE user
             (userid text not null, password text not null, id integer primary key autoincrement)''')

c.execute('''DROP TABLE IF EXISTS basketball''')
c.execute('''CREATE TABLE basketball
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, field_goals text, three_pointers text, free_throws text, rebounds text, assists text, steals text, blocks text, turnovers text, personal_fouls text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''DROP TABLE IF EXISTS soccer''')
c.execute('''CREATE TABLE soccer
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, shots text, saves text, offside text, fouls text, assists text, yellow_cards text, red_cards text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''DROP TABLE IF EXISTS tennis''')
c.execute('''CREATE TABLE tennis
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, winners text, double_faults text, aces text, serves text, net_faults text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''DROP TABLE IF EXISTS golf''')
c.execute('''CREATE TABLE golf
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, course_name text, first text, second text, third text, fourth text, fifth text, sixth text, seventh text, eighth text, ninth text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''DROP TABLE IF EXISTS hockey''')
c.execute('''CREATE TABLE hockey
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, goals text, defence_blocked_shots text, off_target_shots text, goals_stopped text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''DROP TABLE IF EXISTS foffense''')
c.execute('''CREATE TABLE foffense
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, completions text, yards text, touchdowns text, interceptions text, field_goals text, extra_points text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''DROP TABLE IF EXISTS fdefense''')
c.execute('''CREATE TABLE fdefense
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, tackles text, fumbles text, sacks text, interceptions text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')


conn.commit()
conn.close()