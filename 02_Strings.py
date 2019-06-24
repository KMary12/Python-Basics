print("This is a line of text")
print("This is first line!\nThis is a second line!")
#Prints out the " That normaally would indicate the end of string
print("Tis is some \" test")
#this strin is stored in a vairalable
phrase = "String in a variable"
print(phrase)
print("\n" + phrase + " and concatenated string")
print(phrase.capitalize() )
print(phrase.upper() )
print(phrase.isupper() )
print(phrase.islower() )
# converts variable to uppercase and checks if its true
print(phrase.upper().isupper())
#string functions
print(len(phrase))
print((phrase[2]))
#index
print(phrase.index("t"))
print(phrase.index("i"))
print(phrase)
print(phrase.replace("variable", "variable_replaced"))
