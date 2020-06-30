#Areas of Rectangles
#6/30/2020
#Jessica Forbes

#Dimensions of rectangle 1
length1 = int(input("Enter the length of the first rectangle: "))
width1 = int(input("Enter the width of the first rectangle: "))


#Get the dimensions of rectangle 2
length2 = int(input("Enter the length of the second rectangle: "))
width2 = int(input("Enter the width of the second rectangle: "))


#Calculate the areas of the rectangles
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greater area.
if area1 > area2:
    print("Rectangle 1 has the greater area.")
elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("Both have the same area.")
