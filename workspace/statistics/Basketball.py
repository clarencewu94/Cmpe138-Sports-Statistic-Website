<<<<<<< HEAD
class Basketball:

    def __init__(self, FG, TPT, FT, REB, AST, STL, BLK, TO, PF):

        self.FG = FG
        self.TPT = TPT
        self.FT = FT
        self.REB = REB
        self.AST = AST
        self.STL = STL
        self.BLK = BLK
        self.TO = TO
        self.PF = PF

    def get_FG(self):
        return self.FG

    def get_TPT(self):
        return self.TPT

    def get_FT(self):
        return self.FT

    def get_REB(self):
        return self.REB

    def get_AST(self):
        return self.AST

    def get_STL(self):
        return self.STL

    def get_BLK(self):
        return self.BLK

    def get_TO(self):
        return self.TO

    def get_PF(self):
        return self.PF

class Foffense:
    def __init__(self,CMP,YDS,TD,INTs,FG,XP):

        self.CMP = CMP
        self.YDS = YDS
        self.TD = TD
        self.INTs = INTs
        self.FG = FG 
        self.XP = XP

    def get_CMP(self):
        return self.CMP
    
    def get_YDS(self):
        return self.YDS 
    
    def get_TD(self):
        return self.TD
    
    def get_INTs(self):
        return self.INTs
    
    def get_FG(self):
        return self.FG
        
    def get_XP(self):
        return self.XP

class Fdefense:
    def __init__(self,tackles,fumbles,sacks,interception):

        self.tackles = tackles
        self.fumbles = fumbles
        self.sacks = sacks
        self.interception = interception

    def get_tackles(self):
        return self.tackles
    
    def get_fumbles(self):
        return self.fumbles
    
    def get_sacks(self):
        return self.sacks
    
    def get_interception(self):
        return self.interception
    
class Soccer:
    def __init__(self,shows, saves, offside, fouls, assists, yellow_cards, red_cards):

        self.shows = shows
        self.saves = saves
        self.offside = offside
        self.fouls = fouls
        self.assists = assists
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

    def get_shows(self):
        return self.shows
    
    def get_saves(self):
        return self.saves
    
    def get_offside(self):
        return self.offside
        
    def get_fouls(self):
        return self.fouls 
    
    def get_assists(self):
        return self.assists
    
    def get_yellow_cards(self):
        return self.yellow_cards
 
    def get_red_cards(self):
        return self.red_cards

class Tennis:
    def __init__(self, winners, double_faults, aces, serves, net_faults):

        self.winners = winners
        self.double_faults = double_faults 
        self.serves = serves
        self.net_faults = net_faults
        self.aces = aces
        
    def get_winners(self):
        return self.winners
    def get_double_faults(self):
        return self.double_faults

    def get_serves(self):
        return self.serves

    def get_net_faults(self):
        return self.net_faults

    def get_aces(self):
        return self.aces 
    

class Golf:
    def __init__(self, course_name, first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, eighteenth):

        self.course_name = course_name
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
        self.sixth = sixth
        self.seventh = seventh
        self.eighth = eighth
        self.ninth = ninth
        self.tenth = tenth
        self.eleventh = eleventh
        self.twelfth = twelfth
        self.thirteenth = thirteenth
        self.fourteenth = fourteenth
        self.fifteenth = fifteenth
        self.sixteenth = sixteenth
        self.seventeenth = seventeenth
        self.eighteenth = eighteenth

    def get_course_name(self):
        return self.course_name
    
    def get_first(self):
        return self.first 
    
    def get_second(self):
        return self.second
    
    def get_third(self):
        return self.third
    
    def get_fourth(self):
        return self.fourth

    def get_fifth(self):
        return self.fifth

    def get_sixth(self):
        return self.sixth

    def get_seventh(self):
        return self.seventh

    def get_eighth(self):
        return self.eighth

    def get_ninth(self):
        return self.ninth

    def get_tenth(self):
        return self.tenth

    def get_eleventh(self):
        return self.eleventh

    def get_twelfth(self):
        return self.twelfth

    def get_thirteenth(self):
        return self.thirteenth

    def get_fourteenth(self):
        return self.fourteenth

    def get_fiftheenth(self):
        return self.fifteenth

    def get_sixteenth(self):
        return self.sixteenth

    def get_seventheeth(self):
        return self.seventeenth

    def get_eighteenth(self):
        return self.eighteenth

class Hockey:
    def __init__(self,goals, defence_blocked_shots, off_target_shots, goals_stopped):
 
        self.goals = goals
        self.defence_blocked_shots = defence_blocked_shots
        self.off_target_shots = off_target_shots
        self.goals_stopped = goals_stopped

    def get_goals(self):
        return self.goals
    
    def get_defence_blocked_shots(self):
        return self.defence_blocked_shots
    
    def get_off_target_shots(self):
        return self.off_target_shots
    
    def get_goals_stopped(self):
        return self.goals_stopped
    
