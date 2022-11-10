#### Importing the Libraries for the network analytics import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

### loading the dataset for the network analytics model building
Linkedin=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\network analysis\Datasets_Network Analytics\linkedin.csv")

Linkedin.columns ### To know the columns of the dataset 

Linkedin.shape ## To know the shape of the dataset 


######## Idenfying the duplicates ########
duplicate=Linkedin.duplicated()
duplicate
sum(duplicate)

Linkedin.isnull().sum()

G=nx.star_graph(Linkedin)

nx.draw(G, node_color="DarkRed", node_size=300)
