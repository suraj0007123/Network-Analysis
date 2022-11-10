#### Importing the Libraries for the network analytics 
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

## Loading the dataset for the Network analytics model building
connecting_route = pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\network analysis\Datasets_Network Analytics\connecting_routes.csv")

connecting_route2=connecting_route.drop(connecting_route.columns[6], axis=1)

connecting_route2.columns

# changing index cols with name() 
connecting_route2.columns=['Flights','ID','Main Airport','Main Airport ID','Destination','Destination ID','Haults','Machinary']

connecting_route2.columns ## To know the column names after giving the names 

connecting_route2.info() ## To know the info about the data

connecting_route2.dtypes ## To know the data dtypes of each column of the dataset

connecting_route2.shape ## To know the shape of the dataset

######### Identifying the duplicates of the dataset #######
duplicate = connecting_route2.duplicated()

duplicate

sum(duplicate)


#######feature of the dataset to create a data dictionary##########
description  = ["Flights type",
                "Flight ID",
                "Departure airport name",
                 "Departure airport ID",
                 "Destination airport name",
                 "Destination airport ID",
                  "Numbers of haults",
                 "Type of flight"]

d_types =["nominal","nominal","nominal","nominal","nominal","nominal","nominal","nominal"]

data_details =pd.DataFrame({"column name":connecting_route2.columns,
                "description":description,
                "data types ":d_types,
                "data format":connecting_route2.dtypes})

####### Data Cleaning
connecting_route2.isnull().sum()

##### for Mean,Meadian,Mode imputation we can use Simple Imputer or df.fillna()
from sklearn.impute import SimpleImputer

# Mode Imputer
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

connecting_route2["Machinary"] = pd.DataFrame(mode_imputer.fit_transform(connecting_route2[["Machinary"]]))

connecting_route2.isnull().sum()  

######## Model Building
g_data = nx.Graph()

g_data = nx.from_pandas_edgelist(connecting_route2, source = 'Main Airport', target = 'Destination')

print(nx.info(g_data))

b = nx.degree_centrality(g_data)  # Degree Centrality

print(b) 

#top 10  Degree Centrality
top_10_b= sorted(b, key=b.get, reverse=True)[:10]

top_10_b

pos = nx.spring_layout(g_data, k = 0.15)
    
nx.draw_networkx(g_data, pos, node_size = 75, node_color = 'pink')

closeness = nx.closeness_centrality(g_data) # closeness centrality

print(closeness)

#top 10 closeness centrality
top_10_cc= sorted(closeness, key=closeness.get, reverse=True)[:10]
top_10_cc


Betweeness = nx.betweenness_centrality(g_data) # Betweeness_Centrality
print(Betweeness)

#top 10 Betweeness Centrality
top_10_Betweeness= sorted(Betweeness, key=Betweeness.get, reverse=True)[:10]
top_10_Betweeness

## Eigen-Vector Centrality
evg = nx.eigenvector_centrality(g_data) # Eigen vector centrality
print(evg)
#top 10 Eigen vector centrality
top_10_evg= sorted(evg, key=evg.get, reverse=True)[:10]
top_10_evg


# cluster coefficient
cluster_coeff = nx.clustering(g_data)
print(cluster_coeff)

# Average clustering
avg_clust = nx.average_clustering(g_data) 
print(avg_clust)
