import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#data
df = pd.read_excel("semiconductor-ml/Data/semiconductor_data.xlsx")

#target
target = "Energy_Gap (eV)"

categorical_features = ["Crystal_Structure"]

df_encoded = pd.get_dummies(
    df,
    columns=categorical_features,
    drop_first=False
)

#features
numeric_features = df.columns.drop(["Material (x=0.3)",target,"Crystal_Structure"])
crystal_columns = [col for col in df_encoded.columns if col.startswith("Crystal_Structure_")]

feature_columns = list(numeric_features) + crystal_columns

#split
X = df_encoded[feature_columns]
y = df_encoded[target]

model = RandomForestRegressor(
    n_estimators = 500,
    random_state = 42
)

model.fit(X, y)

#cross-validation
Leave_One_Out = LeaveOneOut()

y_pred = cross_val_predict(
    model,
    X,
    y,
    cv=Leave_One_Out
)
#metric
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)

#create feature importance table
importance = pd.DataFrame({
    "Feature": feature_columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print(importance)

#Sort by error
results = pd.DataFrame({
    "Material": df["Material (x=0.3)"],
    "Actual_Energy_Gap": y,
    "Predicted_Energy_Gap": y_pred,
    "Error": abs(y - y_pred)
})

results_sorted = results.sort_values(by="Error", ascending=False)

print(results_sorted)

# Scatter plot
plt.figure(figsize=(8, 6))

plt.scatter(y, y_pred)

# Perfect prediction line
min_value = min(y.min(), y_pred.min())
max_value = max(y.max(), y_pred.max())

plt.plot([min_value, max_value], [min_value, max_value])

plt.xlabel("Actual Energy Gap (eV)")
plt.ylabel("Predicted Energy Gap (eV)")
plt.title("Actual vs Predicted Energy Gap")

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


#plot feature importance
plt.figure(figsize=(9, 5))
plt.barh(importance["Feature"], importance["Importance"])
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Random Forest Feature Importance for Energy Gap Prediction")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

#plot error by material
plt.figure(figsize=(9, 5))
plt.barh(results_sorted["Material"], results_sorted["Error"])
plt.xlabel("Absolute Error (eV)")
plt.ylabel("Material")
plt.title("Prediction Error by Material")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
