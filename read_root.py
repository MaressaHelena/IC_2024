import sys
# sys.path.insert(0,'/eos/home-a/antoniov/SWAN_projects/env/uproot-py39/lib/python3.9/site-packages')
# print ( sys.path )
import uproot
import awkward as ak
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams.update(
    {'font.size': 18,
     'font.family': 'sans-serif',
     'legend.fontsize': 14,
     'axes.labelsize': 22,
     'axes.labelpad': 8.0,
     'xtick.labelsize': 14,
     'ytick.labelsize': 14
    }
    )
print ( mpl.rcParams )

def read_root( fileName, tree_name="T" ):
    
    root = uproot.open( fileName )
    tree = root[ tree_name ]
    print ( tree.keys() )
    
    events = tree.arrays( tree.keys() , library="ak", how="zip" )
    events[ "event_number" ] = ( np.arange( len(events) ) + 1 )
    
    jets = events["jet"]
    jets[ "event_number" ] = events[ "event_number" ]
    
    df = pd.DataFrame( np.array( ak.flatten( jets ) ), columns=("pt","eta","rap","phi","px","py","pz","energy","event_number") ).set_index( "event_number" )
    
    return df