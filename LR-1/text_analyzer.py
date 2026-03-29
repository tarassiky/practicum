# Консольная программа для анализа текста
# Автор: [Тарасова Д.Ю.]

import string


def count_characters(text):
    """Возвращает общее количество символов."""
    return len(text)


def count_characters_without_spaces(text):
    """Возвращает количество символов без пробелов."""
    return len(text.replace(" ", ""))


def count_words(text):
    """Возвращает количество слов в тексте."""
    words = text.split()
    return len(words)


def count_sentences(text):
    """Возвращает примерное количество предложений."""
    sentence_endings = ".!?"
    count = 0
    for char in text:
        if char in sentence_endings:
            count += 1
    return count


def get_clean_words(text):
    """Очищает текст от знаков препинания и возвращает список слов."""
    translator = str.maketrans("", "", string.punctuation + "«»—…")
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    return words


def find_longest_word(text):
    """Находит самое длинное слово в тексте."""
    words = get_clean_words(text)
    if not words:
        return ""
    return max(words, key=len)


def word_frequency(text):
    """Подсчитывает частоту слов."""
    words = get_clean_words(text)
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def print_frequency(freq_dict):
    """Выводит частоту слов по убыванию."""
    sorted_words = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)

    print("\nЧастота слов:")
    for word, count in sorted_words:
        print(f"{word}: {count}")


def main():
    print("=== АНАЛИЗАТОР ТЕКСТА ===")
    text = input("Введите текст для анализа:\n")

    print("\n=== РЕЗУЛЬТАТЫ АНАЛИЗА ===")
    print(f"Количество символов: {count_characters(text)}")
    print(f"Количество символов без пробелов: {count_characters_without_spaces(text)}")
    print(f"Количество слов: {count_words(text)}")
    print(f"Количество предложений: {count_sentences(text)}")

    longest_word = find_longest_word(text)
    if longest_word:
        print(f"Самое длинное слово: {longest_word}")
    else:
        print("Самое длинное слово: не найдено")

    freq = word_frequency(text)
    if freq:
        print_frequency(freq)
    else:
        print("Слова для анализа не найдены.")


if __name__ == "__main__":
    main()