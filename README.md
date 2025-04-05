# Customer Segmentation App
This application implements K-Means clustering to segment customers into distinct groups based on demographic and behavioral features, with an interactive Streamlit interface for real-time predictions.

## Features
- Interactive user input form for dynamic clustering
- Pre-trained model integration for instant predictions
- Visual cluster representation with explanatory imagery
- Production-ready deployment via Streamlit


## Dataset
The application is trained on the **mall customers dataset**, It includes features like:
- Customer_ID
- Gender
- Age
- Annual_Income
- Spending_Score

## Feature Engineering

Feature selection: Focus on key clustering drivers (Income + Spending Score)
Categorical conversion: Binary encoding for gender
Input scaling: Presumes pre-scaled training data (model-compatible)

## Technologies Used

Python: Core application logic
Streamlit: Interactive web interface
Scikit-learn: K-Means clustering algorithm
Pandas/NumPy: Data handling
Pickle: Model serialization

## Model

Algorithm: K-Means Clustering
Input Features: Annual Income + Spending Score (Age used optionally in training)
Output: Discrete cluster assignments (0-N)
Visualization: Pre-generated cluster plot (PNG)

## Installation (for local deployment)
If you want to run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/paulhehehe/Regression_Models_Solution
   cd Regression_Models_Solution

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\\Scripts\\activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit application:
   ```bash
   streamlit run app.py

#### Thank you for using the Customer Segmentation Application! Feel free to share your feedback.
