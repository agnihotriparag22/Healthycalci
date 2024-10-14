#This module consists of the diet charts for various set of people
import fileop
def for_underweight_half(name):
    '''This function suggest you a diet plan'''

    diet={"Roti(6)":600,"Dal/Rice Bowl":350,"Brown Bread(2)":150,"Paneer(50gm)":125,"Oats":175,"Banana Shake(1 Glass)":200,"Salad(300gm)":90,"Sprouts Bowl(200gm)":250,"Curd(1 Cup)":200,"Boiled Potatoes(250gm)":200,"Vegetable curry":200}

    count=1
    print("\n\t\tDIET CHART\n")

    with open(fileop.get_path(name),'a') as f:
        f.write("\n\t\tDIET CHART\n")

    total=sum(list(diet.values()))
    print("S.No\tFOOD\t\t\t\t\tCALORIES")

    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tFOOD\t\t\t\t\tCALORIES\n")
    
    for key,value in sorted(diet.items()):
        if key=="Oats" or key=="Roti(6)":
            print(f"{count}.\t{key}\t\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t\t {value}\n")

        elif key=="Boiled Potatoes(250gm)" or key=="Banana Shake(1 Glass)" or key=="Sprouts Bowl(200gm)":
            print(f"{count}.\t{key}\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t {value}\n")

        else:
            print(f"{count}.\t{key}\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t {value}\n")
        count+=1

    print(f"\nTotal calorie intake: {total}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie intake: {total}\n")

def for_underweight_one(name):
    '''This function suggest you a diet plan'''
    diet={"Roti(8)":800,"Dal/Rice Bowl":350,"Brown Bread(3)":350,"Paneer(100gm)":250,"Oats":175,"Banana Shake(1 Glass)":200,"Salad(300gm)":90,"Sprouts Bowl(200gm)":250,"Curd(1 Cup)":200,"Boiled Potatoes(400gm)":320,"Vegetable curry":200}

    count=1
    print("\n\t\tDIET CHART")
    with open(fileop.get_path(name),'a') as f:
        f.write("\t\tDIET CHART\n")

    total=sum(list(diet.values()))
    print("S.No\tFOOD\t\t\t\t\tCALORIES")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tFOOD\t\t\t\t\tCALORIES\n")

    for key,value in sorted(diet.items()):
        if key=="Oats" or key=="Roti(8)":
            print(f"{count}.\t{key}\t\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t\t {value}\n")

        elif key=="Boiled Potatoes(400gm)" or key=="Banana Shake(1 Glass)" or key=="Sprouts Bowl(200gm)":
            print(f"{count}.\t{key}\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t {value}\n")

        else:
            print(f"{count}.\t{key}\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t {value}\n")
        count+=1

    print(f"\nTotal calorie intake: {total}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie intake: {total}\n")

def for_overweight_half(name):
    '''This function suggest you a diet plan'''

    diet={"Roti(8)":800,"Brown Bread(4)":350,"Paneer(100gm)":250,"Oats":175,"Salad(300gm)":90,"Sprouts Bowl(200gm)":250,"Curd(1/2 Cup)":100,"Vegetable curry":200,"Brown Rice(1 Bowl)":200}

    count=1
    print("\n\t\tDIET CHART")
    with open(fileop.get_path(name),'a') as f:
        f.write("\t\tDIET CHART\n")

    total=sum(list(diet.values()))
    print("S.No\tFOOD\t\t\t\t\tCALORIES")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tFOOD\t\t\t\t\tCALORIES\n")

    for key,value in sorted(diet.items()):
        if key=="Oats" or key=="Roti(8)":
            print(f"{count}.\t{key}\t\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t\t {value}\n")

        elif key=="Boiled Potatoes(250gm)" or key=="Banana Shake(1 Glass)" or key=="Sprouts Bowl(200gm)" or key=="Brown Rice(1 Bowl)":
            print(f"{count}.\t{key}\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t {value}\n")

        else:
            print(f"{count}.\t{key}\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t {value}\n")

        count+=1
    print(f"\nTotal calorie intake: {total}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie intake: {total}\n")

