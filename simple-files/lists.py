friend1 = "Bob"
friend2 = "Mary"

friends = ["Bob", "Mary"]
print(friends[0])

list_of_friends = [
    ["Bob", 30],
    ["Mary", 20]
]
print(f"{list_of_friends[0][0]} is {list_of_friends[0][1]}")

list_of_friends.remove(["Mary", 20])
print(list_of_friends)
