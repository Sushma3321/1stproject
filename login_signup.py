import json
def register():
    username=input("enter the user name:")
    list=[]
    dic={}
    d={}
    s={}
    a="hello my name is",username
    s["descriprtion"]=a
    
    dic["user"]=list

    password=input("enter the password:")
    if len(password)>=6:
        if "@"  in password or "#" in password or "$" in password:
            pass_word=input("enter the conform password:")
            if password==pass_word:
                d["username"]=username
                d["password"]=password
                d["profile"]=s
                list.append(d)
                dob=input("enter the date of birth:")
                hobbies=input("enter the habbies:")
                gender=input("enter the gender:")
                s["dob"]=dob
                s["hobbies"]=hobbies
                s["gender"]=gender
                with open("database.json","w") as f:
                    json.dump(dic,f,indent=8)
                   
                    
                    print("congrats sushma you are signup sucessfully")      
            else:
                    print("password is not match")
                    register() 
        else:
                print("password must have special charecter")
                register() 
    else:
            print("password should be atleast 6 characters")
            register() 
            
def login():
    with open("database.json","r")as file:
        a=json.load(file)
        username=input("enter the name:")
        password=input("enter the password:")
        if a["user"][0]["username"]==username and a["user"][0]["password"]==password:
        
            print('you are login succesfull')
        else:
            print("you are details is wrong")
    
print("login or register")
user=input("enter what do you want")
if user=="register":
    register()
elif user=="login":
   login()   

