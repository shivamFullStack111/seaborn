# Why we use countplot even though we have barplot because barplot create bar of mean and countplot simple show count 


import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")

sns.countplot(
    data=df,
    x="species",   # For Horizontal bar change x to y="species"
    hue="sex",
)

plt.show()