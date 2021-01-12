#!/usr/bin/env python
# coding: utf-8

# In[16]:


nilai_praktek= float(input("nilai praktek:"))
nilai_teori= float(input("nilai teori:"))
nilai_kkm=float(70)


# In[19]:


if nilai_teori >= nilai_kkm and nilai_praktek >= nilai_kkm:
    print("Selamat, anda lulus!") 
elif nilai_teori >= nilai_kkm and nilai_praktek < nilai_kkm:
    print("Maaf, anda harus mengulang ujian praktek")
elif nilai_praktek >= nilai_kkm and nilai_teori < nilai_kkm:
    print("Maaf, anda harus mengulang ujian teori")
else:
    print("Maaf, anda harus mengulang ujian praktek dan ujian teori")


# In[ ]:




