def lbs_to_kg(weight):
    '''This function converts the weight from pounds to kilograms'''
    in_kg=weight*0.453592
    print(f"Your weight in kg: {format(weight*0.453592,".2f")}")
    return in_kg

def ft_to_mtr(height_ft,height_in):
    '''This function converts height in feets to meters'''
    total_in_inch=height_ft*12+height_in
    in_mtr=total_in_inch*0.0254
    print(f"Your height in mtr: {format(total_in_inch*0.0254,".2f")}")
    return in_mtr

def cm_to_mtr(height):
    '''This function converts the height in centimeters to meters'''
    in_mtr=height/100
    print(f"Your height in mtr: {format(height/100,'.2f')}")
    return in_mtr
