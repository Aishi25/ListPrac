hobbies = ["Playing soccer", "Reading a book", "Annoying sibling", "Listening to music", "Working with technology"]
print("My hobbies \n")

hobbies.append("Drawing")
hobbies.append("Coloring")
hobbies.append("Biking")
for i in range(len(hobbies)):
  print(hobbies[i])

print("\n")
print("\n")

import random
number = []
sum = 0
for i in range(5):
  number.append(random.randint(1,100))
  sum = sum + number[i]
print(sum)
avg = sum/len(number)
print("Average is " + str(avg))
