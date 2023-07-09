l=input("Enter integer numbers in list separated by space:").split() # It will return list containing item itself which are in string format
print("New list containing the transformed elements is:")
print(list(map(lambda x:int(x)*2,l))) # It will return required list