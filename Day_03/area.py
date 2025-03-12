def find_area():
    shape = str(input("Enter the shape, You want to find the area of:"))
    if shape.lower() == "rectangle" :
        a,b = map(float, input("Enter the lenght and width:").split(','))
        area = a*b
        print(f"Area of given Rectangle is:{round(area,2)}")
    elif  shape.lower() == "circle":
        rad = float(input("Enter the radius of circle:"))
        area = float(3.14*rad*rad)
        print(f"Area of given circle is:{round(area,2)}")
    else:
        print("Invalid Shape")
find_area()