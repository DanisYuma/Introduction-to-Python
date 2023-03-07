# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(string: str):
    encode_text = ''
    prev_char = string[0]
    count = 1
    for char in string[count:]:
        if char == prev_char:
            count += 1
            prev_char = char
        else:
            encode_text += str(count) + prev_char
            count = 1
            prev_char = char
    else:
        encode_text += str(count) + prev_char
    return encode_text

def decode(string: str):
    decode_text = ''
    i = 0
    while len(string[i: i + 2]) == 2:
        num, char = string[i: i + 2]
        decode_text += char * int(num)
        i += 2
    return decode_text

if __name__ == '__main__':
    string = '!!assdsdjjhsaaa   kkj444332ssa'
    print(string)
    encoded_text = encode(string)
    print(encoded_text)
    print(decode(encoded_text))
