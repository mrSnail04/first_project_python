import json
class Tournament:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

class ChessPlayer:

    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data['tournaments']))
        return cls(tournaments)

t1 = Tournament('Aeroflot Open', 2010)
t2 = Tournament('FIDE World Cup', 2018)
t3 = Tournament('FIDE Grand Prix', 2016)

p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1, default = lambda obj: obj.__dict__, indent = 4, sort_keys= True)
print(type(json_data))
print(json_data)

decode_player = ChessPlayer.from_json(json.loads(json_data))
print(decode_player)
print(decode_player.tournaments)

for i in decode_player.tournaments:
    print(i.name, i.year)