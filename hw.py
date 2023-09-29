# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def group_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range=None):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' not exist.")
        return
    
    files = os.listdir(directory)
    
    def generate_new_name(index):
        if name_range:
            source_name = files[index][name_range[0]-1:name_range[1]]
        else:
            source_name = files[index].split('.')[0]    
        
        new_name = f"{desired_name}{str(index).zfill(num_digits)}.{target_extension}"
        return source_name + new_name
    
    renamed_count = 0
    for index, filename in enumerate(files):
        if filename.endswith(f".{source_extension}"):
            new_name = generate_new_name(renamed_count)
            source_path = os.path.join(directory, filename)
            target_path = os.path.join(directory, new_name)
            os.rename(source_path, target_path)
            renamed_count += 1
            print(f"File '{filename}' renamed -> '{new_name}'")
    print(f"Renamed {renamed_count} file(s).")

directory = '' # path
desired_name = '' # file name
num_digits = 3
source_extension = 'txt'
target_extension = 'dat'
name_range = (3, 6)

group_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range)
