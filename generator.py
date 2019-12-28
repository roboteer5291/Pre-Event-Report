import tbapy
from report import Report, TeamInfo
from create_output import main
import argparse


def get_event_info(event_code="2020mibel"):
    global report
    event_info = tba.event(event_code)
    report.event_info = event_info
    report.event_name = event_info.name
    report.event_code = event_code


def get_teams(event_code="2020mibel"):
    global report
    teams = tba.event_teams(event_code)
    teams.sort(key=lambda x: x.team_number)
    team_numbers = []
    for team in teams:
        team_numbers.append(team.team_number)
    global report
    report.team_numbers = team_numbers
    return teams


def get_team_infos(full_teams=[]):
    global report
    for full_team in full_teams:
        team_info = TeamInfo(full_team.team_number)
        awards = tba.team_awards(full_team.team_number)
        team_info.team_name = full_team.nickname
        team_info.rookie_year = full_team.rookie_year
        for award in awards:
            if award.award_type == 0:  # Chairman's
                if tba.event(event=award.event_key, simple=True).event_type not in [99, 100]:
                    team_info.past_chairmans.append(award.event_key)
                    if int(award.event_key[:4]) >= int(report.event_code[:4]) - 5:
                        team_info.past_chairmans_5_years.append(award.event_key)
            elif award.award_type == 9:  # EI
                if tba.event(event=award.event_key, simple=True).event_type not in [99, 100]:
                    team_info.past_ei.append(award.event_key)
                    if int(award.event_key[:4]) >= int(report.event_code[:4]) - 5:
                        team_info.past_ei_5_years.append(award.event_key)
            elif award.award_type == 1:  # Winner
                if tba.event(event=award.event_key, simple=True).event_type not in [99, 100]:
                    team_info.past_winner.append(award.event_key)
                    if int(award.event_key[:4]) >= int(report.event_code[:4]) - 5:
                        team_info.past_winner_5_years.append(award.event_key)
            elif award.award_type == 2:  # Finalist
                if tba.event(event=award.event_key, simple=True).event_type not in [99, 100]:
                    team_info.past_finalist.append(award.event_key)
                    if int(award.event_key[:4]) >= int(report.event_code[:4]) - 5:
                        team_info.past_finalist_5_years.append(award.event_key)
        report.team_infos.append(team_info)


def generate_statistics():
    global report
    teams = report.team_infos.copy()
    # Event wins
    teams.sort(key=lambda x: len(x.past_winner), reverse=True)
    for i in range(10):
        if len(teams[i].past_winner) == 0:
            break
        report.most_wins.append([teams[i].team_number, len(teams[i].past_winner)])
    # Event wins 5 years
    teams.sort(key=lambda x: len(x.past_winner_5_years), reverse=True)
    for i in range(10):
        if len(teams[i].past_winner_5_years) == 0:
            break
        report.most_wins_5_years.append([teams[i].team_number, len(teams[i].past_winner_5_years)])
    # Event finalist
    teams.sort(key=lambda x: len(x.past_finalist), reverse=True)
    for i in range(10):
        if len(teams[i].past_finalist) == 0:
            break
        report.most_finalist.append([teams[i].team_number, len(teams[i].past_finalist)])
    # Event finalist 5 years
    teams.sort(key=lambda x: len(x.past_finalist_5_years), reverse=True)
    for i in range(10):
        if len(teams[i].past_finalist_5_years) == 0:
            break
        report.most_finalist_5_years.append([teams[i].team_number, len(teams[i].past_finalist_5_years)])
    # Event chairmans
    teams.sort(key=lambda x: len(x.past_chairmans), reverse=True)
    for i in range(10):
        if len(teams[i].past_chairmans) == 0:
            break
        report.most_chairmans.append([teams[i].team_number, len(teams[i].past_chairmans)])
    # Event chairmans 5 years
    teams.sort(key=lambda x: len(x.past_chairmans_5_years), reverse=True)
    for i in range(10):
        if len(teams[i].past_chairmans_5_years) == 0:
            break
        report.most_chairmans_5_years.append([teams[i].team_number, len(teams[i].past_chairmans_5_years)])
    # Event ei
    teams.sort(key=lambda x: len(x.past_ei), reverse=True)
    for i in range(10):
        if len(teams[i].past_ei) == 0:
            break
        report.most_ei.append([teams[i].team_number, len(teams[i].past_ei)])
    # Event ei 5 years
    teams.sort(key=lambda x: len(x.past_ei_5_years), reverse=True)
    for i in range(10):
        if len(teams[i].past_ei_5_years) == 0:
            break
        report.most_ei_5_years.append([teams[i].team_number, len(teams[i].past_ei_5_years)])


def generate_report(event_code="2020mibel"):
    get_event_info(event_code)
    full_teams = get_teams(event_code)
    get_team_infos(full_teams=full_teams)
    generate_statistics()


TBA_KEY = "Ps4iAATGfkVj8Rl3bID7CnfySNNsrVi2aN4Ho6zvaKzvgvKcbGNmRGd85WadJTzX"
tba = tbapy.TBA(TBA_KEY)

parser = argparse.ArgumentParser(description="Generate a pre-event report for a FRC competition")

parser.add_argument("event_code", metavar="Event Code", type=str,
                    help="The event code to be looked up")
args = parser.parse_args()

report = Report()

generate_report(args.event_code)
print(str(report))
main(report)
