
# 1 exemple din curs
# if 5 > 2:
#     print("5 is grater than 2")

# 2 ex
# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# 3 ex

# fructe = ["mar", "para", "cireasa"]
# x, y, z =  fructe
# print(x)
# print(y)
# print(z)

# ... liste in pyton

# number_list = []
# n = int(input('Introdu numarul de elemente'))
# print("\n")
# for i in range (0, n):
#     print("Introdu elementul la pozitia", i, "")
#     item = int(input())
#     number_list.append(item)
#     print("Lista etse", number_list)


# Exercitii

items = []
n = int(input('Introdu numarul de elemente'))
for i in range(0, n):
    print("Introdu elementul la pozitia", i, "")
    item = int(input())
    items.append(item)

# 1 Sortare


def vector_sort(items):
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if items[i] > items[j + 1]:
                var = items[i]
                items[j] = items[j + 1]
                items[j + 1] = var
    print("Vectorul sortat este", items)


vector_sort(items)

# 2  Min si max
items = []
n = int(input('Introdu numarul de elemente'))
for i in range(0, n):
    print("Introdu elementul la pozitia", i, "")
    item = int(input())
    items.append(item)

max = items[0]
min = items[n-1]

for i in range(0, n):
    if items[i] > max:
        max = items[i]
    elif items[i] < min:
        min = items[i]

print("Minimul din vector este", min)
print("Maximul din vector este", max)


# 3 Realizarea unui vector cu date de tip String

my_favourite_food = []
my_favourite_food.append('Pizza')
my_favourite_food.append('Cake')
my_favourite_food.append('Ice-Cream')
my_favourite_food.append('Soup')

print("Vectorul cu date de tip string este:", my_favourite_food)

# 4 Stergerea elemente din vector
my_favourite_food.remove('Pizza')

print("Vectorul cu date de tip string cu un element sters este:2", my_favourite_food)

# 4 Adaugarea unui element in coada listei
my_favourite_food.append('Peanut Butter')

print("Vectorul cu date de tip string cu un element adaugat este:2",
      my_favourite_food)
