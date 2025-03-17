# **Car Price Prediction 🚗💰**  
**Tech Used:** Python, Web Scraping, Seaborn, Scikit-learn, Linear Regression, RandomForest, GridSearchCV  

## **📌 Overview**  
This project focuses on predicting car prices to help buyers and sellers make informed decisions. The dataset was collected via web scraping from CarDekho, followed by exploratory data analysis (EDA), model building, and optimization.  

Despite multiple challenges during the process (including data scraping issues, overfitting, and feature selection), the project provided valuable hands-on learning in real-world data science applications.  

---

## **🔄 Project Workflow**  

**1. Web Scraping & Data Collection**  
- Scraped 50,000+ car listings from CarDekho.  
- Used 6,000 listings for model training after data cleaning.  

**2. Data Cleaning & Preprocessing**  
- Handled missing values & duplicates (initially overlooked, later corrected).  
- Transformed categorical features into numerical representations.  

**3. Exploratory Data Analysis (EDA)**  
- Identified key price-driving factors (brand, model, year, mileage, etc.).  
- Discovered multicollinearity, leading to feature selection adjustments.  

**4. Model Building & Evaluation**  
- Linear Regression initially showed R² = 1, which was overfitting.  
- Implemented Ridge Regression to mitigate overfitting.  
- Used RandomForest for improved predictive performance.  

**5. Hyperparameter Tuning**  
- Applied GridSearchCV for optimization.  
- Tuned parameters to balance bias-variance tradeoff.  

**6. Challenges & Fixes**  
- Overlooked duplicate values in data cleaning, leading to early noise.  
- Web scraping issue caused only one page of data to be collected (later fixed).  
- Model tuning struggles—removing multicollinearity degraded performance instead of improving it.  

**7. Key Learning**  
- Data validation is crucial—scraping errors can lead to incomplete datasets.  
- Overfitting detection is key—a perfect R² is usually a red flag.  
- Fixing assumptions early saves time—intuition-based decisions often lead to mistakes.  

---

## **🚀 Next Steps**  
🔹 Fix pagination in web scraping & collect the full dataset.  
🔹 Re-run data analysis & model training with improved data.  
🔹 Test additional models (e.g., XGBoost, Lasso Regression) for better predictions, which I have to learn how to work with it.  

---

## **📎 Final Thoughts**  
This project was a real-world learning experience, reinforcing that mistakes are part of the journey. Even though the model isn't perfect yet, understanding where things went wrong is just as important as getting them right.  

🚀 **Will continue refining this project—stay tuned!**  