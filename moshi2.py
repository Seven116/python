import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data  # 特征数据
y = iris.target  # 目标标签

# 创建K均值模型
kmeans = KMeans(n_clusters=3, random_state=0)

# 拟合模型并进行聚类
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# 可视化聚类结果
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
plt.xlabel('特征1')
plt.ylabel('特征2')
plt.title('K均值聚类结果')
plt.show()
