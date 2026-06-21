deep = input("Answer to the great question of life, the universe and everything: ")
better = deep.strip().lower()

# Fixed spelling to 'forty' and capitalized the outputs
if better == "42" or better == "forty two" or better == "forty-two":
    print("Yes")
else:
    print("No")