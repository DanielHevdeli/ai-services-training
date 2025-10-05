### TODO:
1. Basics:
    1. Explain what a probability distribution is.
    2. What are descriptive and inferential statistics.

2. Traditional algorithms.
    1. What are the difference between regression and classification?
    2. Write 1~2 pages summary on logistic and linear regression.

    3. Exercise 1: Linear Regression (Predict exam scores)
        1. Dataset:
           Hours studied (X) vs exam score (y):
           X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
           y = [35, 50, 45, 55, 60, 65, 70, 80, 85]
        2. Use Python to build a linear regressions model to predict a student's exam score based on the hours the student studied. NOTE - you don't have to implement the ML algorithm, use Numpy, matplotlib (to plot graphs) and from sklearn.linear_model import LinearRegression.
            1. Plot the data points (scatter plot). What do you notice about the trend?
            2. Use a linear regression model in Python (e.g., from sklearn.linear_model) to fit the data.
            3. Find the equation of the line (y = m*x + b).
            4. Predict the exam score for a student who studied 10 hours.
            5. Compare the predicted values with the actual values. How close is the model?

    4. Exercise 2: Logistic Regression (Predict student passes/fails)
        1. Dataset:
           Hours studied (X) vs Pass/Fail (y):
           X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
           y = [0, 0, 0, 0, 0, 1, 1, 1, 1]   # 0 = fail, 1 = pass
        2. Use Python to build a logistic regressions model to predict whether a student will pass/fail an exam based on the hours the student studied. NOTE - you don't have to implement the ML algorithm, use Numpy, matplotlib (to plot graphs) and from sklearn.linear_model import LogisticRegression.
            1. Plot the data points: use 0 for fail and 1 for pass. What do you notice about the threshold?
            2. Train a logistic regression model in Python with this dataset.
            3. Plot the predicted probability curve (hours studied on X-axis, probability of passing on Y-axis).
            4. Find the decision boundary (the point where probability ≈ 0.5).
            5. Change the dataset slightly (e.g., say at 5 hours the student passes) and see how the curve changes.

    5. Summarize in 0.5~1 page what hypothesis testing is.

    6. Summarize in 0.5~1 page what decision trees are.

3. Model Metrics.
    1. Explain what are the following model evaluation metrics:
        1. Accuracy
        2. Logarithmic Loss
        3. Precision
        4. Recall
        5. F1-Score


