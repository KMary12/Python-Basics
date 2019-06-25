is_male = True
if is_male:
    print("Your are male")

is_tall = True

#if is_male or is_tall:
#   print("You are male or tall or both")
# else:
#   print("You are Not a male NOR tall")

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not is_tall:
    print(" you are male and not a tall")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not a tall")
