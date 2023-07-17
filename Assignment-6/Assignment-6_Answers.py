def count_occurrences(element_list):
    d=dict()
    for i in set(element_list):
        d[i]=element_list.count(i) # Use count function to count element i and put it as value corresponding to its key i in dictionary d
    return d
print("The dictionary containing the count of each unique element is:")
print(count_occurrences([1,2,3,2,1,3,3,4,5]))
def remove_duplicates(given_list):
    l1=[]
    for i in given_list:
        if i not in l1:
            l1.append(i) # Appending unique element to l1
    return l1
print("The new list where duplicate elements are removed and the order of the original list is preserved is:")
print(remove_duplicates([1,2,3,2,1,3,3,4,5]))
def find_common_elements(list1,list2):
    l=[]
    d1 = dict()
    d2 = dict()
    s1 = set(list1)
    s2 = set(list2)
    for i in s1:
        d1[i]=list1.count(i) # Creating dictionary d1 taking unique elements of list1 as keys and count of their unique element as their corresponding value
    for j in s2:
        d2[j]=list2.count(j) # Creating dictionary d1 taking unique elements of list2 as keys and count of their unique element as their corresponding value
    for k in s1 & s2:
        l.extend([k for m in range(min(d1[k], d2[k]))]) # Creating list of common elements
    return l
print('The list containing the common elements between given two lists is:')
print(find_common_elements([1,2,3,4,5],[4,5,6,7,8]))
def reverse_dictionary(given_dict):
    return dict([(value,key) for key,value in given_dict.items()]) # return dictionary where keys and values are swapped
print('The new dictionary where the keys and values are swapped is:')
print(reverse_dictionary({'a':1,'b':2,'c':3}))
l=[]
def flatten_list(given_list):
    for i in given_list:
        if type(i) is list:
            flatten_list(i) # Call the function
        else:
            l.append(i) # Append element
    return l
print('The flattened version of the given nested list is:')
print(flatten_list([[1,2,3],[4,5],[6,7,8,9]]))
def merge_dictionaries(dict1,dict2):
    d=dict()
    d.update(dict1) # Update d
    d.update(dict2) # Update d
    return d
print('The new dictionary that contains all the key-value pairs from both given dictionaries is:')
print(merge_dictionaries({'a': 1,'b': 2},{'c': 3,'d': 4}))
def find_unique_elements(*given_lists):
    new_list=[]
    for l in given_lists:
        for i in l:
            new_list.append(i) # Append all elements from given lists to new_list
    return list(set(new_list)) # Return list which contains unique elements from given lists
print('The list containing only the unique elements from all the given lists is:')
print(find_unique_elements([1,2,3],[2,3,4],[3,4,5,6]))
def sort_dictionary_by_value(given_dict):
    l1=list(given_dict.keys())
    l2=list(given_dict.values())
    l3=sorted(l2) # l2 is sorted,i.e, values of dictionary is sorted
    return dict([(l1[l2.index(i)],i) for i in l3]) # Return required dictionary and use index function to find position
print('The new dictionary where the keys are sorted based on their corresponding values is:')
print(sort_dictionary_by_value({'a':3,'b':1,'c':2}))
def remove_empty_lists(nested_list):
    if type(nested_list)!=list:
        return nested_list
    result = []
    for item in nested_list:
        if type(item) is list:
            nested_result = remove_empty_lists(item) # Call function remove_empty_lists
            if nested_result!=[]:
                result.append(nested_result) # If it is not [], append to result
        else:
            result.append(item) # Append to result
    return result
print('The new list with all empty lists removed is:')
print(remove_empty_lists([1,[],[2,3],[],[4],[]]))
def count_element_frequency(element_list):
    d=dict()
    for i in set(element_list):
        d[i]=element_list.count(i) # Use count function to count element i and put it as value corresponding to its key i in dictionary d
    return d
print('The dictionary containing the frequency of each element in the list is:')
print(count_element_frequency([1,2,2,3,3,3,4,4,4,4]))
def split_list_by_value(given_list,number):
    l1=[]
    l2=[]
    for i in given_list:
        if i<number:
            l1.append(i) # Append element in l1 if it is less than number
        else:
            l2.append(i) # Append element in l2 if it is greater than number
    return l1,l2
