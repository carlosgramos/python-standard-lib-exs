#The get() method on dict and it's default argument which will be returned if a 
#certain value is not found

name_for_user_id = {
    322: "Alice",
    346: "Bob",
    278: "Jill"
}

#If the userid is not found, the default "Hi there!" will be displayed
def greeting(userid):
    return "Hi %s!" % name_for_user_id.get(userid, "there")

print(greeting(322))
print(greeting(55555))