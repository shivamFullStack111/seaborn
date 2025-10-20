# Using catplot function we can create any type of graph using kind perameter 

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")


# =========== BUILD IN THEMES =====================================================================================================================
sns.set_style("darkgrid")                           #  Using set_style we can change background color or grid color, like dark and white

# ==== ====== CHANAGE FONT SIZE AND LINE THICKNESS ======================================================================================================================
sns.set_context("poster")                           # Change font size and line thickness "paper" (small), "notebook" (normal), "talk" (medium), "poster" (large)

# =========== REMOVE EXTRA BORDERS ===========================================================================================================================
sns.despine()                                       # remove extra borders

# =========== CHANGE GRAPH DIMENTIONS ====================================================================================================================================
plt.figure(figsize=(1,6))                           # Change graph width and height

# =========== Color palette =================================================================================================================================
sns.barplot(
    palette="Blues",                                # This make bars of chart in different different blue colors
    data=df,
    x="island",
    y="body_mass_g",
)



plt.show()