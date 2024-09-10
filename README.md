## Instructions
 - Save in desired location:
   1. `boxplot_generator` folder OR `boxplot_generator.py` python file only.
   2. user `.csv` file as input.
 - Open new terminal at desired folder location and enter command: `python boxplot_generator.py`
 - Inputs:
   1. `.csv` filepath/name.
   2. outlier - maximum (values > input are excluded from data).
 - Outputs two .png files:
   1. boxplot with outliers; saved-filename formated as `ddmmyyyy figure with outliers.png`, where 'ddmmyyyy' represents final day of reported treatment.
   2. boxplot without outliers; filename fromated as `ddMmmYYYY figure without outliers > x.png`, where 'ddmmyyyy' represents final day of treatment and 'x' represents maximum data point.

## Notes:
- Jupyter Notebook (boxplot_generator.ipynb) file contains example usage.
- Example comma-separated value (measurements.csv) file illustrates key-sensitive column names: `date`, 	`type`, 	`cage_num`, 	`width_mm`, `length_mm`,	`area_mm^2`, and `note`.
