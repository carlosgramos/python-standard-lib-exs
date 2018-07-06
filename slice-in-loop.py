# You can use a slice in a for loop if you want to loop through a subset of
# the elements in a list. In the next example we loop through the first three
# players and print their names as part of a simple roster:

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
#Use slice to find the top three scores for player 1. 
#Add the latest score first
p1_game_scores = [56, 78, 90, 34, 87, 98]
print(p1_game_scores)
p1_latest_score = 101

p1_game_scores.append(p1_latest_score)
print(sorted(p1_game_scores)[-3:])

#Making a copy of a list using the slice method
list_1 = [1, 2, 3, 4]
list_2 = list_1[:]

print("Original list: ")
print(list_1)
print("Copied list: ")
print(list_2)

print("The two lists are different...here are their id's:")
print(id(list_1))
print(id(list_2))

#When my friend likes my food
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)




