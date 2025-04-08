# Customer Segmentation App
This app has been built using Streamlit and deployed with Streamlit community cloud

[Visit the app here](https://unsupervisedclusterinsolution.streamlit.app/)

password - streamlit

This application implements K-Means clustering to segment customers into distinct groups based on demographic and behavioral features, with an interactive Streamlit interface for real-time predictions.

## Features
- Interactive user input form for dynamic clustering.
- Pre-trained model integration for instant predictions.
- Visual cluster representation with explanatory imagery.
- Accessible via Streamlit Community Cloud.

## Dataset
The application is trained on the **Mall Customers dataset**, a widely used dataset for customer segmentation. It includes features like:
- Customer_ID
- Gender
- Age
- Annual Income
- Spending Score

## Technologies Used
- **Streamlit**: For building the web application.
- **Scikit-learn**: K-Means clustering algorithm.
- **Pandas** and **NumPy**: For data preprocessing and manipulation.
- **Pickle**: For model serialization.

## Model
The predictive model is trained using the Mall Customers dataset. It applies preprocessing steps like binary encoding for categorical variables and scaling numerical features. The clustering model used is K-Means, with Annual Income and Spending Score as primary input features.

## Future Enhancements
* Adding support for multiple datasets.
* Incorporating more features for clustering analysis.
* Adding dynamic visualizations to enhance user interaction and insights.

## Installation (for local deployment)
If you want to run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/paulhehehe/Unsupervised_Clusterin_Solution.git
   cd Unsupervised_Clusterin_Solution
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

#### Thank you for using the Customer Segmentation Application! Feel free to share your feedback.

