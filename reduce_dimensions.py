import pickle
from sklearn.decomposition import PCA

pickle_in = open("./Data/features_4096.pkl","rb")
features_4096 = pickle.load(pickle_in)

print(features_4096.shape)

pca = PCA(n_components=20)
features_20 = pca.fit_transform(features_4096)

print(features_20.shape)

pca = PCA(n_components=8)
features_8 = pca.fit_transform(features_4096)

print(features_8.shape)

pickle.dump(features_20, open('./Data/features_20.pkl', 'wb'))
pickle.dump(features_8, open('./Data/features_8.pkl', 'wb'))
