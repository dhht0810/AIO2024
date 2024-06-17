def count_words_in_file(file_path):
    word_count = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()

    lines = content.split('\n')
    words = []
    for line in lines:
        words.extend(line.split(' '))

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


# Ví dụ sử dụng
file_path = 'Module_1\Week_2\P1_data.txt'
print(count_words_in_file(file_path)['man'])
