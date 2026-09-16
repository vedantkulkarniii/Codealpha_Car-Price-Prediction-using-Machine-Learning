# Baseline Model Check

## Evaluation setup

The model comparison used an 80/20 train-test split with random_state=42 and a preprocessing pipeline that handled both numeric and categorical features.

## Validation results

| Model | MAE | RMSE | R-squared |
| --- | ---: | ---: | ---: |
| Linear Regression | 77,734.56 | 99,990.42 | 0.6889 |
| Gradient Boosting | 88,811.57 | 115,716.09 | 0.5833 |
| Random Forest | 98,038.98 | 124,826.51 | 0.5151 |

## Conclusion

Linear Regression remains the best-performing baseline model on the validation split. It delivers the lowest MAE and RMSE and the highest R-squared. This supports the project direction to continue with regression-focused modeling and further feature refinement.
