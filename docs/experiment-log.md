# Experiment Log

Each model experiment will record the features used, preprocessing, model settings, metrics, and conclusion.

This prevents results from being remembered only informally and makes comparisons reproducible.

## Initial Model Comparison

- Split: 80/20 train/test split with `random_state=42`
- Features: vehicle attributes plus `car_age`
- Preprocessing: training-set median imputation for numeric columns, most-frequent imputation for categorical columns, and one-hot encoding inside a pipeline

| Model | MAE | RMSE | R-squared |
| --- | ---: | ---: | ---: |
| Linear Regression | 80,277.67 | 104,713.83 | 0.6588 |
| Gradient Boosting | 88,946.24 | 115,636.93 | 0.5839 |
| Random Forest | 97,450.75 | 123,817.80 | 0.5229 |

Linear Regression performed best on this split. Five-fold shuffled cross-validation produced the following mean metrics:

| Model | Mean CV MAE | Mean CV RMSE | Mean CV R-squared |
| --- | ---: | ---: | ---: |
| Linear Regression | 77,983.48 | 98,216.19 | 0.6935 |
| Gradient Boosting | 82,896.78 | 105,385.69 | 0.6471 |
| Random Forest | 92,722.53 | 115,422.78 | 0.5753 |

Linear Regression remains the leading candidate across both evaluation methods. Additional data-quality checks and error analysis are still needed before selecting a final model.
