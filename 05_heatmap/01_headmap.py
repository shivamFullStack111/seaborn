import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 



# ==================================== Heatmap using 2d array =====================================================================================================

arr = np.random.randint(1,100,size=(5,6))    # This will create 2D array of 5 row, 6 columns with random numbers between 1 to 100

sns.heatmap(arr)

plt.show()

# ================================= Heatmap using dataset columns ====================================================================================================================
# Heapmap only for numbers data if there are multiple columns in dataset with different different datatype columns like int, float, string then only filter that columns which data type is number you can drop other columns


# ===================================================== Explanation of sns.heatmap() parameters =====================================================

# data:         The main data source (DataFrame or 2D array) to visualize in a heatmap.
# vmin:         Minimum value for the colormap. Controls the color starting point.
# vmax:         Maximum value for the colormap. Controls the color endpoint.
# cmap:         Defines color scheme or palette (like 'coolwarm', 'Reds', 'Blues', 'viridis', etc.)
# annot:        If True, it shows numeric values inside each cell.
# annot_kws:    A dictionary used to style annotation text (font size, color, weight, etc.)
# linewidths:   Thickness of the border lines between each cell.
# linecolor:    Color of the borders between cells.
# cbar:         If True (default), shows a color scale bar on the side. False hides it.
# xticklabels:  Controls visibility of column names (x-axis labels). True = show, False = hide.
# yticklabels:  Controls visibility of row names (y-axis labels). True = show, False = hide.

# ===================================================================================================================================================
 

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv")
data = df.drop(columns=["island","species","flipper_length_mm","sex","body_mass_g"]).head(30)

grph= sns.heatmap(
    data,
    vmin=10,             
    vmax=200,        
    annot=True,        
    linewidths=2,       
    linecolor="gray",  
    annot_kws={         
        "fontsize":10,
        "color":"gray",
    }
    # cmap="Blues",        # Color schemes/pattern like palette
    # cbar=False,          # This will hode bar on right side
    # xticklabels=False,   # Hide x label 
    # yticklabels=False,   # Hide y label    
)




grph.set(xlabel="x label",ylabel="y label")   # Custom label
sns.set(font_scale=4)   # This will scale fontsize in entire graph

plt.show()

