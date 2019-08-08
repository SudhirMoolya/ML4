import numpy as np
import pandas as pd

x_mse = [15,12,8,8,7,7,7,6,5,3]
y_ese = [10,25,17,11,13,17,20,13,9,15]

x = pd.Series(x_mse)
y = pd.Series(y_ese)

r = x.cov(y)/(x.std()*y.std())

beta1 = (r*y.std())/x.std()

print("The slope of line of regressoin is:","%.3f"%beta1)

----------------------------------------------------------------------------------------------------------------

OUTPUT:
The slope of line of regressoin is: 0.208
