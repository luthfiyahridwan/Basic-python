#!/usr/bin/env python
# coding: utf-8

# In[1]:


praktek= float(input("nilai praktek:"))
teori= float(input("nilai teori:"))
kkm=float(70)


# In[2]:


if teori >= kkm and praktek >= kkm:
    print("Selamat, anda lulus!") 
elif teori >= kkm and praktek < kkm:
    print("Maaf, anda harus mengulang ujian praktek")
elif praktek >= kkm and teori < kkm:
    print("Maaf, anda harus mengulang ujian teori")
else:
    print("Maaf, anda harus mengulang ujian praktek dan ujian teori")


# In[ ]:




