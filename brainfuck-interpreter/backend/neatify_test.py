'''Testing code for formatter goes here

@author: tdhiraj

'''

from neatify import Neatify

sample_code = '>>++++++[>++++++++<-]+[[>.[>]+<<[->-<<<]>[>+<<]>]>++<++]'
formatter = Neatify()

print(formatter.format(sample_code))

