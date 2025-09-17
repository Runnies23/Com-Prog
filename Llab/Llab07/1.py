import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

# specifying the zip file name
filename = "IMDB_movies_merged.json"

### do not forget to uncomment the next line to read json data
data = read_json(filename)

#=================================================================

def q1():
    rst = []
    director_lst = """Denis Villeneuve
Emily Goldberg
George Lucas
Irvin Kershner
Michel Parbot
Richard Marquand
Ridley Scott
Robert Guenette
Tony Miller""".split('\n')
    for i in data:	
        if 'cast' not in i or  i['ratingValue'] == "":
            continue
        print(i['director'])
        # for name in i['director']:
        if i['director']['name'] in director_lst:
            try: 
                i['ratingValue'] = float(i['ratingValue'])
            except Exception as e:
                print(e)
            rst.append(i)
            continue
        # for name in i['cast']:
        #     if "Harrison Ford" in name['name']:
        #         try: 
        #             i['ratingValue'] = float(i['ratingValue'])
        #         except Exception as e:
        #             print(e)
        #         rst.append(i)
        #         continue
                
    all_director = []
    top_five_score = []
    for i in sorted(rst, key=lambda x : x['ratingValue'],reverse=True):
      if len(top_five_score) > 5:
        break

      all_director.append(i['director']['name'])
      if i['ratingValue'] is top_five_score:
        continue
      else: 
        top_five_score.append(i['ratingValue'])
      
    all_director.sort()
    all_director = [i for i in all_director if i != "Steven Spielberg"]
    print("\n".join(all_director))

def q2():
    rst = []
    for i in data:	
        if 'cast' not in i or  i['ratingValue'] == "":
            continue

        Harrison = False
        Tommy = False
        for name in i['cast']:
            try: 
                i['ratingValue'] = float(i['ratingValue'])
            except Exception as e:
                pass
            if name['name'] == "Harrison Ford":
                Harrison = True
            if name['name'] == "Tommy Lee Jones":
                Tommy = True

            if Harrison and Tommy:
                rst.append(i)
                continue
    print(sorted(rst, key=lambda x : x['ratingValue'],reverse=True)[0]['name'])

#=================================================================

print('(1) Answer of Q1')
print('(2) Answer of Q2')
ans = input('or just press (Enter): ')
if ans == '1':
  q1()
elif ans == '2':
  q2()
else:
    print('Nothing to do..')