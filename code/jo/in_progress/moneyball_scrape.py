import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.rotowire.com/baseball/team.php?team=LAD")
soup = BeautifulSoup(page.content, "html.parser")

# provides a list of links to all teams
def get_team_page():
    # finds div that contains all links to teams
    team_tabs = soup.find(class_="scroll-tabs is-compressed")
    team_name = [s.get_text() for s in soup.find(class_="scroll-tabs is-compressed")]
    team_link = [l.get('href') for l in soup.find(class_="scroll-tabs is-compressed")]
    # team_link only returns last half of url, so this adds it
    add_link = 'https://www.rotowire.com/baseball/'
    team_link = [add_link + i for i in team_link]
    return team_link

def get_team_name():
    name = [n.get_text() for n in soup.find_all(class_="page-title__primary")]
    return name

def get_player():
    roster = soup.find('div', class_='bg-concrete pad-15-20 border')
    weird_name= [p.get_text() for p in roster.find_all('a')]
    player_name = [name.replace('\xa0', ' ') for name in weird_name]
    return player_name

def get_player_link():
    roster = soup.find('div', class_='bg-concrete pad-15-20 border')
    player_link = [l.get('href') for l in roster.find_all('a')]
    add_player_link = "https://www.rotowire.com/"
    player_link = [add_player_link + i for i in player_link]
    return player_link

def get_stats():
    global wl
    pitcher_check = [p.get_text() for p in (soup.find_all('span', class_="hide-until-xl"))]
    pitcher_check = pitcher_check[0]
    if pitcher_check == "Pitcher":
        pass
    else:
        stat_box = soup.find(class_='p-card__stats-box')
        player_name = [p.get_text() for p in soup.find_all('div', class_='p-card__player-name')]
        stat_value = [float(s.get_text()) for s in stat_box.find_all(class_='p-card__stat-value')]
        stats_values = player_name
        for i in stat_value:
            stats_values.append(i)
            stats_values.append(wl)
        return stats_values

tup_list = []
with open ('moneyball_overall.csv', 'r') as file:
    lines = file.read().split("\n")
teams = [i.split(',') for i in lines]
key = teams.pop(0)
for i in teams:
    entry = list(zip(key,i))
    tup_list.append(entry)
team_list = [dict(i) for i in tup_list]

player_stats = [['name', 'AVG', 'HR', 'RBI', 'R', 'SB','Team W-L%']]

for link in get_team_page():
    team_name = link[-3:]
    for team in team_list:
        if team["Tm"] == team_name:
            wl = team['W-L%']
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    for link in get_player_link():
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        player_stats.append(get_stats())

player_stats = [str(i) for i in player_stats if i]

player_list =''
for i in player_stats:
    player_list += str(i[1:-1])
    player_list += '\n'

with open('moneyballs_players_csv.csv', 'w') as file:
    file.write(str(player_list))


""" 
change player stat list to be better csv format like overall.csv
firts will tyr to predict 
 """
"""
goal will be something like data = data[['team average batting','team avg wins']]


import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.rotowire.com/baseball/team.php?team=LAD")
soup = BeautifulSoup(page.content, "html.parser")

# provides a list of links to all teams
def get_team_page():
    # finds div that contains all links to teams
    team_tabs = soup.find(class_="scroll-tabs is-compressed")
    team_name = [s.get_text() for s in soup.find(class_="scroll-tabs is-compressed")]
    team_link = [l.get('href') for l in soup.find(class_="scroll-tabs is-compressed")]

    # team_link only returns last half of url, so this adds it
    add_link = 'https://www.rotowire.com/baseball/'
    team_link = [add_link + i for i in team_link]
    return team_link

def get_player():
    roster = soup.find('div', class_='bg-concrete pad-15-20 border')
    weird_name= [p.get_text() for p in roster.find_all('a')]
    player_name = [name.replace('\xa0', ' ') for name in weird_name]
    return player_name

def get_player_link():
    roster = soup.find('div', class_='bg-concrete pad-15-20 border')
    weird_name= [p.get_text() for p in roster.find_all('a')]
    player_link = [l.get('href') for l in roster.find_all('a')]
    add_player_link = "https://www.rotowire.com/"
    player_link = [add_player_link + i for i in player_link]
    return player_link

def get_stats():
    stat_box = soup.find(class_='p-card__stats-box')
    player_name = [p.get_text() for p in soup.find_all('div', class_='p-card__player-name')]
    stat_value = [s.get_text() for s in stat_box.find_all(class_='p-card__stat-value')]
    stat_name = [s.get_text() for s in (stat_box.find_all(class_='p-card__stat-name'))]
    stats = {'name': player_name, 'stat': stat_name, 'value': stat_value}
    return stats

team_roster_list = []
player_stats = []
for link in get_team_page():
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    team_roster_list.append(get_player())
    for link in get_player_link():
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        player_stats.append(get_stats())
player_list =''
for i in player_stats:
    player_list += str(i)
    player_list += '\n'

with open('moneyballs.csv', 'w') as file:
    file.write(str(player_list))







# """ 
# import pandas as pd

