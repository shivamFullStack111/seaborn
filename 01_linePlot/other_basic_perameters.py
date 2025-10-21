import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv").head(50)


sns.lineplot(
                data=df,
                x="bill_length_mm", 
                y="bill_depth_mm",
                hue="sex",
                style="sex",
                palette="Blues",
                markers=["o",">"],
                dashes=False,
                legend=False
) 

# ============================================== PERAMERTER EXPLANATION =======================================================================================================================

# style="sex"                          => For every different value of sex use different style     EXAMPLE: for Male it will use simple line (-) and for Female it will use dotted line (--)

# hue="sex"                            => For different value of sex use different colors 

# palette="Blues"                      => In palette we provide color scheme which is combination of different color, when using hue perameter this assign random color combination so we can provide custom color scheme

# markers=["o","^"]                    => This add marker in cart markers=[] for multiple and marker="" for single

# dashes=False                         => Convert every dashed line to simple line

# legend=False                         => Remove legend from graph

# hue_order=["FEMALE","MALE"]          => we can also reorder by hue                                                               

# kde=True                             => adds a smooth trend line on top of the bars for Bargraph

# rug=True                             => adds small vertical lines for each data point on the x-axis 

# orient="h"                           => This will make barplot to horizontal h -> make horizontal v -> make vertical             

# saturation=1                         => Larger the number enhance color and lower the number decrease quality of color           

# errcolor="red"                       => Change color of small stick that are upon the bars  

# errwidth=5                           => Increase width of stick upon bar                                                          

# alpha=0.3                            => Opacity of graph                                                                          
                                       



plt.title("Testing")
plt.grid()
plt.show()