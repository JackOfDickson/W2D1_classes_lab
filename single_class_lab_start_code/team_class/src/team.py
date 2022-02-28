
class Team:
    def __init__ (self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

#methods below
    def add_player(self, name):
        self.players.append(name)

    def has_player(self, name):
        checker = []
        for player in self.players:
            if player == name:
                checker.append(name)
            else: continue
        if checker == []:
            return False
        else: return True

    def play_game(self, game_result):
        if game_result == True:
            self.points += 3
        else:
            self.points += 0





