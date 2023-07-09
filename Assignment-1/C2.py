# Q: Write a Python function called find_even_numbers that takes a list of integers as input and returns a new list containing only the even numbers from the input list.
def find_even_numbers(num_list):
    even_number=[]
    for n in num_list:
        if n%2==0:
            even_number.append(n)
        else:
            pass
    return even_number
print(find_even_numbers([1,4,5,6,7,9]))