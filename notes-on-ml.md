# notes on ML

## decision trees

You can use decision trees for both classification and regression. The output leaf nodes would either contain a value (classification) or a number (regression). For regression, the number comes from the data and is an average of all data points that ended up at that leaf node. For classification, the label is the label of the majority of data points that ended up at that leaf node.

A "random" decision tree is where you force randomness when picking which attribute to split on.

A "random forest" is just a bunch of "random" decision trees. It reduces overfitting by aggregating the results of multiple trees. A random forest model is an ensemble model. In order to have different trees trained, you need multiple datasets. That's where bagging or bootstrap aggregating comes into play. Bagging creates many datasets from one dataset through sampling. Bagging reduces variance of the model since the results of each model are averaged together. Boosting takes this a step further by emphasizing the individual models that were more erroneous by weighing them more.

* [a primer on bagging vs boosting](https://analyticsindiamag.com/primer-ensemble-learning-bagging-boosting/)

Decision trees are useful when there are complex relationships between the features and the output variables. They also work well compared to other algorithms when there are missing features, when there is a mix of categorical and numerical features and when there is a big difference in the scale of features.

* [regression using decision trees](https://saedsayad.com/decision_tree_reg.htm)

## linear regression

Linear Regression is used to predict continuous outputs where there is a linear relationship between the features of the dataset and the output variable. It is used for regression problems where you are trying to predict something with infinite possible answers such as the price of a house.

* [linear regression vs decision trees](https://mlcorner.com/linear-regression-vs-decision-trees/)
