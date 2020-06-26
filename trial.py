from KMeansCluster import *

x = [1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 12, 12, 13, 14, 14, 15, 17, 18, 18, 18, 20, 20, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 27, 28, 28, 28, 29, 30, 31]

y = [28, 29, 26, 24, 22, 28, 24, 21, 23, 9, 7, 14, 22, 29, 27, 10, 6, 16, 24, 27, 11, 5, 8, 13, 25, 5, 12, 8, 14, 11, 5, 11, 18, 21, 24, 21, 16, 17, 24, 21, 15, 19, 21, 16, 13, 19, 23, 17, 14, 16, 21, 23, 19, 17, 21]

df = pd.DataFrame(list(zip(x, y)), columns=['x', 'y'])

a = 2
b = 4

km = KMeans()
km.fit(df)
km.pred(a, b)