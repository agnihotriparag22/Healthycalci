import excercises
import diet

# This function consist of remedies for various categories based on BMI

def for_underweight(name): 
    '''This function suggest you diet and excercise plan''' 
    print("How much weight do you want to gain in one week:\n1. 0.5kg\n2. 1kg\n")
    while True:
        while True:
            try:
                option=int(input("Choose one option: "))
                break
            except:
                print("Invalid input")
        if option==1 or option==2:
            match option:
                case 1:
                    print("\nIn order to gain 0.5kg weight in a week, You should follow the plan below\n")
                    diet.for_underweight_half(name)
                    excercises.for_underweight_half(name)
                    break
                case 2:
                    print("\nIn order to gain 1kg weight in a week, You should follow the plan below\n")
                    diet.for_underweight_one(name)
                    excercises.for_underweight_one(name)
                    break
        else:
            print("\nChoose again...\n")
            break

def for_healthy(name):
    '''This function suggest you diet and excercise plan'''
    print("Yayy! You are Fit. Here are some suggestions for you to maintain your health:\n")
    diet.for_healthy(name)
    excercises.for_healthy(name)

def for_overweight(name):
    '''This function suggest you diet and excercise plan'''
    print("How much weight do you want to loose in one week:\n1. 0.5kg\n2. 1kg\n")
    while True:
        while True:
            try:
                option=int(input("Choose one option: "))
                break
            except:
                print("Invalid input")
        if option==1 or option==2:
            match option:
                case 1:
                    print("\nIn order to loose 0.5kg weight in a week, You should follow the plan below\n")
                    diet.for_overweight_half(name)
                    excercises.for_overweight_half(name)
                    break
                case 2:
                    print("\nIn order to gain 1kg weight in a week, You should follow the plan below\n")
                    diet.for_overweight_one(name)
                    excercises.for_overweight_one(name)
                    break
        else:
            print("\nChoose again...\n")
            break
    
def for_obese(name):
    '''This function suggest you diet and excercise plan'''
    print("You fall under the category of Obesity. You should follow a strict diet and a proper training schedule.\nHere are some suggestions:\n\n")
    excercises.for_obese(name)
    diet.for_obese(name)
