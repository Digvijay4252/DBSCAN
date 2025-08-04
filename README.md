<!-- # DBSCAN

<img width="1739" height="904" alt="image" src="https://github.com/user-attachments/assets/53ad4f21-2e43-4a28-be7f-b20b483465c6" /> -->

## DBSCAN Clustering Web App

This project implements DBSCAN (Density-Based Spatial Clustering of Applications with Noise) using Python, Flask, and scikit-learn, enabling users to visualize clustering results based on input features.

---

## Features

- Age helps differentiate young spenders, working professionals, and seniors.

- Annual Income is crucial for distinguishing high-income vs. low-income clusters.

- Spending Score helps discover outliers (e.g., high income but low spending) and groups like loyal customers.

---

## How It Works

1. **Data Collection**: Loads a CSV dataset of labeled spam and ham messages.
2. **Preprocessing**: Removes punctuation, stopwords, and applies stemming.
3. **Vectorization**: Converts text into numeric features using CountVectorizer.
4. **Model Training**: Trains a Multinomial Naive Bayes classifier.
5. **Web App**: User enters a message → Model predicts if it's spam → Displays result.

---

## Project Structure

```
DBSCAN/
│
├── app.py                # Flask web application to show results
├── train_model.py        # DBSCAN clustering script (trains and saves cluster labels)
├── dbscan_data.csv       # Input dataset for DBSCAN
├── dbscan_output.csv     # Output with assigned cluster labels
├── templates/
│   └── index.html        # Frontend for displaying results
└── static/
    └── style.css         # (optional) Styling for the HTML page

```

---

## Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/DBSCAN.git
cd DBSCAN
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open in browser

Visit: http://localhost:10000

## Screenshots

<img width="1739" height="904" alt="image" src="https://github.com/user-attachments/assets/53ad4f21-2e43-4a28-be7f-b20b483465c6" />

## Future Improvements

Visualize clusters using matplotlib or seaborn

Add support for user-uploaded CSVs

Allow tuning of eps and min_samples via form

Export clustering result as downloadable file
