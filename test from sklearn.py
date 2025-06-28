from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def run_model(df):
    features = ['vehicle_id', 'date']  # You can add more features here
    target = 'rpm'

    X = df[features]
    y = df[target]

    # Handle categoricals (e.g., vehicle_id)
    preprocessor = ColumnTransformer([
        ('vehicle', OneHotEncoder(handle_unknown='ignore'), ['vehicle_id'])
    ], remainder='passthrough')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('model', GradientBoostingRegressor())
    ])

    pipeline.fit(X_train, y_train)
    print("✅ Model trained. Score on test set:", pipeline.score(X_test, y_test))
