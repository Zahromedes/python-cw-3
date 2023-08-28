# write your code here
Favorite_animals = ["cats", "dogs", "birds", "rabbits"]
print(Favorite_animals)

print (Favorite_animals[2])

Favorite_animals.remove( "birds")
print(Favorite_animals)

Favorite_animals.append("monkeys")
print(Favorite_animals)

for animal in Favorite_animals:
    print(f"I love {animal}" )

Numbers = [1,2,3,4,5]
Numbers_sum = 0

for num in Numbers:
    Numbers_sum = Numbers_sum +num
print(Numbers_sum)