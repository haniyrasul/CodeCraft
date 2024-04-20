* Classification is another major area of machine learning problem solutions, which has two major divisions:
	1. Binary Classification: either 0 or 1
	2. Multi-Class Classification: multiple classes 
*  Covered binary classification, utilizing the Telecom Customer Churn Dataset.
## EDA
* Check missing values
* Look at the target variable (churn)
* Loot at numerical and categorical variables
* Feature Importance: Crucial aspect in this analysis
	* Churn rate: difference between the mean of the group of local variable with global churn mean value (Eg: df_group_gender['mean'] - global_churn )
	* Risk ratio: similar to the churn rate, not the difference but divided by the global_churn_mean
	* Mutual Information: How much we can learn about one variable (eg: Churn) if we know the value of another.
		* Scikit-Learn has the metric: mutual_info_score
*  Correlation: 
	* 0.0 - +/-0.2: LOW (Rarely)
	* +/-0.2 - +/-0.5: MODERATE (Sometimes)
	* +/- 0.6 - +/- 1.0: STRONG (Often/Always) 
* One-Hot Encoding
	* Encode categorical feature: used DictVectorizer from Scikit-Learn
* Logistic Regression Applied
	* intercept: value of the linear predictor when all covariates are zero
	* coef: determine the relationship between input and output variables in a model. It learned during training and used to make predictions on new data

## Summary
* Feature importance - risk, mutual information, correlation
* one-hot encoding can be implemented with DictVectorizer
* Logistic Regression - linear model like linear regression
* output of log reg - probability
* Interpretation of weights is similar to linear regression
