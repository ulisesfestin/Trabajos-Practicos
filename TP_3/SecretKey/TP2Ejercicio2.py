import os

def rename_files(old_name, new_name):
    file_old_name = os.path.join(r"D:\USUARIO\Desktop\FACULTAD\SEGUNDO AÑO\COMPUTACIÓN\TRABAJOS PRÁCTICOS\TP N°2\SecretKey", old_name)
    file_new_name = os.path.join(r"D:\USUARIO\Desktop\FACULTAD\SEGUNDO AÑO\COMPUTACIÓN\TRABAJOS PRÁCTICOS\TP N°2\SecretKey", new_name)
    os.rename(file_old_name, file_new_name)


list_dir = os.listdir(r"D:\USUARIO\Desktop\FACULTAD\SEGUNDO AÑO\COMPUTACIÓN\TRABAJOS PRÁCTICOS\TP N°2\SecretKey")
list_sin_num = ['los angeles.jpg', 'cairo.jpg', 'rochester.jpg', 'madrid.jpg', 'houston.jpg', 'bristol.jpg', 'buenos aires.jpg', 'chennai.jpg', 'hyderabad.jpg', 'miami.jpg', 'sydney.jpg', 'athens.jpg', 'seoul.jpg', 'austin.jpg', 'ithaca.jpg', 'colombo.jpg', 'london.jpg', 'sao paulo.jpg', 'singapore.jpg', 'sunnyvale.jpg', 'istanbul.jpg', 'san diego.jpg', 'new york.jpg', 'dallas.jpg', 'kiev.jpg', 'bogota.jpg', 'edinbrugh.jpg', 'seattle.jpg', 'san jose.jpg', 'pune.jpg', 'chicago.jpg', 'shanghai.jpg', 'bangalore.jpg', 'bucharest.jpg', 'delhi.jpg', 'tel aviv.jpg', 'gainesville.jpg', 'jacksonville.jpg', 'berkeley.jpg', 'beijing.jpg', 'manchester.jpg', 'karachi.jpg', 'oakland.jpg', 'barcelona.jpg']

print(list_dir)

for i in range(len(list_dir)):
    rename_files(list_dir[i],list_sin_num[i])
