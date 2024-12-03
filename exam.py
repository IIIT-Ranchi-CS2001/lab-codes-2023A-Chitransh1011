#SET-2
import pandas as pd
import numpy as np
df = pd.read_csv('AQI_Data (1).csv')

print("First 5 rows of dataset : ")
# Display the first 5 rows
print(df.head())
print("Last 6 rows of rows : ")

#Display the last 6 rows
print(df.tail(6))

#Show the summary statistics for all numeric columns
x = df.describe()
print(x)

# Use NumPy to compute the mean AQI,PM2.5,and PM10 values for each city
AQI_MEAN = np.mean(df['AQI'])
PM1_MEAN = np.mean(df['PM2.5'])
PM2_MEAN = np.mean(df['PM10'])
print("Mean of AQI_MEAN : ",AQI_MEAN)
print("Mean of PM2.5_MEAN : ",PM1_MEAN)
print("Mean of PM10_MEAN : ",PM2_MEAN)


# Check for missing values in the dataset and Replace missing values in numeric columns with the column mean if missing values are found
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)
if missing_values.sum() == 0:
    print("No missing values found in the dataset.")
else:
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        if df[column].isnull().sum() > 0:  
            mean_value = df[column].mean()
            df[column].fillna(mean_value, inplace=True)
    print("Updated DataFrame after replacing missing values:")
    print(df)



# Extract the AQI column as a NumPy array , Calculate mean, median, and standard deviation of AQI values
aqi_values = df['AQI'].to_numpy()
aqi_mean = np.mean(aqi_values)
aqi_median = np.median(aqi_values)
aqi_std_dev = np.std(aqi_values)
print("Statistics for AQI values:")
print("Mean AQI:", aqi_mean)
print("Median AQI:", aqi_median)
print("Standard Deviation of AQI:", aqi_std_dev)






