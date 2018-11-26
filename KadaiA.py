# A-1
user = ["Bob", "Tom", "Ken"]

# A-2
int_numbers = [1, 2, 3, 4, 5, ]
# int_numbers = list(range(1, 6))
# int_nubers = [i for i in range(1, 6)]


# A-3
kazuma_info = ["Kazuma", "Takahashi", 35]

# A-4
members = ["Kazuma", "Makoto", "Ohitra"]
# print("Kazuma", "Makoto") 誤り

print(members[1])
print(members[0])

print("================")

# A-5
kazuma_info = ["Kazuma", "Takahashi", 35]
print(f"Name:{kazuma_info[0]} {kazuma_info[1]}, Age:{35}")

print("================")

# A-6
odd_numbers = [2, 4, 6, 8]
for o_n in odd_numbers:
    print(o_n)

print("================")

# A-7
even_numbers = [2, 4, 6, 8]
for e_n in even_numbers:
    print(e_n * 2)

print("================")

# A-8
user_info = [["Kazuma", 35], ["Tom", 57], ["Bob", 77]]
for u_i in user_info:
    print(f"Name: {u_i[0]}, Age: {u_i[1]}")

    # name = [0]
    # age = [1]
    #
    # print(f"Name: {name}, Age: {age}")

print("================")

# A-9
kazuma_info = {"first_name": "Kazuma", "family_name": "Takahashi", "age": 35}
print(kazuma_info["first_name"])  # "Kazuma"
print(kazuma_info["family_name"])  # "Takahashi"
print(kazuma_info["age"])  # 35

print("================")

# A-10
import random


def dice():
    return random.randint(1, 6)


print(dice())

print("================")
