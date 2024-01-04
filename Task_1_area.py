
# Task 1: Calculate Area with Conditions

def calculate_area(length,width):
    if length == width:
        return "This is a square!"
    else:
        return length*width

def enter_data():
    try:
        l = float(input('enter the length : '))
        w = float(input('enter the width : '))
        
        area = calculate_area(l,w)
        if type(area) == float:
            print('the area of rectangle is : ' , area)
        else:
            print(area)
    except:
        print('enter the correct dimention')

enter_data()