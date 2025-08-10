# Price Predictor Application - Complete Documentation

## Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Core Features](#core-features)
4. [Technology Stack](#technology-stack)
5. [Database Models](#database-models)
6. [Machine Learning Models](#machine-learning-models)
7. [API Endpoints](#api-endpoints)
8. [User Interface](#user-interface)
9. [Data Flow](#data-flow)
10. [Business Logic](#business-logic)
11. [Installation & Setup](#installation--setup)
12. [Usage Guide](#usage-guide)
13. [File Structure](#file-structure)
14. [Security Features](#security-features)
15. [Future Enhancements](#future-enhancements)

---

## Overview

The **Price Predictor Application** is a comprehensive Django-based web application designed to predict agricultural commodity prices using machine learning algorithms. It serves as a decision-support system for government agencies, particularly the Ministry of Consumer Affairs, to manage buffer stock operations and monitor market price fluctuations.

### Key Objectives:

- Predict agricultural commodity prices using historical data
- Monitor price alerts and buffer stock thresholds
- Provide visualization of price trends across different states and seasons
- Support government decision-making for market interventions
- Enable real-time price data management and analysis

---

## System Architecture

### Architecture Pattern: MVC (Model-View-Controller)

- **Models**: Django ORM models for data persistence
- **Views**: Python functions handling business logic
- **Templates**: HTML templates for user interface
- **URLs**: Django URL routing system

### Components:

1. **Web Application Layer**: Django framework with HTML/CSS/JavaScript frontend
2. **Business Logic Layer**: Python views with ML model integration
3. **Data Layer**: SQLite database with Django ORM
4. **ML Layer**: Scikit-learn and XGBoost models for price prediction
5. **Visualization Layer**: Matplotlib and Plotly for data visualization

---

## Core Features

### 1. Price Prediction System

- **AI-Powered Predictions**: Uses ensemble of ML models (XGBoost, Linear Regression)
- **Multi-Factor Analysis**: Considers state, commodity, season, production, and year
- **Real-time Prediction**: Instant price predictions based on input parameters

### 2. Buffer Stock Management

- **Threshold Monitoring**: Tracks commodity prices against predefined thresholds
- **Alert System**: Identifies commodities with prices above threshold limits
- **Stock Tracking**: Manages buffer stock quantities for different commodities
- **Production Recommendations**: Suggests production levels based on historical data

### 3. Price Data Management

- **Data Entry**: Manual price fixing with AI-suggested values
- **Historical Data**: Maintains comprehensive price history
- **State-wise Tracking**: Monitors prices across different states
- **Date-based Filtering**: Current and historical price analysis

### 4. Visualization & Analytics

- **Interactive Graphs**: Price trend visualization using Matplotlib
- **Multi-dimensional Analysis**: State-commodity-season based charts
- **Time Series Analysis**: Year-over-year price trend analysis
- **Export Capabilities**: Graph generation for reports

### 5. Real-time Monitoring Dashboard

- **Live Price Alerts**: Current day's high-price commodities
- **Threshold Violations**: Automatic detection of price anomalies
- **Multi-state Tracking**: Consolidated view across states
- **Quick Navigation**: Easy access to all system functions

---

## Technology Stack

### Backend Technologies

- **Framework**: Django 5.1
- **Language**: Python 3.8+
- **Database**: SQLite3 (with MySQL support in README)
- **ORM**: Django ORM

### Machine Learning

- **Primary ML Library**: Scikit-learn
- **Ensemble Models**: XGBoost
- **Data Processing**: Pandas, NumPy
- **Model Serialization**: Joblib
- **Preprocessing**: Label Encoding

### Frontend Technologies

- **Template Engine**: Django Templates
- **CSS Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.0
- **JavaScript**: Vanilla JavaScript with AJAX

### Visualization

- **Chart Library**: Matplotlib (with Agg backend)
- **Interactive Plots**: Plotly Express
- **Graph Export**: Base64 encoding for web display
- **Styling**: Solarize_Light2 theme

### Data Sources

- **Primary Dataset**: Excel file (september_dataset.xlsx)
- **Features**: State, Commodity, Season, Production, Year, Price
- **Coverage**: Historical agricultural data for training models

---

## Database Models

### 1. CommodityData Model

```python
class CommodityData(models.Model):
    id = models.AutoField(primary_key=True)
    Date = models.DateField(default=timezone.now)
    Season = models.CharField(max_length=50)
    Commodity = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Production = models.FloatField()
    Price = models.FloatField()
```

**Purpose**: Stores historical and current commodity price data
**Key Features**: Auto-incrementing ID, date tracking, multi-dimensional categorization

### 2. BufferStock Model

```python
class BufferStock(models.Model):
    Commodity = models.CharField(max_length=100)
    stock = models.FloatField(null=True)
    threshold = models.FloatField(null=True)
```

**Purpose**: Manages buffer stock quantities and price thresholds
**Key Features**: Threshold-based alerting, stock quantity tracking

### Database Relationships

- One-to-many relationship between BufferStock and CommodityData through Commodity field
- Date-based filtering for current and historical analysis
- Index optimization on Date and Commodity fields for performance

---

## Machine Learning Models

### Model Architecture: Ensemble Approach

#### 1. XGBoost Model (Primary Predictor)

- **File**: `X.pkl`
- **Algorithm**: Gradient Boosting
- **Features**: State, Commodity, Season, Production, Year, Price_LR
- **Purpose**: Main price prediction with high accuracy

#### 2. Linear Regression Model (Auxiliary)

- **File**: `l.pkl`
- **Algorithm**: Linear Regression
- **Features**: Year, Commodity
- **Purpose**: Generates Price_LR feature for XGBoost model

### Feature Engineering

#### Label Encoders:

1. **State Encoder** (`state.pkl`): Encodes state names to numerical values
2. **Commodity Encoder** (`commodity.pkl`): Encodes commodity types
3. **Season Encoder** (`season.pkl`): Encodes seasonal information

#### Feature Processing Pipeline:

1. Input validation and type conversion
2. Label encoding of categorical features
3. Linear regression prediction for Price_LR
4. XGBoost ensemble prediction
5. Output normalization and validation

### Model Performance Features:

- **Real-time Prediction**: Sub-second response time
- **Error Handling**: Graceful handling of unknown categories
- **Scalability**: Efficient processing of batch predictions
- **Accuracy**: Ensemble approach for improved prediction quality

---

## API Endpoints

### Public Endpoints

#### 1. Home Dashboard

- **URL**: `/`
- **Method**: GET
- **View**: `home(request)`
- **Purpose**: Main dashboard with price alerts
- **Returns**: High-price commodities exceeding thresholds

#### 2. Price Prediction Interface

- **URL**: `/predict/`
- **Method**: GET
- **View**: `predict(request)`
- **Purpose**: Commodity price prediction form
- **Template**: `newpredict.html`

#### 3. Data Submission & Prediction

- **URL**: `/dataSubmition/`
- **Method**: POST
- **View**: `commodity_data_submission(request)`
- **Purpose**: Process prediction requests and display results
- **Input**: commodity, season, production, state
- **Output**: AI-predicted price with option to fix manually

#### 4. Price Fixing

- **URL**: `/fixprice/`
- **Method**: POST
- **View**: `price_fix(request)`
- **Purpose**: Save predicted or manually adjusted prices
- **Actions**: 'fix-estimated' or 'fix-price'

#### 5. Visualization

- **URL**: `/graph/`
- **Method**: GET
- **View**: `graph(request)`
- **Purpose**: Price trend visualization interface

#### 6. Graph Generation

- **URL**: `/graph-data/`
- **Method**: POST
- **View**: `graphs_plot(request)`
- **Purpose**: Generate and display price trend graphs
- **Input**: state, commodity
- **Output**: Base64-encoded matplotlib graph

#### 7. Buffer Stock Management

- **URL**: `/buffer-stock/`
- **Method**: GET
- **View**: `buffer_stock(request)`
- **Purpose**: Buffer stock monitoring and management
- **Features**: Threshold alerts, production recommendations

#### 8. Stock Updates

- **URL**: `/update-stock/`
- **Method**: POST
- **View**: `update_stock(request)`
- **Purpose**: Update buffer stock quantities
- **Format**: JSON API endpoint

### AJAX Endpoints

#### 9. Price Data API

- **URL**: `/get-price-data/<str:commodity>/`
- **Method**: GET
- **View**: `get_price_data(request, commodity)`
- **Purpose**: Fetch current day's price data for specific commodity
- **Returns**: JSON array with state-wise prices

---

## User Interface

### Design Philosophy

- **Government Portal Aesthetic**: Professional blue and white color scheme
- **Responsive Design**: Bootstrap 5.3.0 for mobile compatibility
- **Accessibility**: Clear navigation and readable fonts
- **User Experience**: Intuitive workflow for government officials

### Page Structure

#### 1. Main Dashboard (`newhome2.html`)

- **Header**: Ministry of Consumer Affairs branding
- **Navigation**: Quick access buttons to all features
- **Alerts Section**: Real-time price threshold violations
- **Statistics**: Summary of commodities and states monitored

#### 2. Prediction Interface (`newpredict.html`)

- **Input Form**: State, commodity, season, production fields
- **Validation**: Client-side and server-side input validation
- **Real-time Feedback**: Instant prediction results

#### 3. Price Fixing (`newprice_fix.html`)

- **Dual Options**: Accept AI prediction or set manual price
- **Confirmation**: Clear action buttons for decision making
- **Data Display**: Show all input parameters for verification

#### 4. Visualization (`newgraphs.html`)

- **Filter Controls**: State and commodity selection
- **Graph Display**: Interactive matplotlib charts
- **Data Analysis**: Year-season price trends
- **Export Options**: Save graphs for reporting

#### 5. Buffer Management (`newbuffer.html`)

- **Stock Overview**: Current buffer stock levels
- **Alert Management**: High-price commodity alerts
- **Action Items**: Recommended production levels
- **Update Interface**: Real-time stock quantity updates

### UI Components

- **Responsive Tables**: Sortable and filterable data displays
- **Modal Dialogs**: Confirmation and detail views
- **Progress Indicators**: Loading states for ML predictions
- **Error Handling**: User-friendly error messages
- **Success Notifications**: Confirmation of successful operations

---

## Data Flow

### 1. Prediction Workflow

```
User Input → Form Validation → Feature Encoding →
ML Model Prediction → Session Storage → Price Display →
User Decision → Database Storage
```

### 2. Buffer Stock Monitoring

```
Daily Price Data → Threshold Comparison → Alert Generation →
Production Analysis → Recommendation Display →
Stock Update Interface
```

### 3. Visualization Pipeline

```
User Selection → Data Filtering → Excel Data Loading →
Graph Generation → Base64 Encoding → Web Display
```

### 4. Data Management Flow

```
External Data Sources → Excel Import → Data Validation →
Database Storage → Model Training → Prediction Service
```

---

## Business Logic

### 1. Price Prediction Algorithm

```python
def getPrice_from_model(commodity, season, production, state):
    # Feature encoding
    encoded_features = encode_inputs(commodity, season, state)

    # Linear regression for auxiliary feature
    price_lr = lr_model.predict([year, commodity])

    # XGBoost ensemble prediction
    final_price = xgboost_model.predict(all_features)

    return final_price
```

### 2. Threshold Alert System

- **Daily Monitoring**: Automatic checking of current day's prices
- **Threshold Comparison**: Price vs. predefined thresholds
- **Alert Generation**: Identification of violation cases
- **Production Recommendation**: Historical data analysis for guidance

### 3. Buffer Stock Logic

- **Dynamic Thresholds**: Commodity-specific price limits
- **Multi-state Tracking**: Consolidated monitoring across regions
- **Historical Analysis**: 2022 production data for recommendations
- **Real-time Updates**: AJAX-based stock quantity management

### 4. Data Validation Rules

- **Input Validation**: Type checking and range validation
- **Business Rules**: Logical consistency checks
- **Error Recovery**: Graceful handling of invalid data
- **Data Integrity**: Foreign key relationships and constraints

---

## Installation & Setup

### Prerequisites

```bash
# System Requirements
Python 3.8+
Django 5.1
SQLite3 (or MySQL for production)

# Python Packages
pip install django pandas numpy scikit-learn xgboost matplotlib plotly joblib openpyxl
```

### Installation Steps

1. **Clone Repository**

```bash
git clone <repository-url>
cd PricePredictor_
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Database Setup**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Load Initial Data**

```bash
python manage.py loaddata initial_data.json  # If available
```

5. **Create Superuser**

```bash
python manage.py createsuperuser
```

6. **Run Development Server**

```bash
python manage.py runserver
```

### Configuration Files

- **Settings**: `pricepredictor/settings.py`
- **URLs**: `pricepredictor/urls.py` and `price/urls.py`
- **Models**: Pre-trained ML models in `price/templates/`
- **Data**: `september_dataset.xlsx` for historical analysis

---

## Usage Guide

### For Government Officials

#### 1. Daily Monitoring

- Access main dashboard to view price alerts
- Review commodities exceeding thresholds
- Check state-wise price variations

#### 2. Price Prediction

- Navigate to prediction interface
- Input commodity details (state, season, production)
- Review AI-generated price prediction
- Choose to accept or manually adjust price
- Save final price to database

#### 3. Buffer Stock Management

- Monitor current stock levels
- Review high-price commodity alerts
- Update stock quantities as needed
- Follow production recommendations

#### 4. Data Analysis

- Generate price trend graphs
- Analyze seasonal variations
- Compare state-wise performance
- Export charts for reporting

### For Data Administrators

#### 1. Data Maintenance

- Update historical datasets
- Retrain ML models periodically
- Manage threshold settings
- Monitor system performance

#### 2. User Management

- Create user accounts
- Assign permissions
- Monitor user activity
- Generate usage reports

---

## File Structure

```
PricePredictor_/
├── manage.py                     # Django management script
├── db.sqlite3                    # SQLite database
├── september_dataset.xlsx        # Historical data for analysis
├── README.md                     # Project documentation
├──
├── pricepredictor/               # Main Django project
│   ├── __init__.py
│   ├── settings.py               # Django configuration
│   ├── urls.py                   # Main URL routing
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
│
└── price/                        # Main application
    ├── __init__.py
    ├── admin.py                  # Django admin configuration
    ├── apps.py                   # App configuration
    ├── models.py                 # Database models
    ├── views.py                  # Business logic
    ├── urls.py                   # App URL routing
    ├── tests.py                  # Unit tests
    │
    ├── migrations/               # Database migrations
    │   ├── __init__.py
    │   ├── 0001_initial.py
    │   ├── 0002_alter_commoditydata_date.py
    │   ├── 0003_buffer.py
    │   ├── 0004_buffer_stock.py
    │   ├── 0005_bufferstock_delete_buffer.py
    │   ├── 0006_bufferstock_threshold_alter_bufferstock_commodity.py
    │   └── 0007_remove_commoditydata_district.py
    │
    └── templates/                # Frontend templates and ML models
        ├── newhome2.html         # Main dashboard
        ├── newpredict.html       # Prediction interface
        ├── newprice_fix.html     # Price fixing page
        ├── newgraphs.html        # Visualization page
        ├── newbuffer.html        # Buffer stock management
        ├── X.pkl                 # XGBoost model
        ├── l.pkl                 # Linear regression model
        ├── state.pkl             # State encoder
        ├── commodity.pkl         # Commodity encoder
        ├── season.pkl            # Season encoder
        └── [other legacy templates and models]
```

---

## Security Features

### 1. Django Security

- **CSRF Protection**: All forms protected with CSRF tokens
- **Session Management**: Secure session handling for user data
- **Input Validation**: Server-side validation for all user inputs
- **SQL Injection Prevention**: Django ORM protection

### 2. Data Security

- **Model File Protection**: ML models stored securely on server
- **Database Access Control**: Restricted database permissions
- **Error Handling**: No sensitive information in error messages
- **Session Security**: Temporary data storage in secure sessions

### 3. Application Security

- **Input Sanitization**: All user inputs validated and sanitized
- **File Upload Security**: Controlled file access and validation
- **XSS Prevention**: Template auto-escaping enabled
- **Authentication**: Admin interface protection

---

## Future Enhancements

### 1. Technical Improvements

- **Model Enhancement**: Regular retraining with new data
- **Performance Optimization**: Caching for frequently accessed data
- **API Development**: RESTful API for external integrations
- **Mobile App**: Native mobile application development

### 2. Feature Additions

- **Advanced Analytics**: Machine learning insights and trends
- **Notification System**: Email/SMS alerts for stakeholders
- **Multi-language Support**: Regional language support
- **Export Functionality**: PDF/Excel report generation

### 3. Integration Capabilities

- **External APIs**: Integration with market data providers
- **Government Systems**: Connection with existing government portals
- **Real-time Data**: Live market price feeds
- **Cloud Deployment**: Scalable cloud infrastructure

### 4. Business Intelligence

- **Predictive Analytics**: Long-term price forecasting
- **Market Analysis**: Comprehensive market trend analysis
- **Decision Support**: Advanced recommendation systems
- **Performance Metrics**: KPI dashboard for monitoring effectiveness

---

## Support and Maintenance

### 1. Regular Maintenance Tasks

- Database optimization and cleanup
- Model retraining with updated data
- Security updates and patches
- Performance monitoring and optimization

### 2. Monitoring and Logging

- Application performance monitoring
- Error tracking and reporting
- User activity logging
- System health checks

### 3. Backup and Recovery

- Regular database backups
- Model file versioning
- Configuration backup
- Disaster recovery procedures

---

## Conclusion

The Price Predictor Application represents a comprehensive solution for agricultural commodity price prediction and buffer stock management. By combining machine learning algorithms with user-friendly interfaces, it provides government agencies with the tools needed to make informed decisions about market interventions and stock management.

The application's modular architecture ensures scalability and maintainability, while its ensemble machine learning approach provides reliable price predictions. The intuitive user interface makes it accessible to government officials without technical backgrounds, while the robust backend ensures reliable operation in production environments.

With its focus on real-time monitoring, predictive analytics, and decision support, the Price Predictor Application serves as a valuable tool for maintaining market stability and ensuring food security through effective buffer stock management.

---

**Version**: 1.0  
**Last Updated**: August 2025  
**Developed for**: Ministry of Consumer Affairs  
**Technology**: Django + Machine Learning  
**Status**: Production Ready
