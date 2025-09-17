# Football score 
# MP W L D GF GA GD Pts

#if same point print by sorted name 

data_dict = dict()

while True:
    input_val = input("Enter : ")
    if input_val == "quit":
        break
    team1, team2, score1, score2 = input_val.split()
    score1, score2 = int(score1), int(score2)

    #MP
    if team1 not in data_dict:
        data_dict[team1] = {
            "MP" : 1,
            "W" : 0,
            "D" : 0,
            "L" : 0,
            "GF" : 0,
            "GA" : 0,
            "GD" : 0,
            "Pts" : 0,
        }
    else: 
        data_dict[team1]['MP'] += 1

    if team2 not in data_dict:
        data_dict[team2] = {
            "MP" : 1,
            "W" : 0,
            "D" : 0,
            "L" : 0,
            "GF" : 0,
            "GA" : 0,
            "GD" : 0,
            "Pts" : 0,
        }
    else: 
        data_dict[team2]['MP'] += 1
        
    #W L D
    if score1 > score2:
        data_dict[team1]["W"] += 1
        data_dict[team2]["L"] += 1
    elif score2 > score1:
        data_dict[team1]["L"] += 1
        data_dict[team2]["W"] += 1
    else: 
        data_dict[team1]["D"] += 1
        data_dict[team2]["D"] += 1

    
    data_dict[team1]["GF"] += score1
    data_dict[team1]["GA"] += score2

    data_dict[team2]["GF"] += score2
    data_dict[team2]["GA"] += score1


for key, value in data_dict.items():
    value['Pts'] = value["W"] * 3 + value['D']
    value['GD'] = value['GF'] - value['GA']

print("============================================")
print(f"{'Rank':<4}{'Team':<8}{'MP':>4}{'W':>4}{'D':>4}{'L':>4}{'GF':>4}{'GA':>4}{'GD':>4}{'Pts':>4}")
print("============================================")

idx = 1
rst = []
amount = 1 
recent_most = 0
for key, value in sorted(data_dict.items(), key=lambda x : x[1]['Pts'], reverse=True):
    # print(key, value['Pts'])
    if value['Pts'] >= recent_most:
        rst.append((f"{idx:<4}{key:<8}{value['MP']:>4}{value['W']:>4}{value["D"]:>4}{value['L']:>4}{value['GF']:>4}{value['GA']:>4}{value['GD']:>4}{value['Pts']:>4}",key))
        recent_most = value['Pts']
        amount += 1

    else: 

        if len(rst) != 0:
            for item, name in sorted(rst, key=lambda x : x[1]):
                print(item)
        rst = []
        idx += 1
        amount = 1
        recent_most = value['Pts']

        rst.append((f"{idx:<4}{key:<8}{value['MP']:>4}{value['W']:>4}{value["D"]:>4}{value['L']:>4}{value['GF']:>4}{value['GA']:>4}{value['GD']:>4}{value['Pts']:>4}",key))

for item, name in sorted(rst, key=lambda x : x[1]):
                print(item)

print("============================================")