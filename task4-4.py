# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.
import string

rus_alphabet ='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'+string.punctuation
eng_alphabet = string.ascii_lowercase+string.ascii_uppercase+string.punctuation

def cesar (input_str:str, code:int, type:bool):
    if type==False:
        code=-1*code
    rus_alphabet ='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'+string.punctuation
    eng_alphabet = string.ascii_lowercase+string.ascii_uppercase+string.punctuation
    crypted_str = []
    for line in input_str:
        for letter in line:
            crypted_str.append(chr(ord(letter)+code))
    return crypted_str


input_file= open('for4.txt','r',encoding='UTF-8')
coded_file= cesar(input_file,1,True)
input_file.close
output_file = open('for4.txt','w',encoding='UTF-8')
output_file.writelines(coded_file)