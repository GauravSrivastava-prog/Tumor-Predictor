# Tumor-Predictor

This project aims to predict whether a breast cancer diagnosis is malignant or benign using the Breast Cancer Wisconsin (Diagnostic) dataset from the UCI Machine Learning Repository.

## Dataset

The dataset contains features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. These features describe characteristics of the cell nuclei present in the image.

**Features:**

- radius (mean of distances from center to points on the perimeter)
- texture (standard deviation of gray-scale values)
- perimeter
- area
- smoothness (local variation in radius lengths)
- compactness (perimeter^2 / area - 1.0)
- concavity (severity of concave portions of the contour)
- concave points (number of concave portions of the contour)
- symmetry
- fractal dimension ("coastline approximation" - 1)

**Target:**

- Diagnosis (M = malignant, B = benign)

## Methodology

1. **Data Loading and Preprocessing:** The dataset is loaded using the `ucimlrepo` library. The target variable ('Diagnosis') is encoded using Label Encoding.

2. **Model Selection:** Various classification models are evaluated using stratified k-fold cross-validation. The models include:
    - Logistic Regression
    - Linear Discriminant Analysis ( We have chosen this model as default because of it's best performance of all. )
    - K-Nearest Neighbors
    - Decision Tree
    - Gaussian Naive Bayes
    - Support Vector Machine

3. **Model Training and Evaluation:** The best performing model is selected and trained on the training data. The model's performance is evaluated on a separate validation set using metrics such as accuracy, precision, recall, and F1-score.

4. **Prediction:** The trained model can be used to predict the diagnosis for new, unseen data.


## Results

The project demonstrates the application of machine learning techniques for breast cancer diagnosis prediction. The best performing model achieves an accuracy of [insert accuracy here] on the validation set.

## Usage

1. Install the required libraries: `pandas`, `ucimlrepo`, `scikit-learn`, `imblearn`, `matplotlib`.
2. Execute the code in the Jupyter Notebook provided.
3. To make predictions on new data, use the `predict` method of the trained model.

## Features

- **Accurate Predictions:** Uses LDA to classify tumors as malignant or benign.
- **User-Friendly Interface:** Easy-to-navigate design for inputting tumor feature values.
- **Real-Time Feedback:** Instant predictions based on user input.
- **Responsive Design:** Compatible with various devices for accessibility.

## Technologies Used

- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Machine Learning:** scikit-learn
- **Data Storage:** No external database; uses in-memory storage.

## Installation

To set up the TumorPredictor application locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/TumorPredictor.git

# Navigate to the project directory
cd TumorPredictor

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`

# Install the required dependencies
pip install -r requirements.txt

## Conclusion

This project provides a basic framework for breast cancer prediction using the Wisconsin Diagnostic dataset. Further improvements can be explored by incorporating feature engineering, hyperparameter tuning, and ensemble methods.
