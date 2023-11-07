age = 30
result = age > 18 and age < 65 # True and true
print(result)

## Like Java, expressions will exit early
exit_early = age < 18 and age > 65
print(exit_early)

exit_early_using_or = age < 18 or age > 65
print(exit_early_using_or)


# Generally zero or empty values will be False and non-zero or non-empty values will be True
bool(0) # False - it is zero
bool(13) # True

bool("") # False
bool("yo") # True

bool([]) # False
bool([1, 2, 3]) # True



