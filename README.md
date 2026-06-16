# Phishing-Email-Detection-
# Phishing Email Detection System

## Project Overview

The AI-Based Phishing Email Detection System is a Machine Learning project developed using Python and Scikit-Learn to identify potentially malicious or phishing emails based on their textual content.

The system analyzes email messages, extracts features using TF-IDF vectorization, and classifies emails as either:

* Safe Email (Ham)
* Phishing Email (Spam)

The model is trained on the SMS Spam Collection Dataset and achieves high classification accuracy through supervised machine learning techniques.

---

## Objectives

* Detect phishing and suspicious emails automatically.
* Apply Machine Learning techniques for email classification.
* Extract meaningful features from email content using Natural Language Processing (NLP).
* Evaluate model performance using Accuracy Score and Confusion Matrix.
* Demonstrate practical cybersecurity applications of Artificial Intelligence.

---

## Features

* Email classification using Machine Learning
* TF-IDF text feature extraction
* Naive Bayes classification algorithm
* Accuracy evaluation
* Confusion Matrix visualization
* Interactive email testing through terminal input

---

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn
* Git
* GitHub
* VS Code
---

## Dataset

Dataset Used:

SMS Spam Collection Dataset

Dataset Size:

* 5,572 messages
* Labeled as:

  * Ham (Safe)
  * Spam (Phishing)

The dataset contains real-world SMS messages that are used to train and evaluate the machine learning model.

---

## Project Workflow

1. Load Dataset
2. Preprocess Email Text
3. Convert Text into Numerical Features using TF-IDF
4. Split Dataset into Training and Testing Sets
5. Train Naive Bayes Classifier
6. Evaluate Accuracy
7. Generate Confusion Matrix
8. Classify User-Provided Email Content

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Phishing-Email-Detection.git

cd Phishing-Email-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python phishing_detector.py
```

---

## Results

### Model Accuracy

```text
Accuracy: 96.68%
```

### Confusion Matrix

```text
[[966   0]
 [ 37 112]]
```

The model successfully identifies phishing emails with high accuracy while maintaining a low false-positive rate.

---



## Future Enhancements

* Deep Learning-based Email Classification
* URL Analysis for Phishing Detection
* Real-Time Email Scanning
* Web-Based User Interface
* Cloud Deployment using AWS

---

## Learning Outcomes

Through this project, the following skills were developed:

* Machine Learning Fundamentals
* Natural Language Processing
* Cybersecurity Threat Detection
* Data Preprocessing
* Model Evaluation
* Git and GitHub Version Control


 Cloud Computing | Machine Learning Enthusiast
