#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint


# In[ ]:


resoult=randint(1,20)


# In[ ]:


line=input('Guess the number 1-20: ')
number=int(line)

while resoult!=number :
    if number < resoult :
        print("too low!")
    else:
        print("too high!")
    line=input('Guess the number 1-20: ')
    number=int(line)

print("Congratulation!")

