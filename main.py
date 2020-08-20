hobbies = ["Playing soccer", "Reading a book", "Annoying sibling", "Listening to music", "Working with technology"]
print("My hobbies")

hobbies.append("Drawing")
hobbies.append("Coloring")
hobbies.append("Biking")
for i in range(len(hobbies)):
  print(hobbies[i])


print("\n")

import random
number = []
sum = 0
for i in range(3):
  number.append(random.randint(1,100))
  sum = sum + number[i]
print(sum)
avg = sum/len(number)
print("Average is " + str(avg))

print("\n")

import random
number = []
lar = 0
for i in range(3):
  number.append(random.randint(1,10))
  print(number[i])

  if (number[i] > lar):
    lar = number[i]
print("Largest number:" +str(lar))


print("\n")

name = []
while True:
  n = input("Enter a name. Enter stop to end this. ")
  name.append(n)
  if (n == "stop" or "Stop"):
    break;
for i in range(len(name)-1):
  print(name[i])

print("\n")

