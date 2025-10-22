# 📘 Simple Linear Regression — Beginner Hands-On Notebook

# 🧭 Objective
# Learn what linear regression is by doing!\
# You'll train a simple model that predicts exam marks from hours studied.
# This notebook is designed for absolute beginners — no math background required.

# ---

# ✅ Step 1. Import the tools we need
import numpy as np # for numbers
import matplotlib.pyplot as plt # for ploting
from sklearn.linear_model import LinearRegression # for models
from sklearn.model_selection import train_test_split # for train-test split

# ---

# ✅ Step 2. Create a tiny dataset
# Imagine you surveyed 20 students: how many hours they studied, and the marks they got.
# X = hours studied (our input)
# y = marks obtained (our target)
X = np.array(range(1, 21)).reshape(-1, 1)
np.random.seed(0) # for reproducibility
y = 1.2 * X.flatten() + np.random.normal(0, 1.5, X.shape[0]) + 2 # roughly linear but noisy

# 💬 Question: What pattern do you expect to see in this data? lets visualize it!

# ---

# ✅ Step 3. Visualize the data
plt.scatter(X, y)
plt.xlabel("Hours studied")
plt.ylabel("Marks obtained")
plt.title("Hours vs Marks — Our Toy Data")
plt.show()

# 💬 Question: Does the relationship look roughly linear (like a straight line)?

# ---

# ✅ Step 4. Split into training and test sets
# We train the model on some data and test it on the rest to see if we generalize well.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 💬 Question: Why do you think we keep some data for testing instead of training on all of it?

# ---

# ✅ Step 5. Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 💬 Question: What does 'fit' mean in this context?
# Hint: The model is trying to draw the best possible line through the training data.

# ---

# ✅ Step 6. Make predictions
# Let's see how well our model predicts marks for the test data.
y_pred = model.predict(X_test)

print("Test data (hours studied):", X_test.ravel())
print("Actual marks:", y_test)
print("Predicted marks:", y_pred)

# ---

# ✅ Step 7. Inspect model parameters
print("Slope (coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# 💬 Question: What does the slope tell us about studying hours and marks?
# Hint: It's how much marks increase for every extra hour studied.

# ---

# ✅ Step 8. Plot the regression line
plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, model.coef_[0]*X + model.intercept_, color="red", label="Fitted line")
plt.xlabel("Hours studied")
plt.ylabel("Marks obtained")
plt.title("Simple Linear Regression Line")
plt.legend()
plt.show()

# 💬 Question: Does the red line fit the data points well?
# Try changing the y values a little and see how the line changes!

# ---

# 🧩 Step 9. Reflect
# 1. What do you think the model learned?
# 2. Would this model work well if the data weren’t linear (e.g., curved)?

# 🏁 Congrats! You've just trained and visualized your first machine learning model.
