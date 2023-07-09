import string
s='''In a small village, there was a boy whose mother was very keen on academic studies. Every morning, she encouraged him to read books of high academic value. The boy diligently read the books and studied them.
One day, the boy wanted to go on a trip for some relaxation. To keep his books safe, he used a bag to carry them. He collected his books and placed them carefully in the bag. While at a tourist spot, the boy felt at ease and placed his bag among the beautiful flowers in a garden.
Unbeknownst to him, a large bird flew by and snatched his bag, mistaking it for a nest. The boy realized with great concern that he had lost his books. He realized that his negligence had caused this unfortunate incident.
The boy learned a valuable lesson that day — the power of his words and actions. He understood that his carelessness had led to the loss of his precious books. From that day forward, he vowed to be more responsible and cautious in his actions, realizing that even small acts of negligence could have significant consequences.
This story teaches us the importance of being mindful of our words and actions. It reminds us that our choices and behavior can have lasting effects and that it is crucial to be responsible and attentive in everything we do.'''
def remove_punc(s):
    return s not in string.punctuation # Remove punctuation
s = ''.join(filter(remove_punc, s))
word=input('Enter a word:')
if word in [i for i in s.split() if i.isalpha()]: #Check if word is present in list containing words of text
    print("The word is present in the story text.")
else:
    print("The word is not present in the story text.")