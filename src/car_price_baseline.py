from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "raw" / "car_sales.csv"
PROCESSED_PATH = ROOT / "data" / "processed" / "car_sales_processed.csv"
MODEL_PATH = ROOT / "models" / "linear_regression_baseline.joblib"
RESULTS_PATH = ROOT / "models" / "baseline_model_results.csv"


def load_and_prepare_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["car_age"] = df["year"].max() - df["year"]

    for column in ["mileage_km", "engine_cc"]:
        df[column] = df[column].fillna(df[column].median())

    for column in ["fuel_type", "transmission"]:
        df[column] = df[column].fillna(df[column].mode().iloc[0])

    df = df.copy()
    df.to_csv(PROCESSED_PATH, index=False)
    return df


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    numeric_columns = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = [column for column in X.columns if column not in numeric_columns]

    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
    ])

    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_transformer, numeric_columns),
            ("categorical", categorical_transformer, categorical_columns),
        ]
    )


def evaluate_models() -> pd.DataFrame:
    df = load_and_prepare_data()
    X = df.drop(columns=["price"])
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    preprocessor = build_preprocessor(X_train)
    models = {
        "Linear Regression": LinearRegression(),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(random_state=42, n_estimators=300),
    }

    results = []

    for name, model in models.items():
        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model),
            ]
        )

        pipeline.fit(X_train, y_train)
        predictions = pipeline.predict(X_test)

        result = {
            "model": name,
            "mae": mean_absolute_error(y_test, predictions),
            "rmse": (mean_squared_error(y_test, predictions)) ** 0.5,
            "r2": r2_score(y_test, predictions),
        }
        results.append(result)

        if name == "Linear Regression":
            joblib.dump(pipeline, MODEL_PATH)

    metrics = pd.DataFrame(results).sort_values("mae", ascending=True)
    metrics.to_csv(RESULTS_PATH, index=False)
    return metrics


if __name__ == "__main__":
    metrics = evaluate_models()
    print(metrics.to_string(index=False))
