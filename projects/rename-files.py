# Python program to rename all file
# names in your directory
import os
 
os.chdir('C:\\Users\\Dell\\Desktop\\w3-schools\\howto')
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = f_name.replace("js_","").replace("css_","").replace("ifr_","")
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)