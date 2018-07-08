

username = input("what is your name: ")
if len(username) >= 6:
    print("username is fine")
else:
    print("username must be 6 characters")

print("Your name is %s" % username)

age = input("what is your age: ")
print("Your age is", age)
month = input("what month were you born: ")
print("You were born in %s" % month)

mylist = ["Tom", "Susan", "Sandra", "Brenda", 500]

print(mylist)

for item in mylist:
    if type(item) == int:
        product = item * 10
        print("finally found a number", product)
    else:
        print("It's not a number, it's a sibbling", item)

        

