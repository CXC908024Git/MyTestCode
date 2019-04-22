# -*- coding: utf-8 -*-

from wand.image import Image
import sys

print('Enter the absolute path of pdf file:')
pdf_path=input()
print('Enter the format of picture you want to change:')
pic_format=input()

FN=pdf_path.split('/')[-1].split('.')[0:1][0]

def pdf2pic_format(file_name):
    with Image(filename=file_name) as img:
            img.save(filename="%s.%s" % (FN,pic_format))


pdf2pic_format('%s' % pdf_path)
sys.exit()
                   
    
