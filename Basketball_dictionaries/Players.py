players = [
    {
        "name": "Kevin Durant",
        "age":34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age":24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age":32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age":33, "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age":32, "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "",
        "age":16,
        "position": "P",
        "team": "en"
    }
]

class Player:

    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    @classmethod
    def get_team(cls, team_list):
        new_team_list = []
        for person in team_list:
            teamMember = Player(person)
            new_team_list.append(teamMember)
        return new_team_list


    def display_player_attributes(self):
        print(f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Position: {self.position}\n"
            f"Team: {self.position}\n")
        return self


# kevin = Player(players[0])
# jason = Player(players[1])
# kyrie = Player(players[2])

# kevin.display_player_attributes()
# jason.display_player_attributes()
# kyrie.display_player_attributes()

team_list = []
for person in players:
    team_member = Player(person)
    team_list.append(team_member)

print(team_list)

for playr in team_list:
    playr.display_player_attributes()

a_different_teamList = Player.get_team(players)

print(a_different_teamList)
for person in a_different_teamList:
    person.display_player_attributes()