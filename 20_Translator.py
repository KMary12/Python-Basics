def translate_function(value):
    translation = " "
    for letter_var in value:
        if letter_var in "AEIOUaeiou":
            if letter_var.isupper():
                translation = translation + "G"
                print(translation)
            else:
                translation = translate_function + "g"
        else:
            translation = translation +letter_var
    return translation

print(translate_function(input("Enter a prhase for translation: ")))
