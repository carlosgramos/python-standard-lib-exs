#There are several ways to format strings in python:
#We want to display the message 'Hey Bob, ther is a )xbadc0ffee error!'

errno = 50159747054
name = 'Bob'

####Positional formatting -> % operator
print('Hello, %s' % name)
print('%x' % errno)

#If you have more than one argument for the % operator, pass them as a tuple
# print('Hey %s, there is a 0x%x error!') % (name, errno)

#You can also pass a dicitonary to the % operator
print('Hey %(name)s, there is a 0x%(errno)x error!' % {"name":name, "errno":errno})

####String literals -> .format()
#Using string literals, .format(), on a string object
print('Hello, {}'.format(name))

#Or refer to variable substitutions by name, making it easy to change the values in the future.
#Also, notice you need to pass a format spec by adding a :x suffix.
print('Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno))

####Formatted strings -> f'string'
#Using formatted strings, f-strings
print(f'Hello, {name}!')

#Formatted strings allow you to imbed python expressions inside the string
a = 5
b = 10

print(f'Five plus ten is {a + b} and not {2 * (a + b)}')

#f-string inside a function
def greet(name, question):
    return f"Hello, {name}, how's it {question}?"
    
print(greet('Bob', 'going'))

#Deconstructing the function
import dis

dis.dis(greet)

#String literals support the existing format string syntax
#Notice the passing of the :#x suffix
print(f"Hey {name}, there's a {errno:#x} error!")

####Template Strings (standard library)
from string import Template

t = Template('Hey, $name!')
print(t.substitute(name=name))

#The Template class does not support format specifiers,
#so you need to manually transform the errno into a hex-string
templ_string = 'Hey $name, there is a $error!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))

#Formatting mini languages can create security vulnerabilities
SECRET = 'this-is-a-secret'

class Error:
    def __init__(self):
        pass
    
#Malicious user can craft a format string that can read data from the global namespace:
user_input = '{error.__init__.__globals__[SECRET]}'

err = Error()
print(user_input.format(error=err))

#Use Template strings when capturing user input in order to close the attack vector
print(Template(user_input).substitute(error=err))

#Python String Formatting Rule of Thumb: If your format strings are user-supplied, 
#use Template Strings (#4) to avoid security issues. Otherwise, use 
#Literal String Interpolation/f-Strings (#3) if you’re on Python 3.6+, and “New Style” 
#str.format (#2) if you’re not.
