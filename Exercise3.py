
#exercise 3.1
red_objects= {'apple', 'crab', 'rose', 'strawberry'}
fruits= {'orange', 'apple', 'strawberry', 'grape', 'kiwi', 'mandarin'}

red_fruit=fruits.intersection(red_objects)
print(red_fruit)


clour_fruit = fruits.difference(red_objects)
print(clour_fruit)

# exercise 3.2
orange_objects = {"basketball", "fanta", "orange","autumn" "leaves", "mandarin"}

orange_fruit = fruits.intersection(orange_objects)
orange_red_fruit = red_fruit.union(orange_fruit)
print(orange_red_fruit)
differ_fruit = (red_objects.difference(fruits)).union(orange_objects.difference(fruits))
print(differ_fruit)

# exercise3.3

all_object = list((red_objects.union(fruits)).union(orange_objects))
print(all_object)