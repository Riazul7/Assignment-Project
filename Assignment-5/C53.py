l=input("Enter string in list separated by space:").split() # It will return list containing item itself
print("New list containing the strings with more than 5 characters are:")
print(list(filter(lambda x:len(x)>5,l))) # Use filter function to show list containing strings with more than 5 characters