# Charlie Gussen: CCG 12/9/21

def letter_counter(word,letter):
    count = 0
    for x in word:
        if x == letter:
            count += 1
    return count

print(letter_counter("cat", "t") == 1)
print(letter_counter("apple", "p") == 2)
print(letter_counter("supercalifragilisticexpialidocious", "i") == 7)