print('Two lists: one containing all elements less than the given value, and the other containing all elements greater than or equal to the given value is:')
print(split_list_by_value([1,2,3,4,5],3))
def find_longest_word(given_list):
    l=[]
    for i in given_list:
        l.append(len(i))
    return given_list[l.index(max(l))] # Index function to find position of maximum value in l and then return longest word in given list
print('The longest word in the given list is:')
print(find_longest_word(['apple','banana','cherry','durian']))
from flatten_dict import flatten
from pprint import pprint
def flatten_dictionary(given_dict):
    return pprint(flatten(given_dict,reducer='dot')) # Concatenated using dot notation
print('The flattened dictionary where the keys are concatenated using dot notation is:')
flatten_dictionary({'a': 1,'b':{'c': 2,'d':{'e':3}}})
from collections import defaultdict
def get_list_intersection(*lists):
    result=[]
    common_dict = {}
    frequency_dicts = []
    for lst in lists:
        frequency_dict = defaultdict(int)
        for key in lst:
            frequency_dict[key] += 1
        frequency_dicts.append(dict(frequency_dict)) # Appending dictionaries taking input from list and using frequency of unique element as value
    common_keys = set(frequency_dicts[0].keys())
    for d in frequency_dicts[1:]:
        common_keys.intersection_update(d.keys()) # common_keys containing unique elements which are present in all dictionaries
    for key in common_keys:
        min_value = min(d[key] for d in frequency_dicts)
        common_dict[key] = min_value # Create dictionary which contains unique elements present in all dictionaries as keys and its minimum value in all dictionaries as value
    for key,value in common_dict.items():
        result.extend([key]*value)
    return result # Return required list
print('The list containing the elements that are present in all the input lists is:')
print(get_list_intersection([1,2,3],[2,3,4],[3,4,5,6]))
def get_key_with_max_value(given_dict):
    v1=list(given_dict.values())
    m=max(v1) # Find maximum value
    i=v1.index(m) # Find position of that maximum value
    return list(given_dict.keys())[i] # Return required key
print('The key in given dictionary with the maximum value is:')
print(get_key_with_max_value({'a':3,'b':1,'c':2}))
def split_string_by_length(given_string,number):
    l=[]
    n=0
    while n<len(given_string):
        l.append(given_string[n:n+number]) # Append substrings in l
        n+=number
    return l
print('The list of substrings, each of the specified length is:')
print(split_string_by_length('abcdefgh',3))
from collections import defaultdict
def find_common_characters(*strings):
    lists = []
    for i in strings:
        lists.append([*i]) # A list called lists is created by appending list which contains letter of given string
    result=[]
    common_dict = {}
    frequency_dicts = []
    for lst in lists:
        frequency_dict = defaultdict(int)
        for key in lst:
            frequency_dict[key] += 1
        frequency_dicts.append(dict(frequency_dict)) # Appending dictionaries taking input from created list and using frequency of unique element as value
    common_keys = set(frequency_dicts[0].keys())
    for d in frequency_dicts[1:]:
        common_keys.intersection_update(d.keys()) # common_keys containing unique elements which are present in all dictionaries
    for key in common_keys:
        min_value = min(d[key] for d in frequency_dicts)
        common_dict[key] = min_value
    for key,value in common_dict.items():
        result.extend([key]*value)
    return result # Return required list
print('The list containing the common characters present in all the input strings is:')
print(find_common_characters('apple','banana','cherry'))
def count_list_elements(element_list):
    d=dict()
    for i in set(element_list):
        count=element_list.count(i) # variable count is assigned for storing count of each unique element in list
        percentage=(count/len(element_list))*100 # variable percentage is assigned for storing percentage of each unique element in list
        d[i]=count,percentage
    return d # Return required dictionary
print('The dictionary containing the count of each unique element, along with their percentage in the list is:')
print(count_list_elements([1,2,2,3,3,3,4,4,4,4]))
def remove_duplicate_characters(given_string):
    l1=[]
    for i in [*given_string]:
        if i not in l1:
            l1.append(i)
    return ''.join(l1) # Use join function to return required string
print('The new string with duplicate characters removed, while preserving the order of the original string is:')
print(remove_duplicate_characters('banana'))
def find_missing_elements(list1,list2):
    l=[]
    for i in list1:
        if i not in list2:
            l.append(i) # Append missing elements
    return l
print('The list of the missing elements is:')
print(find_missing_elements([10,15,16,12,9,8],[8,15]))
