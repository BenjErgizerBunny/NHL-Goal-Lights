# red, blue, green, orange, teal
# Avalanche, Blackhawks, Blue Jackets, Blues, Bruins, Canadiens, Canucks, Capitals, Coyotes, Devils, Ducks, Flames, Flyers, Hurricanes, Islanders, Jets, Kings, Lightning, Maple Leafs ,Oilers, Panthers, Penguins, Predators, Red Wings, Sabres, Senators, Sharks, Stars, Wild


# from colorama import init, Fore, Style
import datetime
import json
import os
import platform
import sys
import time
import requests
import socket
# import sqlite3
# connection = sqlite3.connect('beels.db')

i = datetime.datetime.now()

refresh_time = 1
api_url = 'http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp?loadScoreboard=jQuery110105207217424176633_1428694268811&_=1428694268812'
api_headers = {'Host': 'live.nhle.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36', 'Referer': 'http://www.nhl.com/ice/scores.htm'}

old_score = 0 #Home team variables
team_playing = False #Home team variables
away_old_score = 0 #Away team variables
show_today_only = False #Away team variables


#colours
red = 'https://maker.ifttt.com/trigger/red/with/key/kbHfUo-8sIJDkJPQKgUIN'
blue = 'https://maker.ifttt.com/trigger/leafgoal/with/key/kbHfUo-8sIJDkJPQKgUIN'
orange = 'https://maker.ifttt.com/trigger/orange/with/key/kbHfUo-8sIJDkJPQKgUIN'
teal = 'https://maker.ifttt.com/trigger/teal/with/key/kbHfUo-8sIJDkJPQKgUIN'
green = 'https://maker.ifttt.com/trigger/green/with/key/kbHfUo-8sIJDkJPQKgUIN'

# sql_command1 = """CREATE TABLE IF NOT EXISTS teams_table (
# team INTEGER PRIMARY KEY,
# beel_time CURRENT_TIMESTAMP,
# fname text);"""


def change_teams():
    change_teams = raw_input("Do you want to change your favourite teams? (Y/N)")
    if change_teams == "Y":
            team = raw_input("Enter your favourite team")
            colour = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')
            team2 = raw_input("Enter your second favourite team or 'none'")
            if not team2 == "none":
                colour2 = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')
                team3 = raw_input("Enter your third favourite team or 'none'")
                colour3 = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')
                if not team3 == "none":
                    team4 = raw_input("Enter your third favourite team or 'none'")
                    colour4 = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')
                    if not team4 == "none":
                        team5 = raw_input("Enter your third favourite team or 'none'")
                        colour5 = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')
                        if not team5 == "none":
                            team6 = raw_input("Enter your third favourite team or 'none'")
                            colour6 = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')
                            if not team6 == "none":
                                team7 = raw_input("Enter your third favourite team or 'none'")
                                colour7 = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')
                                if not team7 == "none":
                                    team8 = raw_input("Enter your third favourite team or 'none'")
                                    colour8 = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')
                                    if not team8 == "none":
                                        team9 = raw_input("Enter your third favourite team or 'none'")
                                        colour9 = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')
                                        if not team9 == "none":
                                            team10 = raw_input("Enter your third favourite team or 'none'")
                                            colour10 = raw_input('Enter their colour (red, blue, green, orange, teal, yellow )')

def main():
	global refresh_time
	global team
	global team_playing
	global old_score
	global away_old_score

	# Format dates to match NHL API style:

	# Todays date
	t = datetime.datetime.now()
	todays_date = "" + t.strftime("%A") + " " + "%s/%s" % (t.month, t.day)

	# Yesterdays date
	y =y = t - datetime.timedelta(days=1)
	yesterdays_date = "" + y.strftime("%A") + " " + "%s/%s" % (y.month, y.day)

	while True:

			try:
				r = requests.get(api_url, headers=api_headers) #making sure there is a connection with the API
			except (requests.ConnectionError): #Catch these errors
				print ("Could not get response from NHL.com trying again...")
				time.sleep(5)
				continue
			except(requests.HTTPError):
				print ("HTTP Error when loading url. Please restart program. ")
				sys.exit(0)
			except(requests.Timeout):
				print ("The request took too long to process and timed out. Trying again... ")
				time.sleep(5)
			except(socket.error):
				print ("Could not get response from NHL.com trying again...")
				time.sleep(5)
			except(requests.RequestException):
				print ("Unknown error. Please restart the program. ")
				sys.exit(0)


			# We get back JSON data with some JS around it, gotta remove the JS
			json_data = r.text

			# Remove the leading JS
			json_data = json_data.replace('loadScoreboard(', '')

			# Remove the trailing ')'
			json_data  = json_data[:-1]

			data = json.loads(json_data)
			for key in data:
				if key == 'games':
					for game_info in data[key]:

						# Assign more meaningful names
						game_clock = game_info['ts']
						game_stage = game_info['tsc']
						status = game_info['bs']

						away_team_locale = game_info['atn']
						away_team_name = game_info['atv'].title()
						away_team_score = game_info['ats']
						away_team_result = game_info['atc']


						home_team_locale = game_info['htn']
						home_team_name = game_info['htv'].title()
						home_team_score = game_info['hts']
						home_team_result = game_info['htc']

						# Fix strange names / locales returned by NHL
						away_team_locale = fix_locale(away_team_locale)
						home_team_locale = fix_locale(home_team_locale)
						away_team_name = fix_name(away_team_name)
						home_team_name = fix_name(home_team_name)



def home_team():
    if team in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score
    if team2 in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour2)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score

    if team3 in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour3)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score

    if team4 in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour4)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score

    if team5 in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour5)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score

    if team6 in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour6)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score

    if team7 in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour7)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score

    if team8 in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour8)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score

    if team9 in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour9)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score

    if team10 in home_team_name:
        if int(old_score) < int(home_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour10)
            time.sleep(1)
            old_score = int(home_team_score) # Set the old_score to be the current score

    # if team or team1 or team2 or team3 or team4 or team5 or team6 or team7 or team8 or team9 or team10 not in (home_team_name)
        # print("No Goals!")
    if team not in home_team_name:
        print("no goals")

def away_team():
    if team in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score
    if team2 in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour2)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score

    if team3 in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour3)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score

    if team4 in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour4)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score

    if team5 in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour5)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score

    if team6 in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour6)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score

    if team7 in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour7)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score

    if team8 in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour8)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score

    if team9 in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour9)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score

    if team10 in away_team_name:
        if int(old_score) < int(away_team_score): # If the old score < the new score, a goal was scored
            print team + " have scored a goal!"
            r = requests.post(colour10)
            time.sleep(1)
            old_score = int(away_team_score) # Set the old_score to be the current score


def fix_locale(team_locale):
	# NHL API forces team name in locale for both New York teams, i.e. locale + name == "NY Islanders islanders"
	if 'NY ' in team_locale:
		return 'New York'

	if 'Montr' in team_locale:
		return 'Montreal'

	return team_locale

def fix_name(team_name):
	#Change 'redwings' to 'Red Wings'
	if 'wings' in team_name:
		return 'Red Wings'

	if 'jackets' in team_name:
		return 'Blue Jackets'

	if 'leafs' in team_name:
		return 'Maple Leafs'

	return team_name

change_teams()
main()
away_team()
home_team()
