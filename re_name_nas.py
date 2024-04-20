import os
import re

file_path = r'/Volumes/share_vd/media/我们与恶的距离 (2019) 4K/'
for root, dirs, files in os.walk(file_path):
    print(files)

for file in files:
    srcFile = file
    dstFile = re.sub(r'第(\d+)', r'我们与恶的距离S01E\1', srcFile)
    # dstFile = re.sub(r'Fullmetal.Alchemist꞉ Brotherhood', r'钢之炼金术师', srcFile)
    os.rename(file_path + '/' + srcFile, file_path + '/' +dstFile)