
# Importing necessary libraries
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression

#importing data
link="http://bit.ly/w-data"
df=pd.read_csv(link)

df.shape

df.head(10)

df.info()

df.describe()

df.isna().sum()

df=df.dropna()

df=df.drop_duplicates()

df.shape

x=df.Hours.values.reshape(-1,1)
y=df.Scores.values.reshape(-1,1)

#visualization
plt.scatter(x,y,c="red",s=50,marker="*")
plt.title("Scatter plot")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()

#train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25,random_state=0)
x_train

linearReg=LinearRegression()
linearReg.fit(x_train,y_train)

plt.scatter(x_train,y_train,c="green",s=50,marker="*")
plt.plot(x_train,linearReg.predict(x_train),color="red")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()

print("Coefficiennt of linear regression model : ",float(linearReg.coef_))
print("y-intercept of linear regression model : ",float(linearReg.intercept_))

print(f"Linear regression equation fitted is : y = {float(linearReg.coef_)} x + {float(linearReg.intercept_)}")

#predicting for test data
y_pred=linearReg.predict(x_test)
y_pred

#evaluation of the linear regression model
from sklearn.metrics import r2_score,mean_squared_error
print("The r-square value is : ",r2_score(y_pred,y_test))
print("The mean squred error is : ",mean_squared_error(y_pred,y_test))
print("The root mean squred error is : ",mean_squared_error(y_pred,y_test,squared=False))

