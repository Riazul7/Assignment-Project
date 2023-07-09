import string
s='''In a small village, there was a boy whose mother was very keen on academic studies. Every morning, she encouraged him to read books of high academic value. The boy diligently read the books and studied them.
One day, the boy wanted to go on a trip for some relaxation. To keep his books safe, he used a bag to carry them. He collected his books and placed them carefully in the bag. While at a tourist spot, the boy felt at ease and placed his bag among the beautiful flowers in a garden.
Unbeknownst to him, a large bird flew by and snatched his bag, mistaking it for a nest. The boy realized with great concern that he had lost his books. He realized that his negligence had caused this unfortunate incident.
The boy learned a valuable lesson that day — the power of his words and actions. He understood that his carelessness had led to the loss of his precious books. From that day forward, he vowed to be more responsible and cautious in his actions, realizing that even small acts of negligence could have significant consequences.
This story teaches us the importance of being mindful of our words and actions. It reminds us that our choices and behavior can have lasting effects and that it is crucial to be responsible and attentive in everything we do.'''
def remove_punc(s):
    return s not in string.punctuation # Remove punctuation
s = ''.join(filter(remove_punc, s))
def word_frequency(str):
    d=dict()
    l=[i.lower() for i in str.split() if i.isalpha()] # List containing words in case-insensitive manner
    a=set(l) # Find unique words in case-insensitive manner
    for i in a:
        d[i]=l.count(i) # Taking i as key and its frequency as value in dictionary
    return d # Return required dictionary
print("The dictionary containing unique words and its frequency is:")
print(word_frequency(s))