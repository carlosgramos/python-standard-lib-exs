#Accessing a value in a list
bicycles = ['trek', 'cannondale', 'huffy', 'redline']
message = "My first bicycle was a " + bicycles[1].title() + "."
print(message)

#Changing values
motorcycles = ['ducati', 'honda', 'harley']
motorcycles[0] = 'suzuki'
print(motorcycles)

#Appending values
motorcycles.append('kawasaki')
print(motorcycles)

#Inserting values
motorcycles.insert(5, 'yamaha')
print(motorcycles)

#Deleting values
del motorcycles[4]
print(motorcycles)

#Popping a value
popped_bike = motorcycles.pop()
print(popped_bike)
print(motorcycles)

#Removing an item by value
motorcycles.remove('harley')
print(motorcycles)

#Sort list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Iterate through items in list using for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
#Doing work inside the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    
#Using range to create a list of numbers
num_list = list(range(1, 10))
print(num_list)