#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Hello():
    
    def __init__(self, firstname, lastname):
        self.first = str(firstname)
        self.last = str(lastname)
        self.count = 0
        
    def sayhello(self):
        print("Hello",self.first,self.last+"!")
        self.count = self.count+1
    
    def saybye(self):
        print("Code was executed",self.count,"times.")
        print("Goodbye,",self.first+'!')


# In[ ]:




