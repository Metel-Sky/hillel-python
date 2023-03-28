from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    # результирующий префикс = "" (сюда будем добавлять прошедшие проверку буквы)
    prefix = ""
    # найти самое короткое слово
    shortest_word_len = len(min(strs, key=len))
    i = 0
    # пока длина префикса меньше длины самого короткого слова
    while i < shortest_word_len:
        # взять i-тую букву первого слова
        letter = strs[0][i]
        # для каждого последующего слова
        for word in strs[1:]:
            # сравнить одинакова ли i-тая буква
            if word[i] != letter:
                #   если для кого-то не совпало, то возвращаем результат
                return prefix
        # если совпало для всех, добавляем букву в результат
        prefix += letter
        i += 1
    # возвращаем результат
    return prefix

def professional_longestCommonPrefix(v: List[str]) -> str:
    ans = ""
    v = sorted(v)
    for i in range(min(
            len(v[0]),
            len(v[-1])
    )
    ):
        if (v[0][i] != v[-1][i]):
            return ans
        ans += v[0][i]
    return ans


if __name__ == '__main__':
    print(professional_longestCommonPrefix(["flower", "flow", "flight"]))
    print(professional_longestCommonPrefix(["flower", "", "flight"]))
    print(professional_longestCommonPrefix(["flower", "flow", "aba"]))
    print(professional_longestCommonPrefix(["fl", "flow", "zxczc", "flight"]))