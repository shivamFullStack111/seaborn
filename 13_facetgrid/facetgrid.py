# FactGrid use to create multiple graph of same column like if we pass col="sex" then it create 2 graph 1 for Male and another for Female

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")

graph = sns.FacetGrid(
    data=df,
    col="island"                    # island column contain 3 different type of values so map create histogram graph for every value
    # row="sex"                     # We can also provide row if we use row="sex" it create total 6 graph because island contain 3 different value and sex contain 2 different values so 2x3=6 
)
            
graph.map(
    sns.histplot,                   # Graph you want to create
    "body_mass_g"                   # Column name for graph, it will make histogram for body_mass_g column
).add_legend()               

plt.show()