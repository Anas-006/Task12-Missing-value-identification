import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()
df=pd.DataFrame(
    iris.data,
    columns=["Sepal length","Sepal width","Petal lenght","Petal width"]
)
missing_values=df.isnull().sum()
print("Missing values")
print(missing_values)