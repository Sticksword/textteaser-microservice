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

When running linear regression, usually you minimize one of two cost functions: RMSE and MAE.
RMSE is root mean squared error, where you square the difference (error), take the mean, and square root that.
MAE is mean absolute error, where you take the absolute difference (error) and take the mean across the training set.
RMSE increases and is more sensitive to the variance in error frequency distribution, where as MAE doesn't account for that.

* [RMSE vs MAE](https://medium.com/human-in-a-machine-world/mae-and-rmse-which-metric-is-better-e60ac3bde13d)

## recommender systems

Typically you have either content based filtering, user to user collaborative filtering, or item to item collaborative filtering. Usually these types of collaborative filtering are based on nearest neighbors. You could also have poularity based recommendation as well as classification based where you try to classify if a product would be liked based on user features and product features.

* [recommendation engine from scratch in python](https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-recommendation-engine-python/)
* [a medium article describing many of the state of the art](https://medium.com/@madasamy/introduction-to-recommendation-systems-and-how-to-design-recommendation-system-that-resembling-the-9ac167e30e95)
* [simple tutorial on matrix factorization](http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/)

## how to monitor ML models

* [overview (dissected below)](https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/)

### why

* data skews, when the underlying data changes since we last trained
* model staleness, when the coefficients and hyperparameters are not accurate anymore, due to shifts in the environment or adversarial scenarios where bad actors actively seek to bypass your model
* negative feedback loops, for example when the models deployed affect potential future training data
  * [@37:00 Dan Shiebler for Twitter’s Cortex AI team describes this challenge:](https://www.superdatascience.com/podcast/machine-learning-at-twitter)
    * “We need to be very careful how the models we deploy affect data we’re training on […] a model that’s already trying to show users content that it thinks they will like is corrupting the quality of the training data that feeds back into the model in that the distribution is shifting.”

### understanding the spectrum

Testing & monitoring ultimately boil down to risk management. They are both techniques we use to increase our confidence that the system functionality is what we expect it to be, even as we make changes to the system. There is a spectrum of risk management. At one end of the spectrum we have a system with no testing & no monitoring. This is a system with grim future prospects, but also a system where making adjustments is very easy. At the other end we have a heavily tested system with every imaginable monitoring available setup. This is a system where we have a very high level of confidence in its behavior, but where making changes to the system is extremely painful and time-consuming. In this way testing & monitoring are like battle armor. Too little and you are vulnerable. Too much, and you can barely move.

Broadly speaking, there are two buckets where things can go wrong:

* Data Science issues (data monitoring, prediction monitoring)
* Operations issues (system monitoring)

### data sci monitoring

What we can monitor:

* model prediction distribution (regression algorithms) or frequencies (classification algorithms)
  * median, mean, standard deviation, max/min values
* model input distribution (numerical features) or frequencies (categorical features), as well as missing value checks
  * Given a set of expected values for an input feature, we can check that a) the input values fall within an allowed set (for categorical inputs) or range (for numerical inputs) and b) that the frequencies of each respective value within the set align with what we have seen in the past. Depending on our model configuration, we will allow certain input features to be null or not.
* model versions
  * track what was deployed when

### operational monitoring

What we can monitor:

* System Performance (Latency)
* System Performance (IO/Memory/Disk Utilisation)
* System Reliability (Uptime)
* Auditability (though this applies also to our model)

[Three pillars of observability](https://grafana.com/blog/2019/10/21/whats-next-for-observability/):

* Metrics (eg. with Prometheus (monitor and manage metrics) & Grafana (viz))
* Logs (eg. with ELK (elasticsearch, logstash, and kibana))
* Distributed Traces

## deploying ML models

* [overview (dissected below)](https://christophergs.com/machine%20learning/2019/03/17/how-to-deploy-machine-learning-models/)
* [google paper on hidden technical debt in ML systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf)

### start with the ML system architecture

![ml architecture image](docs/ml_system_architectures.jpg "ML System Architectures")

Ask the product/use case questions:

* Do you need to be able to serve predictions in real time (and if so, do you mean like, within a dozen milliseconds or after a second or two), or will delivery of predictions 30 minutes or a day after the input data is received suffice?
* How often do you expect to update your models?
* What will the demand for predictions be (i.e. traffic)?
* What size of data are you dealing with?
* What sort(s) of algorithms do you expect to use (and do you really need them)

![example architecture image](docs/example_architecture.jpg "Example ML Architecture")

### turn experimental code into reproducible pipelines

can use [scikit learn pipelines](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) or other tool/library of choice

### make sure to test, a hallmark of traditional software engineering

* differential tests, how do different models compare on the same data
* benchmark tests, did the new models become more inefficient somehow
* maybe load/stress tests

### [A Rubric for ML Production Readiness and Technical Debt Reduction](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf)

You need:

* TESTS FOR FEATURES AND DATA
* TESTS FOR MODEL DEVELOPMENT
* TESTS FOR ML INFRASTRUCTURE
* MONITORING TESTS FOR ML

### [Need CD for ML](https://martinfowler.com/articles/cd4ml.html)
