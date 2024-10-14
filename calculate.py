import menu
import fileop
#This module consists of functions for calorie calculation

#The intake function calculates the calorie intake of a person
    # input = Food items
    # output = Total calorie intake
#The burn function calculate the calories burned by a person
    # input = Excercise + Duration
    # output = Total calories burned
def intake(name):
    '''This function calculates the total calories intake of a person based on their diet'''
    calories=0
    menu.show_diet()
    while True:
        while True:
            try:
                option=abs(int(input("Add items: ")))
                break
            except:
                print("Invalid Input")
        match option:
            case 1:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=200*quantity
            case 2:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=120*quantity
            case 3:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=90*quantity
            case 4:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=250*quantity
            case 5:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=120*quantity
            case 6:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")                 
                calories+=175*quantity
            case 7:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=80*quantity
            case 8:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=100*quantity
            case 9:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")          
                calories+=75*quantity
            case 10:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=200*quantity
            case 11:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input") 
                calories+=200*quantity
            case 12:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=350*quantity
            case 13:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=250*quantity
            case 14:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=350*quantity
            case 15:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=200*quantity
            case 16:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=200*quantity
            case 17:
                while True:
                    try:
                        quantity=abs(int(input("Enter the quantity: ")))
                        break
                    except:
                        print("Invalid Input")
                calories+=100*quantity
            case 18:
                menu.show_diet()
            case 0:
                break
    
    print(f"\nYour total calorie intake(per day) is: {calories}")

    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie intake(per day): {calories} calories\n")

    return calories

def burn(name):
    '''This function calculates the calories burned by a person'''
    calories=0
    total_time=60.0
    menu.show_excercises()
    while True:
        while True:
            try:
                option=int(input("Add items: "))
                break
            except:
                print("Invalid Input")
        match option:
            case 1:
                print("\nWalking")
                
                print(f"Total time: {total_time} minutes\n")
                if total_time>0:
                    while True:
                        try:
                            time=abs(float(input("How much time do you spend: ")))
                            break
                        except:
                            print("Invalid Input")
                    if time<=total_time:
                        total_time-=time
                        cal=time*5
                        calories+=cal
                        print(f"You have {total_time} minutes left")
                    else:
                        print("You don't have enough time left to excercise")
                else:
                    print("You don't have enough time to excercise")                   
            case 2:
                print("\nRunning")
               
                print(f"Total time: {total_time} minutes\n")
                if total_time>0:
                    while True:
                        try:
                            time=abs(float(input("How much time do you spend: ")))
                            break
                        except:
                            print("Invalid Input")
                    if time<=total_time:
                        total_time-=time
                        cal=time*15.6
                        calories+=cal
                        print(f"You have {total_time} minutes left")
                    else:
                        print("You don't have enough time left to excercise")
                else:
                    print("You don't have enough time to excercise")                   
            case 3:
                print("\nSwimming")
            
                print(f"Total time: {total_time} minutes\n")
                if total_time>0:
                    while True:
                        try:
                            time=abs(float(input("How much time do you spend: ")))
                            break
                        except:
                            print("Invalid Input")
                    if time<=total_time:
                        total_time-=time
                        cal=time*10.8
                        calories+=cal
                        print(f"You have {total_time} minutes left")
                    else:
                        print("You don't have enough time left to excercise")
                else:
                    print("You don't have enough time to excercise")             
            case 4:
                print("\nYoga")
                print(f"Total time: {total_time} minutes\n")
                if total_time>0:
                    while True:
                        try:
                            time=abs(float(input("How much time do you spend: ")))
                            break
                        except:
                            print("Invalid Input")
                    if time<=total_time:
                        total_time-=time
                        cal=time*6.6
                        calories+=cal
                        print(f"You have {total_time} minutes left")
                    else:
                        print("You don't have enough time left to excercise")
                else:
                    print("You don't have enough time to excercise")
            case 0:
                break
    print(f"\nYou burned {calories} calories in a day\n")

    with open(fileop.get_path(name),'a') as f:
        f.write(f"Total calorie Burn(per day): {calories} calories\n")
        
    return calories