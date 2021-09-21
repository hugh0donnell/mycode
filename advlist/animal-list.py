#!/usr/bin/env python3

animals = ["Fox","Fly","Ant","Bee","Cod","Cat","Dog","Yak","Cow","Hen","Koi","Hog","Jay","Kit"]
print(animals[0] + " " + animals[1] + " " + animals[2] + " " + animals[3] + " " + animals[4] + " " + animals[5] + " " + animals[6])

for i in animals:
  print(i)

print(*animals,sep=" ")

