##CSV -> Graph Converter, Solomon Harkins, 5/3/2025
from pathlib import Path
import csv
from matplotlib import pyplot as plt
from datetime import datetime

path = Path.cwd() / 'OHUR.csv'
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)


x_val, y_val = [], []
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    high = float(row[1])
    x_val.append(current_date)
    y_val.append(high)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(x_val, y_val, color='green')

for index, axis in enumerate(header_row):
    if index==0:
        x_label = axis
    else:
        y_label = axis

ax.set_title(f"{y_label} in relation to {x_label}", fontsize=24)
ax.set_xlabel(x_label, fontsize=16)
ax.set_ylabel(y_label, fontsize=16)
ax.tick_params(labelsize=16)

plt.show()