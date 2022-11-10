#### Importing the Libraries for the network analytics import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

## Loading the dataset for the Network analytics model building
facebook=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\network analysis\Datasets_Network Analytics\facebook.csv")

facebook.columns ### To know the columns

facebook.shape ### To know the shape of the dataset


########### Identifying the duplicates #########
duplicate=facebook.duplicated()
duplicate
sum(duplicate)

######## Model Building ########## 
facebook_1=np.matrix(facebook)

G=nx.from_numpy_matrix(facebook_1,create_using=nx.DiGraph()) ##### Using the numpy matrix for the undirected groph

print(G.edges(data=True))

nx.draw(G)
