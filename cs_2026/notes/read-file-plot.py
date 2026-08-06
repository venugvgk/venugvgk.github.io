from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
script_dir = Path(__file__).resolve().parent
excel_file = script_dir / 'data.xlsx'

if not excel_file.exists():
    raise FileNotFoundError(f"Could not find Excel file: {excel_file}")

df = pd.read_excel(excel_file)

# Extract data for bar graph
# Assuming first column is labels and second column is values
labels = df.iloc[:, 0]
values = df.iloc[:, 1]

# Create bar graph
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='steelblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph from Excel Data')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
