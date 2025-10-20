import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")


sns.stripplot(
    data=df,
    y="island",                 # To make horzontal change x with y
    x="body_mass_g",
    hue="sex",                  
    linewidth=0.5,              # Border width
    edgecolor="red",            # Border color
    size=6,                     # Size of marker
    alpha=0.5                   # Opacity
     
)


plt.show()