patience = 3
password = "mysecretkey"
status = "fail"

for i in range(patience):
    print("Hello, welcome to KU68 banking system.")
    key= input("Enter your secret key: ").strip()
    if key == password:
        print("You entered the correct secret key, congrat..")
        status='success'
        break
    if i == patience-1:
        break
    print("""You entered the wrong secret key!
Sorry, we cannot let you in..
Do please try again.
""")
    
if status == "fail":
    print("""You entered the wrong secret key!
Sorry, we cannot let you in..
You mis-entered too much times the secret key!
bye""")