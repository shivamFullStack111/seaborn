import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")

sns.violinplot(
    data=df,
    x="island",                                     # To make horizonatal change x with y                          
    y="body_mass_g",
    hue="species",
    split=True,
    order=["Dream","Biscoe","Torgersen"],           # Reorder in table
    linewidth=1,                                    # Border width
    linecolor="black",                              # Border color
    scale="width"
)

plt.grid()
plt.show()