#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


root = Tk()


# In[3]:


root.geometry("500x300")


# In[4]:


def getvals():
    print("Accepted")


# In[5]:


##heading
Label(root, text= "Registration Form", font = "arial 15 bold").grid(row=0, column=3)


# In[6]:


###Fields name
name = Label(root, text="name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
email = Label(root, text="email")
age = Label(root, text="email")
country = Label(root, text="From?")


# In[7]:


### Packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
email.grid(row=4, column=2)
country.grid(row=5, column=2)


# In[8]:


### Variables for storing data
name_v= StringVar
phone_v= StringVar
gender_v= StringVar
email_v= StringVar
country_v= StringVar
check_v= IntVar


# In[9]:


## Creating entry field
nameentry = Entry(root, textvariable = name_v)
phoneentry = Entry(root, textvariable = phone_v)
genderentry = Entry(root, textvariable = gender_v)
emailentry = Entry(root, textvariable = email_v)
countryentry = Entry(root, textvariable = country_v)


# In[10]:


# Packing all entry fields
nameentry.grid(row=1, column= 3)
phoneentry.grid(row=2, column= 3)
genderentry.grid(row=3, column=3 )
emailentry.grid(row=4, column= 3)
countryentry.grid(row=5, column=3 )


# In[11]:


#### Creating check box
checkbtn = Checkbutton(text="remember me?", variable = check_v)
checkbtn.grid(row=6, column= 3)


# In[12]:


#### Submit button
Button(text = "Submit", command = getvals).grid(row=7, column= 3)


# In[ ]:





# In[ ]:





# In[13]:


root.mainloop()


# In[ ]:




