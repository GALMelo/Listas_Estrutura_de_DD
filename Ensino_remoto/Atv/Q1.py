oldest = 0
all = 0
especified = float(0)

for x in range(1,100):
    age = int(input())
    if age > oldest:
        oldest = age
    elif age == -1:
        break;
    list = input().lower().split(' ')
    sex = list[0]
    hair = list[1]
    eyes = list[2]
    if sex == "f":
        if 17 < age < 36:
            if hair == "l":
                if eyes == "v":
                    especified += 1
    all += 1

per = float((especified * 100) / all)

print("Mais Velho: {}".format(oldest))
print("Mulheres com olhos verdes, loiras com 18 a 35 anos: {:.2f} ".format(per))