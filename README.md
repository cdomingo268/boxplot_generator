Instructions
 - Save in desired location:
   1. `boxplot_generator`
   2. User designed `.csv` file as input.
 - Open new terminal at folder location and enter command: `python bad_boxplot_generator.py`
 - Inputs:
   1. `.csv` filepath and name.
   2. outlier maximum (values > input are excluded from data).
 - Outputs two .png files:
   1. boxplot with outliers; saved-filename formated as `ddmmyyyy figure with outliers.png`, where 'ddmmyyyy' represents final day of reported treatment.
   2. boxplot without outliers; filename fromated as `ddMmmYYYY figure without outliers > x.png`, where 'ddmmyyyy' represents final day of reported treamtment and 'x' represents maximum data point range.

Notes:
- Jupyter Notebook (bad_box_lot_generator_tutorial.ipynb) file contains methods for updating and improving functionality.
- Example comma-separated value file describes key sensitive row/column data for input.