def for_overweight_one(name):
    '''This function suggest you a diet plan'''
    diet={"Roti(6)":600,"Brown Bread(2)":150,"Paneer(50gm)":125,"Oats":175,"Salad(300gm)":90,"Sprouts Bowl(200gm)":250,"Curd(1/2 Cup)":100,"Vegetable curry":200,"Brown Rice(1 Bowl)":200}

    count=1
    print("\n\t\tDIET CHART")
    with open(fileop.get_path(name),'a') as f:
        f.write("\t\tDIET CHART\n")

    total=sum(list(diet.values()))
    print("S.No\tFOOD\t\t\t\t\tCALORIES")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tFOOD\t\t\t\t\tCALORIES\n")

    for key,value in sorted(diet.items()):
        if key=="Oats" or key=="Roti(6)":
            print(f"{count}.\t{key}\t\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t\t {value}\n")

        elif key=="Boiled Potatoes(250gm)" or key=="Banana Shake(1 Glass)" or key=="Sprouts Bowl(200gm)" or key=="Brown Rice(1 Bowl)":
            print(f"{count}.\t{key}\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t {value}\n")

        else:
            print(f"{count}.\t{key}\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t {value}\n")
        count+=1

    print(f"\nTotal calorie intake: {total}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie intake: {total}\n")

#Correct alignment in this table
def for_healthy(name):
    '''This function suggest you a diet plan'''
    diet={"Roti(8)":800,"Brown Bread(2)":150,"Paneer(100gm)":250,"Oats":175,"Fruit Juice(1 Glass)":120,"Salad(300gm)":90,"Sprouts Bowl(100gm)":125,"Curd(1/2 Cup)":100,"Vegetable curry":200,"Fruit Bowl":120,"Brown Rice(1 Bowl)":200}

    count=1
    print("\n\t\tDIET CHART")
    with open(fileop.get_path(name),'a') as f:
        f.write("\t\tDIET CHART\n")

    total=sum(list(diet.values()))
    print("S.No\tFOOD\t\t\tCALORIES")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tFOOD\t\t\tCALORIES\n")

    for key,value in sorted(diet.items()):
        if key=="Oats" or key=="Roti(8)":
            print(f"{count}.\t{key}\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t {value}\n")

        elif key=="Sprouts Bowl(100gm)" or key=="Brown Rice(1 Bowl)" or "Fruit Juice(1 Glass)":
            print(f"{count}.\t{key}\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t {value}\n")

        else:
            print(f"{count}.\t{key}\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t {value}\n")

        count+=1
    print(f"\nTotal calorie intake: {total}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie intake: {total}\n")
        
#Correct alignment in this table
def for_obese(name):
    '''This function suggest you a diet plan'''
    diet={"Roti(6)":600,"Paneer(100gm)":250,"Oats":175,"Salad(1 Bowl)":90,"Sprouts Bowl(200gm)":250,"Curd(1/2 Cup)":100,"Vegetable curry":200,"Brown Rice(1 Bowl)":200}

    count=1
    print("\n\t\tDIET CHART")
    with open(fileop.get_path(name),'a') as f:
        f.write("\t\tDIET CHART\n")

    total=sum(list(diet.values()))
    print("S.No\tFOOD\t\t\t\tCALORIES")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tFOOD\t\t\t\tCALORIES\n")

    for key,value in sorted(diet.items()):
        if key=="Oats" or key=="Roti(6)":
            print(f"{count}.\t{key}\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t {value}\n")

        elif key=="Sprouts Bowl(200gm)" or key=="Brown Rice(1 Bowl)" or "Fruit Juice(1 Glass)" or key=="Brown Bread(2)":
            print(f"{count}.\t{key}\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t {value}\n")

        else:
            print(f"{count}.\t{key}\t\t\t\t {value}")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}.\t{key}\t\t\t\t {value}\n")

        count+=1
    print(f"\nTotal calorie intake: {total}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie intake: {total}\n")