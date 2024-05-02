import os
import re

file_path = r'/Volumes/share_vd/media/西游记后传 (2000) 4K/'
for root, dirs, files in os.walk(file_path):
    print(files)

for file in files:
    srcFile = file
    dstFile = re.sub(r'第(\d+)', r'西游记后传S01E\1', srcFile)
    # dstFile = re.sub(r'Fullmetal.Alchemist꞉ Brotherhood', r'钢之炼金术师', srcFile)
    os.rename(file_path + '/' + srcFile, file_path + '/' +dstFile)