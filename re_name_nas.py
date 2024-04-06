import os
import re

file_path = r'/Volumes/share_vd/media/潜伏 (2009) 4K/'
for root, dirs, files in os.walk(file_path):
    print(files)

for file in files:
    srcFile = file
    dstFile = re.sub(r'E(\d+)', r'S01E\1', srcFile)
    # dstFile = re.sub(r'Fullmetal.Alchemist꞉ Brotherhood', r'钢之炼金术师', srcFile)
    os.rename(file_path + '/' + srcFile, file_path + '/' +dstFile)