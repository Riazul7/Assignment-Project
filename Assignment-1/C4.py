# Q: Write a Python function called count_vowels that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. Ignore case sensitivity.
def count_vowels(str):
    return str.lower().count("a")+str.lower().count("e")+str.lower().count("i")+str.lower().count("o")+str.lower().count("u")
print(count_vowels("An aeroplane is our asset"))