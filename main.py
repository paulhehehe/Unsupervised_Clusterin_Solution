# from setuptools import find_packages, setup


# setup(
#     name='src',
#     packages=find_packages(),
#     version='0.1.0',
#     description='Credit Risk Model code structuring',
#     author='Swapnil Kangralkar',
#     license='',
# )

from src.data.make_dataset import load_and_preprocess_data
from src.visualization.visualize import plot_clusters
from src.features.build_features import create_dummy_vars
from src.models.train_model import train_kmeans,elbow_method,Silhouette
from src.models.predict_model import evaluate_model

if __name__ == "__main__":
    # Load and preprocess the data
    data_path = "data/raw/mall_customers.csv"
    df = load_and_preprocess_data(data_path)

    # Train the logistic regression model
    model = train_kmeans(df)

    # Evaluate the model
    plot_clusters(model,df)
    elbow_method(df)
    Silhouette(df)
    
