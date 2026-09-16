# Next Feature Experiments

The current linear regression baseline is performing better than the tree-based alternatives. The next experiments should therefore focus on improving interpretability and prediction accuracy without abandoning the baseline approach.

## Planned directions

- Add `car_age` and mileage-adjusted variants to reflect depreciation more explicitly.
- Compare brand-level and model-level effects with a controlled encoding strategy.
- Test whether a mileage-to-age ratio improves over raw mileage usage.
- Confirm whether the current missing-value strategy is stable on validation folds.

## Success signal

The next feature iteration should reduce validation MAE without making the model materially less interpretable.
