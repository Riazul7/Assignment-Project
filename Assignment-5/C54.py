class EmptyListException(Exception): # class EmptyListException is derived from superclass Exception
    pass
class InvalidElementException(Exception): # class InvalidElementException is derived from superclass Exception
    pass
def calculate_average():
    try:
        l = input("Enter number in list separated by space:").split() # Create list containing items which are in string format
        if not l:
            raise EmptyListException("Input list is empty.") # Raise EmptyListException if input list is empty
        return sum(list(map(lambda x: float(x), l))) / len(l) # Return average of numbers
    except EmptyListException:
        raise
    except Exception as e:
        raise InvalidElementException(f"Error:{str(e)}") # Raise InvalidElementException if any element of input list is not number
try:
    print(calculate_average())
except EmptyListException as e:
    print("Empty error:",str(e))
except InvalidElementException as e:
    print("An error occurs.",str(e))