#### Importing the Libraries for the network analytics 
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

## Loading the dataset for the Network analytics model building
flight_hault = pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\network analysis\Datasets_Network Analytics\flight_hault.csv")

# changing index cols with name() 
flight_hault.columns=["ID","Name","City","Country","IATA_FAA","ICAO","Latitude","Longitude","Altitude","Time","DST","Tz database time"]

flight_hault.columns ## To know the columns names of the dataset

flight_hault.info() ## To know the info of the dataset

flight_hault.dtypes ## To know the data-types of each column of the dataset

flight_hault.shape ## To knwo the shape of the dataset

##### Identifying the duplicates ######
duplicate = flight_hault.duplicated()

duplicate

sum(duplicate)

#######feature of the dataset to create a data dictionary##########
description  = ["ID is nothing just index",
                "name of place",
                "name of city",
                 "country name",
                 "Departure airport name",
                 "Destination airport name"
                 ,"latitude","longitude","altitude","one clock time for whole",
                  "dst",
                 "time Zone"]


d_types =["count","nominal","nominal","nominal","nominal","nominal","ratio","ratio","ratio","Interval","nominal","nominal"]

data_details =pd.DataFrame({"column name":flight_hault.columns,
                "description":description,
                "data types ":d_types,
                "data format":flight_hault.dtypes})

flight_hault.drop(['ID'],axis=1,inplace=True)

flight_hault.columns

####### Data Cleaning
flight_hault.isnull().sum()

##### for Mean,Meadian,Mode imputation we can use Simple Imputer or df.fillna()
from sklearn.impute import SimpleImputer

##### Mode Imputer ########
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
flight_hault["IATA_FAA"] = pd.DataFrame(mode_imputer.fit_transform(flight_hault[["IATA_FAA"]]))
flight_hault.isnull().sum()  

####### Mode Imputer ######
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
flight_hault["ICAO"] = pd.DataFrame(mode_imputer.fit_transform(flight_hault[["ICAO"]]))
flight_hault.isnull().sum()  

######## Model Building
g_data = nx.Graph()

g_data = nx.from_pandas_edgelist(flight_hault, source = 'IATA_FAA', target = 'ICAO')

print(nx.info(g_data))

b = nx.degree_centrality(g_data)  # Degree Centrality
print(b) 
#top 10  Degree Centrality
top_10_b= sorted(b, key=b.get, reverse=True)[:10]
top_10_b


pos = nx.spring_layout(g_data, k = 0.15)
nx.draw_networkx(g_data, pos, node_size = 75, node_color = 'orange')


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


