#bank account 
#create 
#withdraw
#deposit
#transfer
#show
#exit

bankaccount = dict()
while True:
    input_txt = input("BANK >>> ")
    if input_txt == "exit":
        break

    command = input_txt.split(" ")[0]

    match command:
        case "create":
            name, amount = input_txt.split(" ")[1:]
            amount = int(amount)
            if name in bankaccount:
                print(f"The Account '{name}' is exist")
                continue
            if amount < 0:
                print("Can't create with negative numbers")
                continue
            bankaccount[name] = amount

        case "withdraw":
            name, amount = input_txt.split(" ")[1:]
            amount = int(amount)
            if name not in bankaccount:
                print(f"The Account '{name}' is not exist")
                continue
            if amount < 0:
                print("Can't withdraw with negative numbers")
                continue
            if bankaccount[name] < amount:
                print(f"Insufficient balance in accout. Current balance : {bankaccount[name]}")
                continue
            bankaccount[name] -= amount

        case "deposit":
            name, amount = input_txt.split(" ")[1:]
            amount = int(amount)
            if name not in bankaccount:
                print(f"The Account '{name}' is not exist")
                continue
            if amount < 0:
                print("Can't deposit with negative numbers")
                continue
            
            bankaccount[name] += amount


        case "transfer":
            sender, receiver, amount = input_txt.split(" ")[1:]
            amount = int(amount)
            if sender not in bankaccount:
                print(f"The Account '{sender}' is not exist")
                continue

            if receiver not in bankaccount:
                print(f"The Account '{receiver}' is not exist")
                continue

            if amount < 0:
                print("Can't transfer with negative numbers")
                continue
            
            if bankaccount[sender] < amount:
                print(f"Insufficient balance in accout. Current balance : {bankaccount[sender]}")
                continue

            bankaccount[sender] -= amount
            bankaccount[receiver] += amount

        case "show":
            name = input_txt.split(" ")[1]
            if name not in bankaccount:
                print("Account is not exist")
                continue

            print(f"{name} is account : {bankaccount[name]}")

        case _:
            print("something went wrong")
