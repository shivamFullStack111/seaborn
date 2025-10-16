import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd

df = pd.read_csv("penguins.csv").head(50)

# ===================== * Filling null values * ==============================================================================

df["bill_depth_mm"].fillna(df["bill_depth_mm"].mean(),inplace=True)
df["bill_length_mm"].fillna(df["bill_length_mm"].mean(),inplace=True)
df["flipper_length_mm"].fillna(df["flipper_length_mm"].mean(),inplace=True)
df["body_mass_g"].fillna(df["body_mass_g"].mean(),inplace=True)


# ================= * Deleting null values row from sex * ====================================================================

df.dropna(subset=["sex","species","island"],inplace=True)


# ===================== * scatter plot * =====================================================================================

sns.scatterplot(data=df, x="bill_length_mm", y="flipper_length_mm", hue="species")      #====== hue="species"====== will show different types of species in different colors

plt.grid()
plt.show()