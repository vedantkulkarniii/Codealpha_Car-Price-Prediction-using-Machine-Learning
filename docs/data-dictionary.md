# Data Dictionary

This dataset records used-car listings and is designed for a regression task where `price` is the target variable.

| Column | Meaning | Type | Unit | Role |
|---|---|---|---|---|
| `brand` | Manufacturer brand of the vehicle | Categorical | - | Feature |
| `model` | Specific model name | Categorical | - | Feature |
| `year` | Manufacturing year | Integer | year | Feature |
| `mileage_km` | Distance travelled by the vehicle | Numeric | km | Feature |
| `fuel_type` | Fuel type used by the vehicle | Categorical | - | Feature |
| `transmission` | Automatic or manual gearbox | Categorical | - | Feature |
| `engine_cc` | Engine displacement | Numeric | cc | Feature |
| `seats` | Passenger seating capacity | Integer | seats | Feature |
| `owner_count` | number of prior owners | Integer | owners | Feature |
| `price` | Selling price of the car | Numeric | currency | Target |

## Data-quality notes

- The dataset contains 600 rows and 10 columns.
- The target column, `price`, has no missing values.
- Missing values appear in `mileage_km`, `fuel_type`, `transmission`, and `engine_cc` and will be handled during preprocessing.
- Price values are relatively broad, suggesting the regression task will benefit from a well-structured preprocessing pipeline and careful validation.
