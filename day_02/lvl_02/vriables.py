# Day2:30 Days of python programming

# declaring variables
first_name = "Saleh"
last_name = "Sadeqi"
full_name = first_name + last_name
country = "Iran"
city = "Tehran"
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = True
is_tired, is_employed, is_determined = True, False, True

# using built-in type() to find types
print("first name data type: ", type(first_name))
print("last name data type : ", type(last_name))
print("full name data types : ", type(full_name))
print("country data type", type(country))
print("city data type : ", type(city))
print("age data type : ", type(age))
print("year data type : ", type(year))
print("married situation data type : ", type(is_married))
print("true situation data type : ", type(is_true))
print("light situation data type : ", type(is_light_on))
print("tiredness, job and hope situation data type : ", type(is_tired), type(is_employed) , type(is_determined))

# using len() function 
print(len(first_name))
print(f"my first name length is {len(first_name)} and my last name length is {len(last_name)}")

# calculation using varibales
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# circle
circle_radius = 30
area_of_circle = 3.14 * circle_radius ** 2
circum_of_circle = 2 * 3.14 * circle_radius

# defining permenantn solution to are of circle
def circle_area(radius) :
    return 3.14 * (radius ** 2)

# getting input from user
user_circle_radius = float(input("enter a number for radius of a circle in order to know it's area : "))
print(circle_area(user_circle_radius))


# getting user data via input() function 

user_first_name = input("first name : ")
user_last_name = input("last name : ")
user_country = input("country : ")
user_age = int(input("age : "))