# #reads csv and shows data
# player_data = pd.read_csv('moneyballs_player_csv.csv', 'r')
# team_data = pd.read_csv('moneyball_overall.csv', 'r')

# # defines what data we look at
# x = player_data[['AVG', 'HR', 'RBI', 'R', 'SB']]
# y = team_data['W-L%']

# # splits data to use 80% as training data and %20 as test data
# training_data_player = [:(int((len(player_data)*0.8)))]
# test_data_player = [(int((len(player_data)*0.8))):]
# training_data_team = [:(int((len(team_data)*0.8)))]
# test_data_team = [(int((len(team_data)*0.8))):]

# #gets linear model formula
# from sklearn import linear_model
# regression = linear.model.LinearRegression()

# # sets some variable to to work in the regression model
# train_x = np.array(training_data_player[['AVG', 'HR', 'RBI', 'R', 'SB']])
# train_y = np.array(training_data_team['W-L%'])

# test_x = np.array(test_data_player[['AVG', 'HR', 'RBI', 'R', 'SB']])
# test_y = np.array(test_data_team['W-L%'])

# regression.fit(train_x,train_y)

# # prints the coefficient data with pandas:
# coeff_data = pd.DataFrame(regr.coef_ , x.columns , columns=['coefficients'])
# print(coeff_data)

# # predicts data
# y_pred = regr.predict(test_x)

# # checks accuracy
# from sklearn.metrics import r2_score
# r = r2_score(test_y , y_pred)
# print('r2 :',r) """


# import requests
# from bs4 import BeautifulSoup

# page = requests.get("https://www.rotowire.com/baseball/team.php?team=LAD")
# soup = BeautifulSoup(page.content, "html.parser")

# # provides a list of links to all teams
# def get_team_page():
#     # finds div that contains all links to teams
#     team_tabs = soup.find(class_="scroll-tabs is-compressed")
#     team_name = [s.get_text() for s in soup.find(class_="scroll-tabs is-compressed")]
#     team_link = [l.get('href') for l in soup.find(class_="scroll-tabs is-compressed")]
#     # team_link only returns last half of url, so this adds it
#     add_link = 'https://www.rotowire.com/baseball/'
#     team_link = [add_link + i for i in team_link]
#     return team_link

# def get_team_name():
#     name = [n.get_text() for n in soup.find_all(class_="page-title__primary")]
#     return name

# def get_player():
#     roster = soup.find('div', class_='bg-concrete pad-15-20 border')
#     weird_name= [p.get_text() for p in roster.find_all('a')]
#     player_name = [name.replace('\xa0', ' ') for name in weird_name]
#     return player_name

# def get_player_link():
#     roster = soup.find('div', class_='bg-concrete pad-15-20 border')
#     player_link = [l.get('href') for l in roster.find_all('a')]
#     add_player_link = "https://www.rotowire.com/"
#     player_link = [add_player_link + i for i in player_link]
#     return player_link

# def get_stats():
#     pitcher_check = [p.get_text() for p in (soup.find_all('span', class_="hide-until-xl"))]
#     pitcher_check = pitcher_check[0]
#     if pitcher_check == "Pitcher":
#         pass
#     else:
#         stat_box = soup.find(class_='p-card__stats-box')
#         player_name = [p.get_text() for p in soup.find_all('div', class_='p-card__player-name')]
#         stat_value = [s.get_text() for s in stat_box.find_all(class_='p-card__stat-value')]
#         stats_values = player_name
#         for i in stat_value:
#             stats_values.append(i)
#         return stats_values


# team_roster_list = []
# player_stats = [['name', 'AVG', 'HR', 'RBI', 'R', 'SB']]
# team_list = []
# for link in get_team_page():
#     page = requests.get(link)
#     soup = BeautifulSoup(page.content, "html.parser")
#     team_roster_list.append(get_team_name())
#     for link in get_player_link():
#         page = requests.get(link)
#         soup = BeautifulSoup(page.content, "html.parser")
#         player_stats.append(get_stats())
# player_list =''

# player_stats = [i for i in player_stats if i]

# for i in player_stats:
#     i = str(i)
#     player_list += str(i)
#     player_list += '\n'

# with open('moneyballs_players_csv.csv', 'w') as file:
#     file.write(str(player_list))