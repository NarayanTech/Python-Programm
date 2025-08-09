print("Love")
boy_name = input("Boy Name: ")
boy_age = int(input("Boy Age: "))
girl_name = input("Girl Name: ")
girl_age = int(input("Boy Age: "))

'''
this 
is 
a 
multi line command
''' # [''' coats are use to for Showing Multiline Commends]
# using abs because Somtime boy might be Younger [#]is used for Showing a Single Line Commmand 
age_diff =  abs(boy_age - girl_age)
print(boy_name + " Loves " + girl_name  + ". Age Difference is " +  str(age_diff))
print(f"{boy_name} loves {girl_name}. Age Difference is {age_diff}")