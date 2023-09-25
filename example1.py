#!/usr/bin/env python3
# by fabricionieves@comunidad.unam.mx
# GNU/GPL License

import numpy as np

data_list=np.arange(1,11,1)

#for x in data_list:
   # print("value:"+str(x))
   # x=np.cos(np.pi)
#print(data_list)


x="hola!"
z=0

try:
    z=int(x)+1
    print("ok")
    print(z)
except:
    print("Error in sum of z")
    print(z)
