import string

def word_frequency(sentence):
    # Remove punctuation marks from the sentence and convert it to lower case
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    # Split the sentence into words
    words = sentence.split()
    # Create a dictionary
    frequency = {}
    # Iterate through each word
    for word in words:
        # If the word is already in dictionary, increment its count
        if word in frequency:
            frequency[word] += 1
        # Otherwise, set the count of the word to 1
        else:
            frequency[word] = 1
    # Return the dictionary
    return frequency


sentence = "This is a test sentence. This is another test sentence."
print(word_frequency(sentence))
# Output: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'sentence': 2, 'another': 1}