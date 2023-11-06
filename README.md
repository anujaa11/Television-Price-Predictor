## Television-Price-Predictor ##

# Overview:
This Python project predicts television prices using data scraped from Flipkart. It provides a practical solution for consumers and businesses to estimate TV prices based on product features.

# Data Extraction
I've implemented a data extraction script named "Data extraction.ipynb" to scrape product data from Flipkart, capturing details such as product name, brand, operating system, launch year, and, most importantly, prices. The scraped data is saved in "Dataset.csv."

## Data Preprocessing and Model Prediction

In the "tv-price-predictor.ipynb" Jupyter Notebook, I've performed data preprocessing to prepare the dataset for analysis and modeling. The cleaned and structured data is stored in "data_cleaning.csv." Preprocessing tasks included handling missing values, removing unnecessary columns, and more.
Additionally,I have developed a machine learning model within the same notebook for price prediction. This model uses the preprocessed data to make price predictions based on television features. Regression techniques have been used in building this model.

## Application (app.py):
I've created a user-friendly web application using Streamlit in "app.py." It allows you to input television details for price predictions.

## Important Files
df.pkl: Stores the preprocessed dataset for the machine learning model.
pipe.pkl: Contains the trained model for estimating television prices.

## Acknowledgments
CampusX YouTube Channel: The educational content and insights from this channel played a significant role in shaping the development of this project, and I learned a great deal from their content.



