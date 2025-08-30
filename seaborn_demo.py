import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Try to load a large local CSV file if it exists, else use seaborn's "tips"
csv_path = "largefile.csv"
if os.path.exists(csv_path):
    tips = pd.read_csv(csv_path)
    print(f"Loaded local CSV: {csv_path}")
else:
    tips = sns.load_dataset("tips")
    print("Loaded seaborn 'tips' dataset")

# Ensure numeric columns are correct type
for col in ["total_bill", "tip", "size"]:
    if col in tips.columns:
        tips[col] = pd.to_numeric(tips[col], errors="coerce")

# Basic scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", style="time")
plt.title("Scatter Plot")
plt.show()

# Distribution plot (histogram + KDE)
sns.histplot(tips["total_bill"], kde=True)
plt.title("Histogram + KDE")
plt.show()

# Box plot
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Box Plot")
plt.show()

# Violin plot
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
plt.title("Violin Plot")
plt.show()

# Bar plot (replace ci with errorbar)
sns.barplot(data=tips, x="day", y="total_bill", hue="sex", errorbar="sd")
plt.title("Bar Plot")
plt.show()

# Count plot
sns.countplot(data=tips, x="day", hue="sex")
plt.title("Count Plot")
plt.show()

# Pairplot (drop rows with NaN in numeric columns)
pairplot_cols = ["total_bill", "tip", "size"]
pairplot_data = tips.dropna(subset=pairplot_cols)
sns.pairplot(pairplot_data, hue="sex")
plt.suptitle("Pairplot", y=1.02)
plt.show()

# Heatmap (correlation matrix)
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Regression plot (drop rows with NaN in required columns)
lmplot_data = tips.dropna(subset=["total_bill", "tip", "sex"])
sns.lmplot(data=lmplot_data, x="total_bill", y="tip", hue="sex")
plt.title("Regression Plot")
plt.show()

# FacetGrid (drop rows with NaN in required columns)
facet_cols = ["sex", "time", "total_bill", "tip"]
facet_data = tips.dropna(subset=facet_cols)
g = sns.FacetGrid(facet_data, col="sex", row="time")
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.add_legend()
plt.suptitle("FacetGrid", y=1.02)
plt.show()

# Customization: style, palette, context
sns.set_style("whitegrid")
sns.set_palette("pastel")
sns.set_context("talk")
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Styled Box Plot")
plt.show()

# Save a figure
plt.figure()
sns.histplot(tips["tip"], kde=True)
plt.title("Saved Histogram")
plt.savefig("seaborn_saved_histogram.png")
plt.close()
