import pprint as pp

inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')

all_game_dict = {}

for line in lines:
    line_components = line.split(":")

    # pp.pprint(line_components)
    game_number = line_components[0].split(" ")[1]

    print(game_number)
    # pp.pprint(line_components[1].split(";"))
    game_cubes = line_components[1].split(";")

    pp.pprint(game_cubes)

    game_dict = {"red": 0, "green": 0, "blue": 0}

    for game in game_cubes:
        game = game.split(",")
        for smol in game:
            smol = str.split(smol)
            game_dict[smol[1]] = max(int(smol[0]), game_dict[smol[1]])

    print(game_dict)

    all_game_dict[int(game_number)] = game_dict
    print("-------------------------------------------------")

# pp.pprint(all_game_dict)

'''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
12 red cubes, 13 green cubes, and 14 blue cubes

'''

super_sum = 0

for key, value in all_game_dict.items():
    print(key, value)
    if value['red'] <= 12 and value['green'] <= 13 and value['blue'] <= 14:
        print(key)
        super_sum += key
print("-------------")
print(super_sum)
