#Q3:You have been given a list of strings representing a paragraph. Write a program that counts the frequency of each word in the paragraph and outputs the word with the highest frequency. The program should ignore any punctuation marks and consider the words case-insensitively.
# str="""My name is Riazul Azim.
#        I have done my M.Sc from Kalyani University.
#        I have bicycle.
#        My hobby is reading books.
#     """
# import string
# punctuation=string.punctuation
# def remove_punc(s):
#     return s not in punctuation
# str = ''.join(filter(remove_punc, str))
# l=[i.lower() for i in str.split()]
# dict={}
# for i in l:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# key = [i for i in dict if dict[i]==max(dict.values())]
# for j in key:
#     print(j)
