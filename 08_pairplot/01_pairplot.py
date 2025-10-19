import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

df = pd.read_csv("/home/shivam111/Desktop/seaborn/penguins.csv").head(40)

# =================================================== PAIRPLOT EXPLANATION =============================================================

# Pairplot automatically create random chart according data but we can changes and modify the graph using their perameters 


# =================================================== PERAMETER EXPLANATION ============================================================

# hue = "sex"                                                  // Differenciate by sex means show male and female data in different colors 

# vars=["bill_length_mm","body_mass_g"]                        // Only create charts using these columns from DataFrame

# hue_order=["Female","Male"]                                  // Change order of hue category

# palette="Blues"                                              // color schemes

# x_vars=["bill_lenght_mm"]                                    // Values that you want to use in x axis

# kind="kde"                                                   // Kind of graph you want  {'scatter', 'kde', 'hist', 'reg'}

# diag_kind="hist"                                             // In digonal make histogram graphs 

sns.pairplot(
    data=df,
    hue="sex",
    kind="scatter",
    diag_kind="auto",
    markers=["^","*"]
)

plt.grid()
plt.show()