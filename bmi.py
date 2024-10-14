#This module consist of a funciton which calculate the BMI of a person
    # input = height + weight
    # output = BMI
import fileop
import convert
import menu
def calculator(name):
    '''This function calculates the Body Mass Index of a person.'''

    print("\nSelect the unit for weight: ")
    menu.show_weightunit()
    while True:
        try:
            option=int(input("Select one option: "))
            if option==1 or option==2:
                match option:
                    case 1:
                        while True:
                            try:
                                weight=float(input("\nEnter your weight(in kg): "))
                                if 25<weight<170:
                                    break
                                else:
                                    print("Enter valid weight")
                            except ValueError or TypeError:
                                print("\nInvalid weight. Try again...")
                    case 2:
                        while True:
                            try:
                                weight=float(input("\nEnter your weight(in lbs): "))
                                weight=convert.lbs_to_kg(weight)
                                if 25<weight<170:
                                    break
                                else:
                                    print("\nInvalid weight. Try again...")
                            except ValueError or TypeError:
                                print("Enter valid weight")
                break
            else:
                print("Invalid input. Try again...\n")
        except:
            print("Invalid input. Try again...\n")
    
    print("\nSelect the unit for height: ")
    menu.show_heightunit()
    while True:
        try:
            option=int(input("Select one option: "))
            if option==1 or option==2 or option==3:
                match option:
                    case 1:
                        while True:
                            try:
                                height=float(input("Enter your height(in mtr): "))
                                if 0.6<height<2.5:
                                    break
                                else:
                                    print("Invalid input. Try again...\n")
                            except ValueError or TypeError:
                                print("Invalid input. Try again...\n")
                    case 2:
                        while True:
                            try:#feet to mtr
                                height_ft=int(input("Enter feet: "))
                                if 1<=height_ft<=8:
                                    height_in=int(input("Enter inch: "))
                                    if 0<=height_in<=12:
                                        height=convert.ft_to_mtr(height_ft,height_in)
                                        if 0.6<height<2.5:
                                            break
                                        else:
                                            print("Invalid input. Try again...\n")
                                    else: print("Invalid input. Try again...\n")
                                else:
                                    print("Invalid input. Try again...\n")
                            except ValueError or TypeError:
                                print("Invalid input. Try again...\n")
                    case 3:
                        while True:
                            try:#cm to mtr
                                height=int(input("Please enter your height(in cm): "))
                                height=convert.cm_to_mtr(height)
                                if 0.6<height<2.5:
                                    break
                                else:
                                    print("Invalid input. Try again...\n")
                            except ValueError or TypeError:
                                print("Invalid input. Try again...\n")
                break
            else:
                print("Invalid input. Try again...\n")    
        except:
            print("Invalid input. Try again...\n")

    BMI=weight/(height**2)
    with open(fileop.get_path(name),'a') as f:
        f.write(f"Height: {format(height,'.2f')}mtr\t\t\t\t\t\tWeight: {format(weight,'.1f')}kg\n")
        f.write("----------------------------------------------------------------------")
    
    print("\n\t\t\t\tBMI RANGE \n")
    with open(fileop.get_path(name),'a') as f:
        f.write("\n\t\t\t\tBMI RANGE \n\n")

    print("\tUnderweight\tHealthy-weight\tOverweight\tObesity\n\n\tBelow 18.5\t18.5-24.9\t25.0-29.9\t30.0 or higher")
    with open(fileop.get_path(name),'a') as f:
        f.write("\tUnderweight\tHealthy-weight\tOverweight\tObesity\n\n\tBelow 18.5\t18.5-24.9\t25.0-29.9\t30.0 or higher")

    print("\nYour BMI is: ", format(BMI,'.2f'))
    two_dec=format(BMI,'.2f')
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\n\nYour BMI is: {two_dec}")
        f.write("\n----------------------------------------------------------------------")
    return BMI
