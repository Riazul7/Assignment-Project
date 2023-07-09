class ZeroDenominatorException(Exception): # class ZeroDenominatorException is derived from superclass Exception
    pass
class DivisionException(Exception): # class DivisionException is derived from superclass Exception
    pass
def divide_numbers(numerator,denominator):
    try:
        if denominator==0:
            raise ZeroDenominatorException("An error occurs while dividing by zero.") # Raise ZeroDenominatorException when the denominator is zero
        return numerator/denominator
    except ZeroDenominatorException:
        raise
    except Exception as e:
        raise DivisionException(f"Error:{str(e)}") # Raise DivisionException for other errors
try:
    print(divide_numbers(10,"hello"))
except ZeroDenominatorException as e:
    print("Zero Denominator error:",str(e))
except DivisionException as e:
    print("Division error.",str(e))