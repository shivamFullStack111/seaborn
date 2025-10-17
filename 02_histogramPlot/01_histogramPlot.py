import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

# Load the dataset
df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")

# Create a histogram for bill_depth_mm with specific bins
# kde=True adds a smooth trend line on top of the bars
# rug=True adds small vertical lines for each data point on the x-axis
# color="red" change the bar color

sns.displot(
    df["bill_depth_mm"],              
    bins=[10,12,14,16,18,20,22,24],      
    kde=True,                        
    rug=True,   
    color="red"           ,
)

plt.show()
