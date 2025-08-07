seq = [5,5,3,1,2,4,5,4]
dict_map_freq = dict()

for i in seq:
    if i in dict_map_freq:
        dict_map_freq[i] += 1
    else:
        dict_map_freq[i] = 1
    
set_ = dict_map_freq.values()
max_lenght, min_lenght = max(set_), min(set_)

dict_map_freq = sorted(dict_map_freq.items(),reverse=True, key=lambda x : x[-1])

# print(dict_map_freq)

rst = []
rst = [[key]*value for key,value in dict_map_freq]
    
    

print(rst)