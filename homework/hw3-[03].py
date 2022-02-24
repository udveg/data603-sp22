#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from mrjob.job import MRJob


# In[3]:


import re


# In[4]:


get_ipython().run_cell_magic('file', 'test456.py', '\nfrom mrjob.job import MRJob\nimport re\n\nclass wordcount(MRJob):\n    \n    def mapper(self, _, line):\n        divideword = line.split(\',\')\n        s_column = divideword[3]\n        c_column= divideword[7]\n        for i in c_column:\n            if c_column.startswith(\'cool\'):\n                pass\n            else: \n                if c_column != \'0\':\n                    yield "Avg", int(s_column)\n            \n\n    def reducer(self,key, values):\n        num=0\n        num1=0\n        for i in values:\n                num+=1\n                num1+=i\n        yield key, num1/num \n        \nif __name__ == \'__main__\':\n    wordcount.run()')


# In[5]:


get_ipython().system('curl https://raw.githubusercontent.com/udveg/hello-world/main/yelp.csv -o new_yelp.csv')


# In[6]:


import test456


# In[7]:


import test456
mr_job = test456.wordcount(args=['new_yelp.csv'])
with mr_job.make_runner() as runner:
    runner.run()
    for key, value in mr_job.parse_output(runner.cat_output()):
        print(key, value)


# In[ ]:




