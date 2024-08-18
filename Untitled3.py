#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


home_page_visitors = pd.read_excel('/Users/faizanraza/Downloads/Home_Page_Visitors.xlsx', sheet_name='homepage')
cart_exit = pd.read_excel('/Users/faizanraza/Downloads/Cart_exit.xlsx')
post_purchase = pd.read_excel('/Users/faizanraza/Downloads/Post_Purchase.xlsx', sheet_name='postpurchase')


# In[3]:


print('Home Page Visitors Data:')
print(home_page_visitors.head())
print('\
Cart Exit Data:')
print(cart_exit.head())
print('\
Post Purchase Data:')
print(post_purchase.head())


# In[4]:


def clean_data(df):
    df['Date Submitted'] = pd.to_datetime(df['Date Submitted'])
    return df


# In[6]:


home_page = clean_data(home_page_visitors)
cart_exit = clean_data(cart_exit)
post_purchase = clean_data(post_purchase)


# In[7]:


print("Home Page Visitors - Most Important Factors:")
print(home_page['What is most important for you right now?'].value_counts(normalize=True).head())

plt.figure(figsize=(10, 6))
sns.countplot(y='What is most important for you right now?', data=home_page)
plt.title('Most Important Factors for Home Page Visitors')
plt.tight_layout()


# Key Highlight 1:
# 
# Finding: The majority of visitors to the homepage are interested in "Athletic Performance" and "Injury Rehabilitation."
# Importance: Understanding the primary interests of visitors can help tailor content and offers to meet their needs.
# Suggestion: Enhance the homepage with targeted content and promotions related to athletic performance and injury rehabilitation to increase engagement and conversion.

# In[8]:


print("\
Cart Exit - Reasons for Not Purchasing:")
print(cart_exit["If you're leaving and not purchasing a PowerDot today, can you tell us why?"].value_counts(normalize=True).head())

plt.figure(figsize=(10, 6))
sns.countplot(y="If you're leaving and not purchasing a PowerDot today, can you tell us why?", data=cart_exit)
plt.title('Reasons for Cart Abandonment')
plt.tight_layout()


# Key Highlight 2:
# 
# Finding: A significant portion of users leave the cart without purchasing due to a lack of product understanding and not proper comparision which shows why our device is better then the other devices of same nature.
# Importance: Addressing these concerns can reduce cart abandonment rates and improve sales.
# Suggestion: Implement a live chat feature or FAQ section to assist users with product information and provide immediate feedback.

# In[9]:


print("\
Post-Purchase - How Customers First Heard About Us:")
print(post_purchase['Quick question for you: How did you FIRST hear about us?'].value_counts(normalize=True).head())

plt.figure(figsize=(10, 6))
sns.countplot(y='Quick question for you: How did you FIRST hear about us?', data=post_purchase)
plt.title('How Customers First Heard About Us')
plt.tight_layout()


# Key Highlight 3:
# 
# Finding: Social media is the most common channel through which customers first hear about the brand.
# Importance: Leveraging social media can further enhance brand visibility and customer acquisition.
# Suggestion: Invest in social media marketing campaigns and influencer partnerships to capitalize on this channel's effectiveness.