=======
class Basketball:

    def __init__(self, FG, TPT, FT, REB, AST, STL, BLK, TO, PF):

        self.FG = FG
        self.TPT = TPT
        self.FT = FT
        self.REB = REB
        self.AST = AST
        self.STL = STL
        self.BLK = BLK
        self.TO = TO
        self.PF = PF

    def get_FG(self):
        return self.FG

    def get_TPT(self):
        return self.TPT

    def get_FT(self):
        return self.FT

    def get_REB(self):
        return self.REB

    def get_AST(self):
        return self.AST

    def get_STL(self):
        return self.STL

    def get_BLK(self):
        return self.BLK

    def get_TO(self):
        return self.TO

    def get_PF(self):
        return self.PF

class Foffense:
    def __init__(self,CMP,YDS,TD,INTs,FG,XP):

        self.CMP = CMP
        self.YDS = YDS
        self.TD = TD
        self.INTs = INTs
        self.FG = FG 
        self.XP = XP

    def get_CMP(self):
        return self.CMP
    
    def get_YDS(self):
        return self.YDS 
    
    def get_TD(self):
        return self.TD
    
    def get_INTs(self):
        return self.INTs
    
    def get_FG(self):
        return self.FG
        
    def get_XP(self):
        return self.XP

class Fdefense:
    def __init__(self,tackles,fumbles,sacks,interception):

        self.tackles = tackles
        self.fumbles = fumbles
        self.sacks = sacks
        self.interception = interception

    def get_tackles(self):
        return self.tackles
    
    def get_fumbles(self):
        return self.fumbles
    
    def get_sacks(self):
        return self.sacks
    
    def get_interception(self):
        return self.interception
    
class Soccer:
    def __init__(self,shows, saves, offside, fouls, assists, yellow_cards, red_cards):

        self.shows = shows
        self.saves = saves
        self.offside = offside
        self.fouls = fouls
        self.assists = assists
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

    def get_shows(self):
        return self.shows
    
    def get_saves(self):
        return self.saves
    
    def get_offside(self):
        return self.offside
        
    def get_fouls(self):
        return self.fouls 
    
    def get_assists(self):
        return self.assists
    
    def get_yellow_cards(self):
        return self.yellow_cards
 
    def get_red_cards(self):
        return self.red_cards

class Tennis:
    def __init__(self, winners, double_faults, aces, serves, net_faults):

        self.winners = winners
        self.double_faults = double_faults 
        self.serves = serves
        self.net_faults = net_faults
        self.aces = aces
        
    def get_winners(self):
        return self.winners
    def get_double_faults(self):
        return self.double_faults

    def get_serves(self):
        return self.serves

    def get_net_faults(self):
        return self.net_faults

    def get_aces(self):
        return self.aces 
    

class Golf:
    def __init__(self, course_name, first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, eighteenth):

        self.course_name = course_name
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
        self.sixth = sixth
        self.seventh = seventh
        self.eighth = eighth
        self.ninth = ninth
        self.tenth = tenth
        self.eleventh = eleventh
        self.twelfth = twelfth
        self.thirteenth = thirteenth
        self.fourteenth = fourteenth
        self.fifteenth = fifteenth
        self.sixteenth = sixteenth
        self.seventeenth = seventeenth
        self.eighteenth = eighteenth

    def get_course_name(self):
        return self.course_name
    
    def get_first(self):
        return self.first 
    
    def get_second(self):
        return self.second
    
    def get_third(self):
        return self.third
    
    def get_fourth(self):
        return self.fourth

    def get_fifth(self):
        return self.fifth

    def get_sixth(self):
        return self.sixth

    def get_seventh(self):
        return self.seventh

    def get_eighth(self):
        return self.eighth

    def get_ninth(self):
        return self.ninth

    def get_tenth(self):
        return self.tenth

    def get_eleventh(self):
        return self.eleventh

    def get_twelfth(self):
        return self.twelfth

    def get_thirteenth(self):
        return self.thirteenth

    def get_fourteenth(self):
        return self.fourteenth

    def get_fiftheenth(self):
        return self.fifteenth

    def get_sixteenth(self):
        return self.sixteenth

    def get_seventheeth(self):
        return self.seventeenth

    def get_eighteenth(self):
        return self.eighteenth

class Hockey:
    def __init__(self,goals, defence_blocked_shots, off_target_shots, goals_stopped):
 
        self.goals = goals
        self.defence_blocked_shots = defence_blocked_shots
        self.off_target_shots = off_target_shots
        self.goals_stopped = goals_stopped

    def get_goals(self):
        return self.goals
    
    def get_defence_blocked_shots(self):
        return self.defence_blocked_shots
    
    def get_off_target_shots(self):
        return self.off_target_shots
    
    def get_goals_stopped(self):
        return self.goals_stopped
    
>>>>>>> 7a8e61f58d6b53971e99a0ea1d79d7758de06f45
   