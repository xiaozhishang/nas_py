import os
import re

file_path = r'/Volumes/share_vd/media/东京女子图鉴 (2016)/Season 01/'
for root, dirs, files in os.walk(file_path):
    print(files)

for file in files:
    srcFile = file
    dstFile = re.sub(r'S(\d+)', r'东京女子图鉴S\1', srcFile)
    # dstFile = re.sub(r'Fullmetal.Alchemist꞉ Brotherhood', r'钢之炼金术师', srcFile)
    os.rename(file_path + '/' + srcFile, file_path + '/' +dstFile)