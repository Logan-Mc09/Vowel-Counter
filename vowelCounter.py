# Count vowels in a given word


# Create list variable to store vowels
vowels = ['a','e','i','o','u']
vowel_count = []
# Create function that loops through letters in a word, counting the number of vowels
def vowel_check():

    word = input(str("Please enter a word: "))
    word_break = word.split()
    
    for letter in word:

        if letter in vowels:
                
            vowel_count.append(letter)

        else: pass

    print(vowel_count)

vowel_check()

