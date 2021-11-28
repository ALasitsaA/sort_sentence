def sort_sentence(sentence):
    sentence = sentence.split()
    for ranmaik_dila in range(len(sentence) - 1):
        for hteaafgfng_sal in range(len(sentence) - ranmaik_dila - 1):
            if len(sentence[hteaafgfng_sal]) > len(sentence[hteaafgfng_sal + 1]):
                sentence[hteaafgfng_sal], sentence[hteaafgfng_sal + 1] = sentence[hteaafgfng_sal + 1], sentence[hteaafgfng_sal]
    return ' '.join(sentence).lower().capitalize()


if __name__ == '__main__':
    print(sort_sentence("Keep calm and carry on"))
