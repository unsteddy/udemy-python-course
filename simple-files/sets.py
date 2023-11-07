art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)


all_friends = art_friends.union(science_friends)
print(all_friends)



# exercise
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friend_name = input("Yo gimme a friends name: ")

# Add the name to the empty set
user_friends.add(friend_name)

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print(nearby_people.intersection(user_friends))
