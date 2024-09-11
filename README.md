## Instructions
 - Save in desired location:
   1. 'dataviz_generator' folder OR 'dataviz_generator.py' python file only.
   2. user `.csv` file as input.
 - Open new terminal at desired folder location and enter command: 'python dataviz_generator.py'
 - Inputs:
   1. '.csv' filepath/name.
   2. boxplot (or lineplot) - input 'b' or 'l'.
   3. yes (or no) outliers - input 'y' or 'n'.
   4. (optional, if 'n' for input 3) maximum data point to include (values > input are excluded from data).
 - Outputs .png file:
   1. plot with outliers; file saved and formated as `{ddmmyyyy figure} with outliers.png`, where {ddmmyyyy figure} represents final day of reported treatment and figure represents user specified plot.
   2. plot without outliers; `{ddMmmYYYY figure} without outliers > {x}.png`, where {x} represents maximum data point.

## Notes:
- Jupyter Notebook (boxplot_generator.ipynb) file contains example usage.
- Example comma-separated value (measurements.csv) file illustrates key-sensitive column names: `date`, 	`type`, 	`cage_num`, 	`width_mm`, `length_mm`,	`area_mm^2`, and `note`.
