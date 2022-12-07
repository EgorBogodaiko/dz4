# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

input_file = open('for3.txt','r',encoding="UTF-8")
working_list =[]
for line in input_file:
    if line[len(line)-1] == "\n":
        mark_index=2
    else:
        mark_index=1
    if int(line[len(line)-mark_index])>4:
        line=(line.upper()) 
    print(line[len(line)-mark_index])
    working_list.append(line)
input_file.close
input_file = open('for3.txt','w',encoding="UTF-8")
input_file.writelines(working_list)
input_file.close