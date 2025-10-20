# Using catplot function we can create any type of graph using kind perameter 

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")

# =========================== Calculating mean for testing ====================================
TorgersenData = df[df["island"]=="Torgersen"]
print(np.mean(TorgersenData.body_mass_g))
# =========================================================================================

sns.catplot(
    data=df,
    x="island",
    y="body_mass_g",
    kind= "point"                            # Using this perameter we can create any type of graph possible values  => (bar, box, count, swarm, strip, violin, boxen, point )
)

plt.show()