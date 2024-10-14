import calculate
import fileop
# This module consist of a funciton which shows the type of diet you are on
    # input = Calorie intake and Calorie burn
    # output = Tyep of diet(Deficit/Surplus) 

def show(name):
    '''This function decided whether you are on calorie deficit or surplus'''
    print("\nNow let's calculate your daily calorie intake")
    intake=calculate.intake(name)

    print("\nLet's see how much calories you burn daily")
    burn=calculate.burn(name)

    result=intake-burn
    if result>0:
        print("You are on calorie surplus\n")
        with open(fileop.get_path(name),'a') as f:
            f.write("\nResult: You are on a calorie surplus diet\n")
            f.write("----------------------------------------------------------------------\n")
    else:
        print("You are on calorie deficit\n")
        with open(fileop.get_path(name),'a') as f:
            f.write("\nResult: You are on a calorie deficit diet\n")
            f.write("----------------------------------------------------------------------\n")