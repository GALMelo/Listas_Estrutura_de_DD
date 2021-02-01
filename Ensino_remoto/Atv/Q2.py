n = int(input())
count = 1

list1 = []
list2 = []

while count <= (n*2):
    if count <= n:
        value = int(input())
        list1.append(value)
        count += 1
    else:
        value = int(input())
        list2.append(value)
        count += 1

index = 0
while index < n:
    print(list1[index])
    print(list2[index])
    index += 1

