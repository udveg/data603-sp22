#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install mrjob


# In[1]:


import pandas as pd


# In[2]:


from mrjob.job import MRJob


# In[6]:


get_ipython().run_cell_magic('file', 'qwe_1.py', '\nfrom mrjob.job import MRJob\nimport re\n\nclass wordcount(MRJob):\n    @staticmethod\n    def mapper2(identifier, line):\n        words=[]\n        for i in identifier.lower().split():\n            words.append(i)\n            #uniquewords=set(words)\n            average=len(words)/10000\n        return average\n    \n    def mapper(self, _, line):\n        row=line.split(\',\')\n        identifier=row[4]\n        z=identifier.split(" ")\n        avg=self.mapper2(identifier,line)\n        #worz=len(z)\n        #worz=len(identifier.split())\n        yield "Average",avg\n\n    def reducer(self,key, values):\n        yield key,sum(values)\n        \n        \nif __name__ == \'__main__\':\n    wordcount.run()')


# In[7]:


get_ipython().system('curl https://raw.githubusercontent.com/udveg/hello-world/main/yelp.csv -o new_yelp.csv')


# In[8]:


import qwe_1


# In[9]:


mr_job = qwe_1.wordcount(args=['new_yelp.csv'])
with mr_job.make_runner() as runner:
    runner.run()
    for key, value in mr_job.parse_output(runner.cat_output()):
        print(key, value)


# In[ ]:





# In[ ]:




