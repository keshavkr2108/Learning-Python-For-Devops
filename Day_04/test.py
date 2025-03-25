name = input("Enter Your Name:")
username = input("Enter User ID:")
password = input("Enter Password:")
gen = str(input("Your Gender:"))
if gen == "male":
    print("Hello Mr. " + name )
elif gen == "female":
    print("Hello Mrs. " + name )
else:
    print("Please Enter your Gender:")