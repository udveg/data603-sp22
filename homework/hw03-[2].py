#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from mrjob.job import MRJob


# In[3]:


import re


# In[8]:


get_ipython().run_cell_magic('file', 'test45.py', "\nfrom mrjob.job import MRJob\nimport re\n\nclass wordcount(MRJob):\n        \n    def mapper(self, _, line):\n        row=line.split(',')\n        identifier=row[1]\n        regex = '\\d{4}-\\d{2}'\n        match = re.findall(regex, identifier)\n            \n        yield match, 1\n\n\n    def reducer(self,key, values):\n         yield key, sum(values)\n        \nif __name__ == '__main__':\n    wordcount.run()")


# In[9]:


get_ipython().system('curl https://raw.githubusercontent.com/udveg/hello-world/main/yelp.csv -o new_yelp.csv')


# In[10]:


import test45


# In[11]:


import test45
mr_job = test45.wordcount(args=['new_yelp.csv'])
with mr_job.make_runner() as runner:
    runner.run()
    print("number of reviews in given month and year")
    for key, value in mr_job.parse_output(runner.cat_output()):
        print(key, value)


# In[ ]:




