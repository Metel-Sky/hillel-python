from operator import itemgetter


def text_preprocessing(text: str, unused_symbols: list, unused_words: set) -> list:
    """
    Очищает текст от ненужных символов и делит его на слова
    :param text: исходный текст
    :param unused_symbols: ненужные символы
    :return: список слов без лишних символов
    """
    for symbol in unused_symbols:
        text = text.replace(symbol, '')

    words = list()
    for word in text.split():
        words.append(word.strip())

    # [<конечный элемент (можно с преобразованием!)>
    # for <название новой переменной>
    # in <откуда переменная берет значения>
    # if <условие попадания>]
    words = [word.strip() for word in text.split() if word.strip() not in unused_words]
    return words


if __name__ == '__main__':
    diesel_article = """The diesel engine, named after Rudolf Diesel, is an internal combustion
     engine in which ignition of the fuel is caused by the elevated temperature 
     of the air in the cylinder due to mechanical compression; thus, the diesel 
     engine is called a compression-ignition engine (CI engine). This contrasts 
     with engines using spark plug-ignition of the air-fuel mixture, such as a 
     petrol engine (gasoline engine) or a gas engine (using a gaseous fuel like 
     natural gas or liquefied petroleum gas).""".lower()

    stopwords_set = {'the', 'of', 'or', 'a', 'an', 'is', 'such', 'by', 'thus', 'like', 'as', 'are', 'am', 'to', 'in',
                     'which', 'this', 'with', 'due', 'after'}
    article_words = text_preprocessing(
        diesel_article,
        ['(', ')', '.', ',', ';', ':', '?', '!', "'"],
        stopwords_set)

    print('Preprocessed words:', article_words)

    word_population = dict()

    for word in article_words:
        if len(word) > 5:
            word = word[:5]
        elif len(word) > 3:
            word = word[:3]
        else:
            # continue - нелинейное ключевое слово, как и break используется в циклах for и while. В отличие от break,
            # не выходит из цикла, а командует перейти в начало цикла, прервав лишь текущую итерацию
            continue
        if word not in word_population:
            word_population[word] = 0
        word_population[word] += 1

    print(word_population)
    print('Sorted', sorted(
        list(word_population.items()),
        key=itemgetter(1),
        reverse=True)
    )