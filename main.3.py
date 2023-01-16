a = int(input("Введіть перше число: "))

b = int(input("Введіть друге число: "))

while True:

    c = int(input("Введіть число: "))

    if c >= a and c <= b:

        break

    else:

        print("Введіть число знову")

for i in range(a, b + 1):

    if i == c:

        print("!", i, "!", sep="", end=" ")

    else:

        print(i, end=" ")