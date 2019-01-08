a =[]
names_list = []
temp_list = []
foo_list = []
bar_list = []
palabra_list = []
#names_list = list(map(str.strip, open(r'D:\madhurwork\kem_poc\textai\ss\lookup_cache\kem\kem_refdata\country_list.txt','r',encoding='utf-8')))
# with open()as file:
#     file = map(str.strip(),)
#     names_list = [line.strip().upper() for line in file if line.strip()]
# with open(r'D:\madhurwork\kem_poc\textai\ss\lookup_cache\kem\kem_refdata\country_list.txt',encoding='utf-8')as file:
#     temp_list = [line for line in file ]

with open(r'filename here')as file:
    names_list = [line.strip().lower() for line in file if line.strip()]
# with open(r'D:\madhurwork\kem_poc\textai\ss\lookup_cache\kem\kem_refdata\Drawer_Name.txt')as file:
#     bar_list = [line.strip().upper() for line in file if line.strip()]
# with open(r'D:\madhurwork\kem_poc\textai\ss\lookup_cache\kem\kem_refdata\Remitting_Bank_Country.txt')as file:
#     palabra_list = [line.strip().upper() for line in file if line.strip()]
# names_list.extend(temp_list)
# names_list.extend(foo_list)
# names_list.extend(bar_list)
# names_list.extend(palabra_list)
names_list = list(set(names_list))
names_list.sort(key=len)
# print(names_list)
with open(r'filename here','w',encoding='ANSI') as file:
    for i in names_list[::-1]:
        file.write("%s\n" %i)
