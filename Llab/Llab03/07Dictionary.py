
dict_ = {
    "arm" : ["n", "แขน"],
    "hello" : ["v", "สวัสดี"],
    "beautiful" : ["adj", "สวย"],
    "toilet" : ["n", "ห้องน้ำ"],
    "kick" : ["v", "เตะ"],
    "handsome" : ["adj", "หล่อ"],
}

def call_fn(text, action):
    return dict_[text.lower()][action-1]


status = True
while status:
    input_text = input()
    if input_text == '0':
        status = False
        break
    if input_text not in dict_:
        print("Word not in dictionary.")
        continue
    
    action_input = int(input())
    while action_input not in [1,2]:
        if action_input not in [1,2]:
            print("Invalid option.")
        action_input = int(input())
    

    response = call_fn(input_text, action_input)
    print(response)
