import json

def stratup_msg():
    #NOTE: dont use this for large numbers of profiles!
    with open 
        print("This dictionary contains the birthdays of:")
        for i in f:
            print(i)
    
while True:
    action = input("would you like to view or add entries? ")

    #update members from file
    with open("twice_info.json", "r") as f:
        members = json.load(f)
    
    
    if action == "view":
        try:
            qry = input("Enter a name to find birthday: ").capitalize()
            print("{name}'s birthday is {date}.".format(name=qry,
                                                        date=members[qry]))
        except KeyError:
            print("Sorry, we can't find that name. Try again.")
                
    elif action == "add":
        name = input("Enter member name:").capitalize()
        birthday = input("Enter the birthday (d/m/yyyy):")
        members2[name] = birthday

        with open("twice_info.json", "w") as f:
            try:
                json.dump(members2,f)
            except:
                json.dump(members,f)
                print("error in writing. reverted to original")
                

   


