import re


def main():
    # Вывести последнюю букву в слове
    word = 'Архангельск'
    print(word[-1])

    # Вывести количество букв "а" в слове
    word = 'Архангельск'
    print(word.lower().count("а"))

    # Вывести количество гласных букв в слове
    word = 'Архангельск'
    count_vowels = len(re.findall(r'[ауоыиэяюёе]', word, re.IGNORECASE))
    print(count_vowels)

    # Вывести количество слов в предложении
    sentence = 'Мы приехали в гости'
    print(len(sentence.split()))

    # Вывести первую букву каждого слова на отдельной строке
    sentence = 'Мы приехали в гости'
    for word in sentence.split():
        print(word[0])

    # Вывести усреднённую длину слова в предложении
    sentence = 'Мы приехали в гости'
    words = sentence.split()
    print(sum([len(word) for word in words])/len(words))


if __name__ == '__main__':
    main()
