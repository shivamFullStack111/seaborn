import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

# Load the dataset
df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv").head(10)          
 
sns.barplot(
    y=[1,2,3,4,5],
    x=[333,535,633,453,13],
    orient="h",  # h make barplot horizontal
    
)


plt.show()
