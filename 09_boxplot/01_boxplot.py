import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")

sns.boxplot(data=df,x="island",y="body_mass_g",palette='Blues',hue="sex")

plt.grid(True)

plt.show()