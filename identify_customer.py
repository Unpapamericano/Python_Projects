import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.tree import DecisionTreeClassifier

# Load the data into a dataframe
df = pd.read_csv("customer_data.csv")

# Handle missing values
df = df.fillna(0)

# Correct errors
df["contract_expiration_date"] = df["contract_expiration_date"].apply(lambda x: x if x != "N/A" else "2022-12-31")

# Format data consistently
df["contract_expiration_date"] = pd.to_datetime(df["contract_expiration_date"])



# Plot a histogram of contract expiration dates
plt.hist(df["contract_expiration_date"], bins=50)
plt.xlabel("Contract Expiration Date")
plt.ylabel("Number of Customers")
plt.show()

# Split the data into training and test sets
X = df[["age", "income", "num_contracts"]]
y = df["contract_expiring"]
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

# Build the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)
precision = sklearn.metrics.precision_score(y_test, y_pred)
recall = sklearn.metrics.recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
