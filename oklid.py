from  math import sqrt

def euclideanDistance(point1 , point2):
    firstValue = (point1[1] - point2[1]) ** 2
    secondValue = (point1[0] - point2[0]) ** 2
    return  sqrt(firstValue + secondValue) 


points = []
distances = []
i = 1
flag = 1
while (flag != 0):
    x = int(input(f"{i}. X kordinatını girin: "))
    y = int(input(f"{i}. Y kordinatını girin: "))
    flag = int(input("Bitirmek için 0 a basın: "))
    i += 1
    point = (x,y)
    points.append(point)

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

print("Noktalar arasındaki minimum Öklid mesafesi:", min(distances))