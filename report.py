class Report:
    def __init__(self):
        self.event_code = None
        self.event_info = None
        self.event_name = None
        self.team_numbers = []
        self.team_infos = []
        self.most_wins = []
        self.most_wins_5_years = []
        self.most_finalist = []
        self.most_finalist_5_years = []
        self.most_chairmans = []
        self.most_chairmans_5_years = []
        self.most_ei = []
        self.most_ei_5_years = []

    def __str__(self):
        return str(self.event_code) + ": " + str(self.event_name)


class TeamInfo:
    def __init__(self, team_number):
        self.team_number = team_number
        self.team_name = ""
        self.rookie_year = None
        self.past_chairmans = []
        self.past_chairmans_5_years = []
        self.past_ei = []
        self.past_ei_5_years = []
        self.past_winner = []
        self.past_winner_5_years = []
        self.past_finalist = []
        self.past_finalist_5_years = []
