<h1 align='center'>  Medical Insurance Cost Prediction ML Project </h1>

**Welcome to the Medical Insurnace Project Repository!** 🏥💉
<br><br>

This project focuses on the medical insurance domain, aiming to provide predictions related to health insurance premiums. SkyHigh Shield, a fictitious healthcare company, explores a dataset containing information about individuals' demographics, lifestyle choices, and medical history.

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1154429779982942258/1202707531546239046/app_screenshot_demo.png?ex=65ce6fac&is=65bbfaac&hm=8a50701c48e18a85629d158250389360b2573e1070b7dd63ddea87ebe20880cb&"  title="app demo image">
</p>
<hr>

## Project Overview 🚀
This project involves the development and deployment of a machine learning model to predict insurance charges based on various features such as age, gender, BMI, number of children, smoking habits, and region. The model is trained on a dataset containing historical insurance data.

## Tools and Technologies Used 🛠️
- Python
- Jupyter Notebook
- Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- Statsmodels
- Pickle (for model serialization)
  
## Project Steps 📑
### Step 1: Data Loading and Cleaning
- Imported necessary libraries.
- Read the insurance dataset (insurance.csv) into a Pandas DataFrame.
- Checked the structure of the dataset and performed initial cleaning.
  
### Step 2: Outlier Removal
- Checked for outliers in the 'bmi' column using the IQR method.
- Removed outliers from the 'bmi' column.
  
### Step 3: Duplicate Row Removal
- Removed duplicate rows from the dataset.
  
### Step 4: Data Preparation
- Separated input and output columns.
- Split the dataset into training and testing sets.

### Step 5: Outlier Adjustment
- Removed instances where insurance charges were greater than 50,000.

### Step 6: Log Transformation
- Applied a log transformation to the insurance charges to handle skewness.

### Step 7: Pipeline Creation
- Created a data processing pipeline using sklearn to handle imputation, encoding, polynomial features, scaling, and model fitting.

### Step 8: Model Training
- Trained a linear regression model using the pipeline.

### Step 9: Model Evaluation
- Evaluated the model on the test set, achieving an R-squared score of approximately 0.83.

### Step 10: Model Serialization
- Exported the trained model using Pickle for future use.

### Step 11: Model Deployment
- Loaded the deployed model and tested it with a sample input to predict insurance charges.

## Project Completion 🎉
The insurance model has been successfully developed, trained, and deployed. It provides accurate predictions for insurance charges based on input features. Feel free to use the deployed model for predicting insurance charges with new data.
<br>
<br>
<br>
**Note:** 
1. The model file (insurance_model.pkl) is available in the repository for future use.
2. To create a new environment, refer to the syntax provided in the 'cmd note.txt' file in this repository.
<br>
<hr>
<h4 align='center'> <i>Thank you for exploring this Insurance Model Deployment Project! Contributions and feedback are always welcome. Cheers to successful predictions! 🚀💼</i></h4>

