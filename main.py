import bmi
import remedies
import result
import os
import fileop

import datetime #Study more about this
# This is the main function of this program

def main():
    '''This is the main function of this application'''
    clear=lambda:os.system('cls')
    clear()
    date=datetime.date.today() #Study more about this
    day=date.strftime('%A') #Study more about this

    print("\t\tWELCOME TO HEALTHY-CALCI")
    
    while True:  
        name=input("\nEnter your full name: ").title()
        name_list=name.split(" ")
        try:
            with open(fileop.get_path(name),'w') as f:
                f.write("\n\t\t\tHEALTHYCALCI REPORT\n\n\n")
                f.write(f"Customer name: {name.title()}\n")
                f.write(f"Date: {date}\t\t\t\t\tDay: {day}\n")
                break
        except:
            print("Enter a valid name")

    print(f"\nHello {name_list[0]}, Let's calculate your Body Mass Index(BMI)")

    BMI=bmi.calculator(name)

    result.show(name) #This function will show if you are on deficit or surplus

    if 0<BMI<=18.5:
        print("\nAccording to your BMI, you are Underwight\n")
        with open(fileop.get_path(name),'a') as f:
            f.write("According to your BMI, you are Underwight\n\n")
        remedies.for_underweight(name)
    elif 18.5<BMI<=24.9:
        print("\nAccording to your BMI, you are Healthy\n")
        with open(fileop.get_path(name),'a') as f:
            f.write("According to your BMI, you are Healthy\n\n")
        remedies.for_healthy(name)
    elif 25<BMI<=29.9:
        print("\nAccording to your BMI, you are Overweight\n")
        with open(fileop.get_path(name),'a') as f:
            f.write("According to your BMI, you are Overwight\n\n")
        remedies.for_overweight(name)
    else:
        print("\nAccording to your BMI, you are Obese\n")
        with open(fileop.get_path(name),'a') as f:
            f.write("According to your BMI, you are Obese\n\n")
        remedies.for_obese(name)

    with open(fileop.get_path(name),'a') as f:
        f.write("----------------------------------------------------------------------\n")
        f.write("This is a system generated file, please do not try to overwrite it(Only for view)")

    print("----------------------------------------------------------------------------------\n")
    print("You can see your personalized calorie report on your computer's desktop")
    print("Please find a text file with your name\n\nfor example:\tname = yash tech\n\t\tfile name = Yash Tech.txt\n\a")
main()

#To-Do in this project
# add list of foods with calories of their standard unit
# add 