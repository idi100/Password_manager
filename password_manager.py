

def view():
    with open('passwords.txt','r') as f:
         for line in f.readlines():
              data = line.rstrip()
              user, passw = data.split("|")
              print("User: ", user, "| Password: ", passw)


def add():
        name = input("Account Name: ")
        pwd = input("Passwords: ")
        with open('passwords.txt','a') as f:
             f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add), press q to quit: \n\n\nImportant: add a password before viewing: ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid")
        continue
