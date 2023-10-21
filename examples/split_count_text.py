def split_text_and_count_words(text):
    # Split the text into words, remove punctuation, and convert to lowercase
    words = text.split()

    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    cleaned_words = []
    for word in words:
        word = word.strip(punctuation)
        if word:
            cleaned_words.append(word.lower())

    # Count the frequency of each word
    word_count = {}
    for word in cleaned_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

def find_most_common_words(word_count, n=10):
    # Find the n most common words without sorting
    most_common = []
    for _ in range(n):
        most_common.append((max_word, word_count[max_word]))
        del word_count[max_word]  # Remove the word from consideration
    return most_common

# Start here - read text
with open("text.txt", 'r') as file:
    text = file.read()

print(text)

# Split the text, count words, and find the 10 most common words
word_count = split_text_and_count_words(text)
print(word_count)
#
# print("The 10 most common words and their counts:")
# most_common_words = find_most_common_words(word_count)
# for word, count in most_common_words:
#     print(f'{word}: {count}')
