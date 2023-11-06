age = 34
print(f"You are {age}")

eddie = "Eddie"
greeting = f"How are you, {eddie}?"
print(greeting)

## This is a template for a fstring, which we can call using .format(param)
final_greeting = "How are you, {}?"
eddie_greeting = final_greeting.format(eddie)
print(eddie_greeting)

bob_greeting = final_greeting.format("Bob")
print(bob_greeting)

name_greeting = "How are you, {name}?"
inline_greeting = name_greeting.format(name="Eddie")
print(inline_greeting)

