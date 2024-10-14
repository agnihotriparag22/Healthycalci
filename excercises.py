#This module consists of a set of exercises for various set of people
import fileop
def for_underweight_half(name):
    '''This function suggest you an excercise plan'''
    exercises={"Walking":[50,10],"Running":[116,10],"Swimming":[108,10],"Yoga":[200,30]}
    cal=list(exercises.values())
    count=1
    cal_count=0
    i=0
    print("\n\tSUGGESTED EXERCISES")
    with open(fileop.get_path(name),'a') as f:
        f.write("----------------------------------------------------------------------\n")
        f.write("\tSUGGESTED EXERCISES\n")
    print("S.No\tExercise\tDuration")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tExercise\tDuration\n")
    for x in exercises.keys():
        if x=="Swimming":
            print(f"{count}\t{x}\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
        else:
            print(f"{count}\t{x}\t\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
    print(f"\nTotal calorie burn: {cal_count}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie burn: {cal_count}\n")

def for_underweight_one(name):
    '''This function suggest you an excercise plan'''
    exercises={"Walking":[25,5],"Running":[58,5],"Swimming":[108,10],"Yoga":[266,40]}
    cal=list(exercises.values())
    count=1
    cal_count=0
    i=0
    print("\n\tSUGGESTED EXERCISES")
    with open(fileop.get_path(name),'a') as f:
        f.write("----------------------------------------------------------------------\n")
        f.write("\tSUGGESTED EXERCISES\n")
    print("S.No\tExercise\tDuration")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tExercise\tDuration\n")
    for x in exercises.keys():
        if x=="Swimming":
            print(f"{count}\t{x}\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
        else:
            print(f"{count}\t{x}\t\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
    print(f"\nTotal calorie burn: {cal_count}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie burn: {cal_count}\n")

def for_overweight_half(name):
    '''This function suggest you an excercise plan'''
    exercises={"Walking":[50,10],"Running":[175,15],"Swimming":[162,15],"Yoga":[133,20]}
    cal=list(exercises.values())
    count=1
    cal_count=0
    i=0
    print("\n\tSUGGESTED EXERCISES")
    with open(fileop.get_path(name),'a') as f:
        f.write("----------------------------------------------------------------------\n")
        f.write("\tSUGGESTED EXERCISES\n")
    print("S.No\tExercise\tDuration")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tExercise\tDuration\n")
    for x in exercises.keys():
        if x=="Swimming":
            print(f"{count}\t{x}\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
        else:
            print(f"{count}\t{x}\t\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
    print(f"\nTotal calorie burn: {cal_count}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie burn: {cal_count}\n")

def for_overweight_one(name):
    '''This function suggest you an excercise plan'''
    exercises={"Walking":[50,10],"Running":[232,20],"Swimming":[216,20],"Yoga":[66,10]}
    cal=list(exercises.values())
    count=1
    cal_count=0
    i=0
    print("\n\tSUGGESTED EXERCISES")
    with open(fileop.get_path(name),'a') as f:
        f.write("----------------------------------------------------------------------\n")
        f.write("\tSUGGESTED EXERCISES\n")
    print("S.No\tExercise\tDuration")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tExercise\tDuration\n")
    for x in exercises.keys():
        if x=="Swimming":
            print(f"{count}\t{x}\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
        else:
            print(f"{count}\t{x}\t\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
    print(f"\nTotal calorie burn: {cal_count}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie burn: {cal_count}\n")

def for_healthy(name):
    '''This function suggest you an excercise plan'''
    exercises={"Walking":[100,20],"Running":[115,10],"Swimming":[162,15],"Yoga":[100,15]}
    cal=list(exercises.values())
    count=1
    cal_count=0
    i=0
    print("\n\tSUGGESTED EXERCISES")
    with open(fileop.get_path(name),'a') as f:
        f.write("----------------------------------------------------------------------\n")
        f.write("\tSUGGESTED EXERCISES\n")
    print("S.No\tExercise\tDuration")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tExercise\tDuration\n")
    for x in exercises.keys():
        if x=="Swimming":
            print(f"{count}\t{x}\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
        else:
            print(f"{count}\t{x}\t\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
    print(f"\nTotal calorie burn: {cal_count}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie burn: {cal_count}\n")

def for_obese(name):
    '''This function suggest you an excercise plan'''
    exercises={"Walking":[100,20],"Running":[175,15],"Swimming":[162,15],"Yoga":[66,10]}
    cal=list(exercises.values())
    count=1
    cal_count=0
    i=0
    print("\n\tSUGGESTED EXERCISES")
    with open(fileop.get_path(name),'a') as f:
        f.write("----------------------------------------------------------------------\n")
        f.write("\tSUGGESTED EXERCISES\n")
    print("S.No\tExercise\tDuration")
    with open(fileop.get_path(name),'a') as f:
        f.write("S.No\tExercise\tDuration\n")
    for x in exercises.keys():
        if x=="Swimming":
            print(f"{count}\t{x}\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
        else:
            print(f"{count}\t{x}\t\t{cal[i][1]} min")
            with open(fileop.get_path(name),'a') as f:
                f.write(f"{count}\t{x}\t\t{cal[i][1]} min\n")
            cal_count+=cal[i][0]
            count+=1
            i+=1
    print(f"\nTotal calorie burn: {cal_count}")
    with open(fileop.get_path(name),'a') as f:
        f.write(f"\nTotal calorie burn: {cal_count}\n")    