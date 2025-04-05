from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import pandas as pd
import pickle


# Function to train the model
def train_kmeans(df):
    kmodel = KMeans(n_clusters=5).fit(df[['Annual_Income','Spending_Score']])

    # Save the trained model
    with open('models/kmodel.pkl', 'wb') as f:
        pickle.dump(kmodel, f)

    return kmodel

def elbow_method(df):
    k = range(3,9)
    K = []
    WCSS = []
    for i in k:
        kmodel = KMeans(n_clusters=i).fit(df[['Annual_Income','Spending_Score']])
        wcss_score = kmodel.inertia_
        WCSS.append(wcss_score)
        K.append(i)

    wss = pd.DataFrame({'cluster': K, 'WSS_Score':WCSS})

    wss.plot(x='cluster', y = 'WSS_Score')
    plt.xlabel('No. of clusters')
    plt.ylabel('WSS Score')
    plt.title('Elbow Plot')
    plt.show()

    plt.savefig('elbow_plot.png')

def Silhouette(df):

    k = range(3,9) # to loop from 3 to 8
    K = []         # to store the values of k
    ss = []        # to store respective silhouetter scores
    for i in k:
        kmodel = KMeans(n_clusters=i,).fit(df[['Annual_Income','Spending_Score']], )
        ypred = kmodel.labels_
        sil_score = silhouette_score(df[['Annual_Income','Spending_Score']], ypred)
        K.append(i)
        ss.append(sil_score)

    wss = pd.DataFrame({'cluster': K, 'Silhouette_Score':ss})

    wss.plot(x='cluster', y='Silhouette_Score')
    plt.xlabel('No. of clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Plot')
    plt.show()

    plt.savefig('Silhouette_Score.png')