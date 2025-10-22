# ☕ Logistic Regression Story: Who Buys Coffee?

# ---
# 🧭 Story Introduction
# Meet Emma, the owner of a cozy coffee shop. She’s noticed that tired-looking customers buy more coffee.
# To plan her stock better, she wants to predict: given how many hours someone slept, will they buy coffee?
# Let’s help Emma build her first **Logistic Regression model**!
# ---

# ✅ Step 1: Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# metrics will be used for evaluation
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ---

# ✅ Step 2: Create the Dataset
# Each data point represents one customer: how many hours they slept and whether they bought coffee.
# 1 = Bought coffee ☕, 0 = Didn’t buy 🚫
X = np.array([3, 4, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5]).reshape(-1, 1)
y = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])

# 🧩 Question: What pattern do you expect between sleep hours and coffee buying?

# ---

# ✅ Step 3: Visualize the Data
plt.scatter(X, y, color='brown')
plt.title("Do Sleepy People Buy More Coffee?")
plt.xlabel("Hours of Sleep")
plt.ylabel("Bought Coffee (1=Yes, 0=No)")
plt.show()

# 💬 Observation:
# Looks like people who sleep less tend to buy more coffee — a classic pattern for logistic regression!

# ---

# ✅ Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 🧠 Explanation:
# We’ll train on 80% of the data and test on 20% to see how well the model generalizes.

# ---

# ✅ Step 5: Train the Model
model = LogisticRegression()
model.fit(X_train, y_train)

# 🧠 Explanation:
# The model learns a curve that best separates buyers from non-buyers based on hours of sleep.

# ---

# ✅ Step 6: Visualize the Model’s Prediction Curve
X_test_range = np.linspace(3, 10, 200).reshape(-1, 1)
y_prob = model.predict_proba(X_test_range)[:, 1]  # Probability of buying coffee

plt.scatter(X, y, color='brown', label='Actual Data')
plt.plot(X_test_range, y_prob, color='orange', label='Predicted Probability')
plt.title("Coffee Buying Probability by Sleep Hours")
plt.xlabel("Hours of Sleep")
plt.ylabel("Probability of Buying Coffee")
plt.legend()
plt.show()

# 💬 Reflection:
# Notice the S-shaped curve — people who sleep less have a higher chance of buying coffee!

# ---

# ✅ Step 7: Evaluate the Model
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc*100:.2f}%")

cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(cm, display_labels=['No Coffee', 'Bought Coffee']).plot()
plt.show()

# 🧠 Explanation:
# The confusion matrix tells us how many predictions were correct for each class.

# ---

# ✅ Step 8: Try It Yourself — Predict New Customers
# Let’s test Emma’s new visitors:
new_customers = np.array([[4], [6], [8.5]])
new_preds = model.predict(new_customers)
new_probs = model.predict_proba(new_customers)[:, 1]

for sleep, pred, prob in zip(new_customers.ravel(), new_preds, new_probs):
    print(f"Customer slept {sleep} hours → {('☕ Buys coffee' if pred==1 else '🚫 No coffee')} (prob={prob:.2f})")

# 💡 Try changing the values in 'new_customers' and see how predictions change!

# ---

# ✅ Step 9: Summary & Reflection
# 🎯 What we learned:
# - Logistic Regression predicts probabilities (not just yes/no)
# - It’s great for problems with two outcomes (binary classification)
# - The decision boundary happens around the point where probability ≈ 0.5

# ☕ Emma can now stock her coffee machine smartly!
# If many customers slept <6 hours, she can expect more caffeine demand!

# 🧩 Final Questions:
# 1. What would happen if Emma added more features (like age or time of visit)?
# 2. Could logistic regression still work if the relationship wasn’t smooth (like this S-shape)?
