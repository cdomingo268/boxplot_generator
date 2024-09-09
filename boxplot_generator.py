# Importing pandas and matplotlib
import pandas as pd
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import seaborn as sns

# add dataframe column 'day' to represent the number of days since start of treatment
# return final day of treatment for filesaving
def add_days_column(dframe):
    start_date = datetime.strptime(dframe.loc[0,'date'], "%m/%d/%y") # datetime object for start of treatment
    final_date = datetime.strptime(dframe.iloc[-1,0], "%m/%d/%y").strftime('%d%b%Y') # datetime object for start of treatment
    for i in measurements_df.index:
        timedelta = int((datetime.strptime(dframe.loc[i,'date'], "%m/%d/%y") - start_date).days)
        dframe.loc[i, 'day'] = timedelta

    return final_date

# define a function that generates boxplot to compare `Test` vs `Control` group
def boxplot_generator(dframe, outliers=True): # input dframe(DataFrame), outlier(boolean)
    
    if outliers == False:
        x = int(input('Enter maximum value (area_mm^2): '))
        dframe = dframe[dframe['area_mm^2'] <= x]
    
    ax = sns.catplot(data=dframe, kind='box', x='day', y='area_mm^2', hue='type', native_scale=True)
       
    if outliers == True:
        ax.set(xlabel='Days from Start of Treatment', ylabel='Area (mm^2)', title='Test vs Control (blue) with Outliers')
        plt.savefig('{} figure with outliers.png'.format(last_day), dpi=500)
    else:
        plt.savefig('{} without outliers > {}'.format(last_day, x), dpi=500)
        ax.set(xlabel='Days from Start of Treatment', ylabel='Area (mm^2)', title='Test vs Control (blue) w/o Outliers > {}'.format(x))
    
    return None
    
# Read in the data collection CSV as a DataFrame
unfiltered_measurements_df = pd.read_csv(input('Enter filepath for .csv file: '))
measurements_df = unfiltered_measurements_df[pd.isna(unfiltered_measurements_df['date']) == False] # remove last NaN row

#Test func
last_day = add_days_column(measurements_df);
boxplot_generator(measurements_df, outliers=False);
boxplot_generator(measurements_df);
