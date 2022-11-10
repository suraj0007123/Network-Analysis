#### Importing the Libraries for the network analytics import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

### Loading the dataset for the network analytics model building 
Instagram=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\network analysis\Datasets_Network Analytics\instagram.csv")

Instagram.columns ### To know the columns 

Instagram.shape ### To know the shape of the dataset 

####### Idenfying the duplicates ###########
duplicate=Instagram.duplicated()
duplicate
sum(duplicate)
##### Dropping the duplicates in the dataset ####
Instagram1 = Instagram.drop_duplicates()

G=nx.star_graph(Instagram1)

nx.draw(G, node_color="Orange", node_size=190)
