from collections import defaultdict

def encode_ppm(text):
    context_dict = defaultdict(lambda: defaultdict(int))
    order = 16
    encoded_text = []


    for i in range(len(text)):
        char = text[i]
        # Получаем контекст, т.е. последовательность символов перед текущим символом
        # размером order. Если order больше, чем количество символов перед текущим символом,
        # контекст будет состоять из всех символов перед текущим символом.
        context = text[max(0, i - order):i]


        if context:
            # Получаем частотный словарь символов, который соответствует текущему контексту
            freq_dict = context_dict["".join(context)]
            # Считаем общее количество символов в контексте
            total_count = sum(freq_dict.values())
            # Считаем количество текущего символа в контексте
            char_count = freq_dict[char]
            # Вычисляем вероятность текущего символа в контексте
            prob = char_count / total_count if total_count else 0

            # Если вероятность больше 0, то записываем символ в закодированный текст и обновляем
            # частотный словарь для контекста
            if prob > 0:
                encoded_text.append(ord(char))
                encoded_text.append("|")
                freq_dict[char] += 1
            # Если вероятность равна 0, то записываем символ с префиксом 1105 в закодированный текст
            # и добавляем новый символ в частотный словарь для контекста
            else:
                encoded_text.append(1105 + ord(char))
                encoded_text.append("|")
                freq_dict[char] = 1
        # Если контекст пустой, то записываем символ в закодированный текст и
        # обновляем частотный словарь для пустого контекста
        else:
            encoded_text.append(ord(char))
            encoded_text.append("|")
            context_dict[""].update({char: 1})

    return encoded_text
#--------------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------


def decode_ppm(encoded_text):
    # Инициализируем переменные: context_dict - словарь контекстов, order - порядок модели, text - декодированный текст.
    context_dict = defaultdict(lambda: defaultdict(int))
    order = 16
    text = ""

    # Проходимся по каждому символу в закодированном тексте.
    for i in range(len(encoded_text)):
        char_code = encoded_text[i]

        # Если символ имеет код меньше или равный 1104,
        # то он является символом из алфавита ASCII и декодируется напрямую в символ.
        # Иначе, символ является русской буквой и декодируется с помощью вычитания 1105 из кода символа.
        if char_code <= 1104:
            char = chr(char_code)
            # Определяем контекст, который будет использоваться для предсказания следующего символа.
            # Он состоит из последних order символов декодированного текста.
            context = text[max(0, len(text) - order):len(text)]
            # Получаем частотный словарь для данного контекста.
            # Если данный контекст не встречался раньше, то автоматически создаем пустой словарь.
            freq_dict = context_dict[context]
            # Получаем частоту появления следующего символа, используя данную модель.
            # Если символ не встречался раньше в данном контексте, то вероятность равна 0.
            char_count = freq_dict[char]
            total_count = sum(freq_dict.values())
            prob = char_count / total_count if total_count else 0

            # Добавляем декодированный символ в декодированный текст и обновляем частотный словарь для данного контекста.
            text += char
            freq_dict[char] += 1
            # Обновляем частотные словари для всех подконтекстов данного контекста.
            for j in range(order):
                if j < len(context):
                    subcontext = context[len(context)-j:]
                    subfreq_dict = context_dict[subcontext]
                    subfreq_dict[char] += 1
                else:
                    break

        else:
            char = chr(char_code - 1105)
            context = text[max(0, len(text) - order):len(text)]
            freq_dict = context_dict[context]
            total_count = sum(freq_dict.values())
            prob = freq_dict[char] / total_count if total_count else 0

            text += char
            freq_dict[char] += 1
            for j in range(order):
                if j < len(context):
                    subcontext = context[len(context)-j:]
                    subfreq_dict = context_dict[subcontext]
                    subfreq_dict[char] += 1
                else:
                    break

    return text