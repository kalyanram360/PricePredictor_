
# Price Predictor

Price Predictor is a machine learning-based system that forecasts the prices of agricultural commodities. It provides actionable insights to aid in buffer stock management and government decision-making. The system considers key factors like production seasonality, location, and real-time conditions to predict prices accurately.

---
## Demo

Watch the demo video:

<a href="https://youtu.be/uCl1GdoNyhQ" target="_blank">
    <img src="https://img.youtube.com/vi/uCl1GdoNyhQ/0.jpg" alt="Price Predictor Demo" style="width:100%;max-width:640px;">
</a>


## Features

- **Price Prediction**: Predicts prices of agri-horticultural commodities such as pulses and vegetables.
- **Data Analysis**: Utilizes production data, climatic conditions, and seasonality for predictions.
- **Government Alerts**: Sends alerts for buffer stock management based on predicted price trends.
- **Scalable Deployment**: Deployed across 550 data centers for real-time analysis and insights.

---

## Technology Stack

### Backend
- **Python**: Core programming language.
- **Django**: For web-based interface and API integration.

### Machine Learning Models
- **Random Forest**
- **XGBoost** (with hyperparameter tuning)
- **Linear Regression**

### Data Processing
- **Pandas**: Data manipulation.
- **NumPy**: Numerical computations.
- **Matplotlib/Seaborn**: Data visualization.

### Database
- **MySQL**: Stores historical data and predictions.

### Deployment
- Scalable multi-center deployment with API integration.

---

## Dataset

- **Features Used**:
  - State
  - Commodity
  - Season
  - Production
  - Year
- Preprocessing: Label encoding for categorical variables.

---

## Installation and Usage

### Prerequisites
- Python 3.8+
- Django
- MySQL
- Required Python libraries: `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `xgboost`.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pricepredictor.git
   cd pricepredictor
