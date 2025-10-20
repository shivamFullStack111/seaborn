import matplotlib.pyplot as plt   
import pandas as pd             
import seaborn as sns           

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv").head(50)

sns.scatterplot(
    data=df,                # The data we want to use (our DataFrame "df")
    x=df.bill_length_mm,    # The column for the X-axis (bill_length_mm → penguin’s beak length)
    y=df.bill_depth_mm,     # The column for the Y-axis (bill_depth_mm → penguin’s beak depth)
    hue="sex",              # Color dots based on whether the penguin is male or female
    sizes=[50, 100],        # How big or small the dots can be
    palette="Blues",        # Blue color schemes
    alpha = 1,              # Opacity
    markers={               # Custom marker only works if style perameter is used
        "MALE": "^",
        "FEMALE": "*"
    },
    style="sex"            # Change marker style automatically   
)

plt.show()              
