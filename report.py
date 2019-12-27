class Report:
    def __init__(self):
        self.event_code = None
        self.event_info = None
        self.event_name = None
        self.team_numbers = []
        self.team_infos = []
        self.most_wins = []
        self.most_finalist = []
        self.most_chairmans = []
        self.most_ei = []

    def __str__(self):
        return str(self.event_code) + ": " + str(self.event_name)


class TeamInfo:
    def __init__(self, team_number):
        self.team_number = team_number
        self.team_name = ""
        self.rookie_year = None
        self.past_chairmans = []
        self.past_ei = []
        self.past_winner = []
        self.past_finalist = []
