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

# scrapes for team name. not actually used in this version
def get_team_name():
    name = [n.get_text() for n in soup.find_all(class_="page-title__primary")]
    return name

# gets player name
def get_player():
    roster = soup.find('div', class_='bg-concrete pad-15-20 border')
    weird_name= [p.get_text() for p in roster.find_all('a')]
    player_name = [name.replace('\xa0', ' ') for name in weird_name]
    return player_name

# gets link to player page
def get_player_link():
    roster = soup.find('div', class_='bg-concrete pad-15-20 border')
    player_link = [l.get('href') for l in roster.find_all('a')]
    add_player_link = "https://www.rotowire.com/"
    player_link = [add_player_link + i for i in player_link]
    return player_link

# scrapes player page for player stats
def get_stats():
    global wl
    pitcher_check = [p.get_text() for p in (soup.find_all('span', class_="hide-until-xl"))]
    pitcher_check = pitcher_check[0]
    # this version doesn't use pitcher stats, so this loops past pitchers
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

# opens the csv that has the team stats and converts to dicts
tup_list = []
with open ('moneyball_overall.csv', 'r') as file:
    lines = file.read().split("\n")
teams = [i.split(',') for i in lines]
key = teams.pop(0)
for i in teams:
    entry = list(zip(key,i))
    tup_list.append(entry)
team_list = [dict(i) for i in tup_list]

# list that will be appended to with player stats
player_stats = [['name', 'AVG', 'HR', 'RBI', 'R', 'SB','Team W-L%']]

# loops through each player in each team. 
# follows the player link and appends to the player stats list
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

# converts to csv format
player_stats = [str(i) for i in player_stats if i]
player_list =''
for i in player_stats:
    player_list += str(i[1:-1])
    player_list += '\n'

# saves to the csv that will be used in the machinelearn program
with open('moneyballs_players_csv.csv', 'w') as file:
    file.write(str(player_list))

