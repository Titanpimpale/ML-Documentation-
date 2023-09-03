Today I learned about multiple linear regression, in MLR we can predict values using more than one varible.

Model prediction with Multiple variable:

![Screenshot 2023-09-03 090227](https://github.com/Titanpimpale/ML-Documentation-/assets/109168200/93c10f99-4762-4ef3-a5f0-0c94c3aabe12)

Let me explain multiple linear regression using example

![mlr](https://github.com/Titanpimpale/ML-Documentation-/assets/109168200/1150f0fd-8554-4c64-8c4d-8db4ad4c6fcf)

1. import pandas: 
   importing important libraries

2.df = pandas.read_csv("data.csv"): 
   Reading your csv file using pandas module (csv files are your data)

3. X = df[['engine', 'cylinders']]
   y = df['CO2']: 
     assigning variable

4. regr = linear_model.LinearRegression()
regr.fit(X, y): 
    fit() takes two variables and fill regression object
5. predictedCO2 = regr.predict([[2300, 1300]]): 
     now regression model is filled we can predict co2 emmission with two variable i.e engine and cylinder 

Hope you like my Multi linear regression doc,  thank you 🙏 
 
   
