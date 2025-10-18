import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

# Load the dataset
df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")

# This bar create different bars of island category and each bar show average (mean) of biil_lenght_mm 


# ================================================ * PERAMETERS * =====================================================================
#                                                                                                                                     |
# hue="sex"                                also categorise by gender                                                                  |
# order=["Dream","Torgersen","Biscoe"]     we can reorder bars sequence accordingly                                                   |
# hue_order=["FEMALE","MALE"]              we can also reorder by hue                                                                 |
# orient="h"                               This will make barplot to horizontal h -> make horizontal v -> make vertical               |
# saturation=1                             Larger the number enhance color and lower the number decrease quality of color             |
# color="red"                              Color of bars But this is deprecated istead use palette                                    |
# errcolor="red"                           Change color of small stick that are upon the bars                                         |
# errwidth=5                               Increase width of stick upon bar                                                           |
# alpha=0.3                                Opacity of graph                                                       |
#                                                                                                                                     |
# ===================================================================================================================================== 

sns.barplot(
    data=df,
    x=df.island,
    y=df.bill_length_mm,
    hue=df.sex,
    order=["Dream","Torgersen","Biscoe"],
    hue_order=["FEMALE","MALE"],
    errcolor="red",
    errwidth=5,
    alpha=0.2
)


plt.show()
