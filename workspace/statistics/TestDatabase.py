import sqlite3
conn = sqlite3.connect('sports.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS user''')
c.execute('''CREATE TABLE user
             (userid text not null, password text not null, id integer primary key autoincrement)''')


c.execute('''INSERT INTO user (userid, password) VALUES (Sideshow_Bob, pancakes)''')
c.execute('''INSERT INTO user (userid, password) VALUES (Jimbo_Jones, waffles)''')
c.execute('''INSERT INTO user (userid, password) VALUES (Kearny, french_toast)''')
c.execute('''INSERT INTO user (userid, password) VALUES (Nelson_Muntz, bacon)''')
c.execute('''INSERT INTO user (userid, password) VALUES (KRUSTYtheCLOWN, ScrambledEggs)''')

c.execute('''DROP TABLE IF EXISTS basketball''')
c.execute('''CREATE TABLE basketball
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, field_goals text, three_pointers text, free_throws text, rebounds text, assists text, steals text, blocks text, turnovers text, personal_fouls text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 1, 3-5, 5-7, 2-3, 4, 5, 2, 2, 9, 1)''')
c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 2, 5-5, 2-7, 2-6, 3, 9, 1, 8, 12, 6)''')
c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 3, 8-8, 2-3, 0-2, 4, 6, 4, 8, 1, 3)''')
c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 4, 2-5, 5-8, 3-3, 4, 6, 2, 0, 5, 6)''')
c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 5, 6-7, 3-7, 2-3, 7, 2, 2, 2, 3, 2)''')
c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 6, 1-6, 5-6, 2-3, 1, 5, 5, 2, 6, 5)''')
c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 7, 1-1, 2-3, 2-3, 3, 3, 2, 3, 4, 6)''')
c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 8, 0-0, 6-6, 2-3, 2, 4, 3, 2, 2, 1)''')
c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 9, 3-3, 5-5, 2-3, 6, 2, 2, 2, 1, 2)''')
c.execute('''INSERT INTO basketball Values(KRUSTYtheCLOWN, 10, 0-1, 3-3, 5-5, 2, 8, 2, 3, 0, 1)''')

c.execute('''DROP TABLE IF EXISTS soccer''')
c.execute('''CREATE TABLE soccer
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, shots text, saves text, offside text, fouls text, assists text, yellow_cards text, red_cards text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 1, 3-5, 5-7, 9, 4, 5, 2, 2)''')
c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 2, 5-5, 2-7, 5, 3, 9, 1, 8)''')
c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 3, 8-8, 2-3, 2, 4, 6, 4, 8)''')
c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 4, 2-5, 5-8, 7, 4, 6, 2, 0)''')
c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 5, 6-7, 3-7, 8, 7, 2, 2, 2)''')
c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 6, 1-6, 5-6, 1, 1, 5, 5, 2)''')
c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 7, 1-1, 2-3, 7, 3, 3, 2, 3)''')
c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 8, 0-0, 6-6, 7, 2, 4, 3, 2)''')
c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 9, 3-3, 5-5, 2, 6, 2, 2, 2)''')
c.execute('''INSERT INTO soccer Values(KRUSTYtheCLOWN, 10, 0-1, 3-3, 5, 2, 8, 2, 3)''')

c.execute('''DROP TABLE IF EXISTS tennis''')
c.execute('''CREATE TABLE tennis
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, winners text, double_faults text, aces text, serves text, net_faults text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 1, 9, 3, 2, 3-9, 5)''')
c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 2, 5, 7, 6, 3-3, 9)''')
c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 3, 8, 3, 2, 4-5, 6)''')
c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 4, 5, 8, 3, 4-8, 6)''')
c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 5, 7, 7, 2, 7-8, 2)''')
c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 6, 6, 6, 3, 1-3, 5)''')
c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 7, 1, 3, 3, 3-12, 3)''')
c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 8, 0, 6, 3, 2-7, 4)''')
c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 9, 3, 5, 6, 6-6, 2)''')
c.execute('''INSERT INTO tennis Values(KRUSTYtheCLOWN, 10, 1, 3, 5, 2-2, 8)''')

