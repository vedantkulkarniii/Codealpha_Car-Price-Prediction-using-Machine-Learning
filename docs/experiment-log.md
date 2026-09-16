# Experiment Log

Each model experiment will record the features used, preprocessing, model settings, metrics, and conclusion.

This prevents results from being remembered only informally and makes comparisons reproducible.

## Initial Model Comparison

- Split: 80/20 train/test split with `random_state=42`
- Features: vehicle attributes plus `car_age`
- Preprocessing: training-set median imputation for numeric columns, most-frequent imputation for categorical columns, and one-hot encoding inside a pipeline

| Model | MAE | RMSE | R-squared |
| --- | ---: | ---: | ---: |
| Linear Regression | 77,734.56 | 99,990.42 | 0.6889 |
| Gradient Boosting | 88,811.57 | 115,716.09 | 0.5833 |
| Random Forest | 98,038.98 | 124,826.51 | 0.5151 |

Linear Regression performed best on this split and remains the leading candidate. The validation result confirms that it yields the lowest MAE and RMSE and the highest R-squared among the tested models.

## Decision

The project will continue with a regression-focused workflow around the linear baseline, while exploring targeted feature engineering improvements such as price-normalized mileage, brand-level effects, and a more explicit age signal.
