import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

csv_path = "largefile.csv"
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    # Ensure numeric columns are correct type
    for col in ["total_bill", "tip", "size"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    print(f"Loaded local CSV: {csv_path}")
else:
    df = None
    print("largefile.csv not found, using synthetic data.")

# Line plot
if df is not None and "total_bill" in df.columns:
    plt.figure()
    plt.plot(df["total_bill"].head(100).reset_index(drop=True), label='total_bill')
    plt.title('Line Plot of total_bill')
    plt.xlabel('Index')
    plt.ylabel('total_bill')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y, label='sin(x)')
    plt.title('Line Plot')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Scatter plot
if df is not None and {"total_bill", "tip"}.issubset(df.columns):
    plt.figure()
    plt.scatter(df["total_bill"].head(100), df["tip"].head(100), c='blue', alpha=0.5)
    plt.title('Scatter Plot: total_bill vs tip')
    plt.xlabel('total_bill')
    plt.ylabel('tip')
    plt.show()
else:
    np.random.seed(0)
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 1000 * np.random.rand(50)
    plt.figure()
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
    plt.title('Scatter Plot')
    plt.colorbar()
    plt.show()

# Bar chart
if df is not None and {"day", "total_bill"}.issubset(df.columns):
    plt.figure()
    df.groupby("day")["total_bill"].mean().plot(kind="bar")
    plt.title('Bar Chart: Avg total_bill by day')
    plt.xlabel('Day')
    plt.ylabel('Avg total_bill')
    plt.show()
else:
    categories = ['A', 'B', 'C', 'D']
    values = [10, 24, 36, 18]
    plt.figure()
    plt.bar(categories, values)
    plt.title('Bar Chart')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.show()

# Histogram
if df is not None and "total_bill" in df.columns:
    plt.figure()
    plt.hist(df["total_bill"].dropna(), bins=30, alpha=0.7, color='g')
    plt.title('Histogram of total_bill')
    plt.xlabel('total_bill')
    plt.ylabel('Frequency')
    plt.show()
else:
    data = np.random.randn(1000)
    plt.figure()
    plt.hist(data, bins=30, alpha=0.7, color='g')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Pie chart
if df is not None and "sex" in df.columns:
    plt.figure()
    df["sex"].value_counts().plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart: Sex Distribution')
    plt.axis('equal')
    plt.show()
else:
    sizes = [15, 30, 45, 10]
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    explode = (0, 0.1, 0, 0)
    plt.figure()
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=140)
    plt.title('Pie Chart')
    plt.axis('equal')
    plt.show()

# Subplots
if df is not None and {"total_bill", "tip"}.issubset(df.columns):
    x = df["total_bill"].head(400).reset_index(drop=True)
    y1 = df["tip"].head(400).reset_index(drop=True)
    y2 = df["size"].head(400).reset_index(drop=True) if "size" in df.columns else y1
    fig, axs = plt.subplots(2)
    axs[0].plot(x, y1)
    axs[0].set_title('Tip vs Total Bill')
    axs[1].plot(x, y2, 'tab:orange')
    axs[1].set_title('Size vs Total Bill')
    plt.tight_layout()
    plt.show()
else:
    x = np.linspace(0, 2 * np.pi, 400)
    y1 = np.sin(x)
    y2 = np.cos(x)
    fig, axs = plt.subplots(2)
    axs[0].plot(x, y1)
    axs[0].set_title('Sine')
    axs[1].plot(x, y2, 'tab:orange')
    axs[1].set_title('Cosine')
    plt.tight_layout()
    plt.show()

# Customization: styles, annotations, etc.
plt.style.use('ggplot')
if df is not None and {"total_bill", "tip"}.issubset(df.columns):
    x = df["total_bill"].head(400).reset_index(drop=True)
    y1 = df["tip"].head(400).reset_index(drop=True)
    y2 = df["size"].head(400).reset_index(drop=True) if "size" in df.columns else y1
    plt.figure()
    plt.plot(x, y1, label='tip')
    plt.plot(x, y2, label='size')
    plt.title('Multiple Lines with Style')
    plt.xlabel('total_bill')
    plt.ylabel('value')
    plt.legend()
    plt.annotate('Max tip', xy=(x[y1.idxmax()], y1.max()), xytext=(x[y1.idxmax()], y1.max()+1),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()
else:
    x = np.linspace(0, 2 * np.pi, 400)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.figure()
    plt.plot(x, y1, label='sin(x)')
    plt.plot(x, y2, label='cos(x)')
    plt.title('Multiple Lines with Style')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.annotate('Max', xy=(np.pi/2, 1), xytext=(2, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()

# Save figure
if df is not None and "total_bill" in df.columns:
    plt.figure()
    plt.plot(df["total_bill"].head(100))
    plt.title('Saved Figure Example')
    plt.savefig('saved_figure.png')
    plt.close()
else:
    plt.figure()
    plt.plot(x, y1)
    plt.title('Saved Figure Example')
    plt.savefig('saved_figure.png')
    plt.close()
