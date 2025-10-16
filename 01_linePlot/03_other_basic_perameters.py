import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd

df = pd.read_csv("penguins.csv").head(50)


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

# style="sex"           => For every different value of sex use different style     EXAMPLE: for Male it will use simple line (-) and for Female it will use dotted line (--)
# hue="sex"             => For different value of sex use different colors 
# palette="Blues"       => In palette we provide color scheme which is combination of different color, when using hue perameter this assign random color combination so we can provide custom color scheme
# markers=["o","^"]     => This add marker in cart markers=[] for multiple and marker="" for single
# dashes=False          => Convert every dashed line to simple line
# legend=False          => Remove legend from graph

plt.title("Testing")
plt.grid()
plt.show()