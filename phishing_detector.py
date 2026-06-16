import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("PHISHING EMAIL DETECTION MODEL")
print("=" * 50)

# Load Dataset
data = pd.read_csv(
    "emails.csv",
    sep="\t",
    names=["label", "message"]
)

# Convert labels
data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})

# Features
X = data["message"]

# Labels
y = data["label"]

# Convert text into numerical vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = MultinomialNB()

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(cm)

# Graphical Confusion Matrix

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['Safe', 'Phishing'],
    yticklabels=['Safe', 'Phishing']
)

plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')

plt.show()

# Interactive Email Checker
while True:

    email = input("\nEnter Email Content: ")

    email_vector = vectorizer.transform([email])

    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        print("⚠️ PHISHING EMAIL DETECTED")
    else:
        print("✅ SAFE EMAIL")

    choice = input("\nCheck another email? (y/n): ")

    if choice.lower() != "y":
        break