#emojize.py
#https://cs50.harvard.edu/python/2022/psets/4/emojize/

import emoji

z = input('Input: ')
print('Output:', emoji.emojize(z, language='alias'))
