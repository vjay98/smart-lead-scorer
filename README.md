# AI-Readiness Lead Generation Challenge 🚀

## Overview
This project enhances Caprae Capital’s lead generation tool by using machine learning to identify AI-ready companies based on size, growth, and maturity.

## Features
- Data cleaning and normalization
- Feature engineering (`lead_score`)
- KMeans clustering to segment companies
- Top 5% lead extraction from high-potential clusters
- CSV export of qualified leads

## Dataset
- Source: [Kaggle - 7M+ Companies](https://www.kaggle.com/datasets/farhanmd29/companies-dataset)
- Key features: `year_founded`, `current_employee_estimate`, `growth_estimate`, `location`, `domain`

## Setup
```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
streamlit run app.py
```

## 🚀 Live Demo

Check out the live app here 👉 [Streamlit App](https://smart-lead-scorer-bdp8qymwgtfb6mzcmrk4app.streamlit.app/)