c.execute('''DROP TABLE IF EXISTS golf''')
c.execute('''CREATE TABLE golf
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, course_name text, first text, second text, third text, fourth text, fifth text, sixth text, seventh text, eighth text, ninth text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 1, Great Island Golf, 5, 2, 4, 0, 2, 2, 9, 1, -2)''')
c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 2, Kahuna's Golf, 2, 2, 3, 0, 1, 0, -1, 4, 0)''')
c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 3, Great Island Golf, 2, 0, 4, -2, 4, 4, 1, 3, 2)''')
c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 4, Great Island Golf, 5, 3, 4, 0, 2, 0, 5, 0, -1)''')
c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 5, Kahuna's Golf, 3, 2, -1, 2, 2, 2, 3, 2, 1)''')
c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 6, Great Island Golf, 5, 3, 1, 5, 5, 2, 1, 1, 1)''')
c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 7, Green Acres, 2, 2, 3, 3, 2, 3, 4, 6, 3)''')
c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 8, Hilltop Golf, 6, -2, 2, 4, 3, 2, 2, 1, -1)''')
c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 9, Kahuna's Golf, 5, 2, 6, 2, 2, 2, 1, 2, -2)''')
c.execute('''INSERT INTO golf Values(KRUSTYtheCLOWN, 10, Green Acres, 3, 5, 2, -1, 2, 3, 0, 1, 0)''')

c.execute('''DROP TABLE IF EXISTS hockey''')
c.execute('''CREATE TABLE hockey
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, goals text, defence_blocked_shots text, off_target_shots text, goals_stopped text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 1, 3-5, 7, 2, 4-4)''')
c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 2, 5-5, 2, 2, 3-5)''')
c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 3, 8-8, 2, 0, 4-8)''')
c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 4, 2-5, 5, 3, 4-5)''')
c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 5, 6-7, 7, 2, 1-6)''')
c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 6, 1-6, 6, 8, 2-3)''')
c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 7, 1-1, 3, 4, 3-5)''')
c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 8, 0-0, 6, 3, 2-2)''')
c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 9, 3-3, 5, 2, 6-9)''')
c.execute('''INSERT INTO hockey Values(KRUSTYtheCLOWN, 10, 0-1, 3, 5, 2-3)''')

c.execute('''DROP TABLE IF EXISTS foffense''')
c.execute('''CREATE TABLE foffense
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, completions text, yards text, touchdowns text, interceptions text, field_goals text, extra_points text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 1, 3, 5, 3, 4, 5-5, 2)''')
c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 2, 5, 2, 6, 3, 9-10, 1)''')
c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 3, 8, 2, 0, 4, 6-6, 3)''')
c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 4, 5, 5, 3, 4, 6-8, 9)''')
c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 5, 7, 3, 3, 7, 2-3, 4)''')
c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 6, 6, 5, 3, 1, 5-5, 3)''')
c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 7, 1, 3, 2, 3, 3-3, 2)''')
c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 8, 0, 6, 3, 2, 4-5, 1)''')
c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 9, 3, 5, 3, 6, 2-9, 7)''')
c.execute('''INSERT INTO foffense Values(KRUSTYtheCLOWN, 10, 0, 3, 5, 2, 8-10, 12)''')

c.execute('''DROP TABLE IF EXISTS fdefense''')
c.execute('''CREATE TABLE fdefense
             (userid text, game INTEGER PRIMARY KEY AUTOINCREMENT, tackles text, fumbles text, sacks text, interceptions text, FOREIGN KEY (userid) REFERENCES user(userid) ON DELETE CASCADE)''')

c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 1, 2, 2, 9, 1)''')
c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 2, 1, 8, 12, 6)''')
c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 3, 4, 8, 1, 3)''')
c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 4, 2, 0, 5, 6)''')
c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 5, 2, 2, 3, 2)''')
c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 6, 5, 2, 6, 5)''')
c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 7, 2, 3, 4, 6)''')
c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 8, 3, 2, 2, 1)''')
c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 9, 2, 2, 1, 2)''')
c.execute('''INSERT INTO fdefense Values(KRUSTYtheCLOWN, 10, 2, 3, 0, 1)''')

conn.commit()
conn.close()