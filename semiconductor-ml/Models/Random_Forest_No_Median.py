import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

#With median data
df = pd.read_excel("semiconductor-ml/Data/semiconductor_data_no_median.xlsx")

#check data
"""
print(df.columns)
print(df.head)
"""

#choose features / target
target_column = "Energy_Gap (eV)"
feature_columns = df.columns.drop(["Material (x=0.3)", target_column])

#Cross-validation
X = df[feature_columns]
y = df[target_column]

#check data
"""
print(X.shape)
print(y.shape)
"""

#random forest model
model = RandomForestRegressor(
    n_estimators = 500,
    random_state = 42
)

#cross-validation method#
"""
train on all materials except 1, test on 1 material left out, 
repeat for all"""
leave_one_out = LeaveOneOut()

#runs cross-validation
y_pred = cross_val_predict(
    model,
    X,
    y,
    cv = leave_one_out
)

#metric
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print("Random Forest Metrics")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)

#graph
import matplotlib.pyplot as plt
import numpy as np

# Actual vs Predicted Scatter Plot
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calculate metrics
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

# Scatter plot
plt.figure(figsize=(8, 6))

plt.scatter(y, y_pred)

# Perfect prediction line
min_value = min(y.min(), y_pred.min())
max_value = max(y.max(), y_pred.max())

plt.plot([min_value, max_value], [min_value, max_value])

plt.xlabel("Actual Energy Gap (eV)")
plt.ylabel("Predicted Energy Gap (eV)")
plt.title("Actual vs Predicted Energy Gap (w/o median)")

# Add metrics text box
text = f"MAE = {mae:.3f}\nRMSE = {rmse:.3f}\nR² = {r2:.3f}"

plt.text(
    0.05,
    0.95,
    text,
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

plt.show()