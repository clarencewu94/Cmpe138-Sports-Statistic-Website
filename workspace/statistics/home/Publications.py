class User:

    def __init__(self, user_name):

        self.user_name = user_name

    def get_user_name(self):
        return self.user_name


class Game:
    def __init__(self, game_name):
        
        self.game_name = game_name
    
    def get_game_name(self):
        return self.game_name
    
class Game_Type:
    def __init__(self, game_type):
        
        self.game_type = game_type
    
    def get_game_type(self):
        return self.game_type
        
class Stats:
    def __init__(self, stat_name):
        
        self.stat_name = stat_name
    
    def get_stat_name(self):
        return self.stat_name
        
class Stat_type:
    def __init__(self, stat_type):
        
        self.stat_type = stat_type
    
    def get_stat_type(self):
        return self.stat_type