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




