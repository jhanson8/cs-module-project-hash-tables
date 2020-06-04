def word_count(s):
    count = {}
    words = s.split()

    if s == "":
        return {}

    for word in words:
        word = word.lower()
        new_word = ""
        for character in word:
            if character.isalnum() or character == "\'":
                new_word += character
        if new_word in count:
            count[new_word] += 1 
        elif new_word == "":
            return {}
        else:
            count[new_word] = 1 
    return_words = dict(count.items())
    return return_words







if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))