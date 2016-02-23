import sys
from metatlas import metatlas_objects as metob
import qgrid
import metatlas.directory_watcher
import pandas as pd
from metatlas import  gui
from ipywidgets import widgets
from IPython.display import display



mz_header = ['compound', 'adduct', 'polarity', 'mz', 'mz_tolerance', 'mz_tolerance_units', 'uname']
mz_dict = dict()

rt_header = ['compound', 'lcms_run', 'rt_max', 'rt_min', 'rt_peak', 'rt_units', 'uname']
rt_dict = dict()

    
def get_atlas_names (wild_card):
    atlas = metob.retrieve('Atlas',name= wild_card, username='*')
    atlases_list = list()
    for cc in atlas:
        atlases_list.append(cc.name)    
           
    return  atlases_list
  

def get_mz_from_atlas(atlas_name):
    atlas = metob.retrieve('Atlas', name = atlas_name, username='*')

    # - dict to hold values
    for i in mz_header:
        mz_dict[i] = list()
    
    for x in atlas[0].compound_identifications:
        mz_dict['compound'].append(str(x.compound[0].name))
        mz_dict['adduct'].append(str(x.mz_references[0].adduct))
        mz_dict['mz'].append(str(x.mz_references[0].mz))
        mz_dict['polarity'].append(str(x.mz_references[0].detected_polarity))
        mz_dict['mz_tolerance'].append(str(x.mz_references[0].mz_tolerance))
        mz_dict['uname'].append(str(x.mz_references[0].username))
        mz_dict['mz_tolerance_units'].append(str(x.mz_references[0].mz_tolerance_units))
        
        return mz_dict


def get_rt(atlas_name):
    atlas = metob.retrieve('Atlas', name = atlas_name, username='*')
    
    #- clear the dictionary
    for i in rt_header:
        rt_dict[i] = list()
    
    for x in atlas[0].compound_identifications:
        rt_dict['compound'].append(str(x.compound[0].name))
        rt_dict['lcms_run'].append(str(x.rt_references[0].lcms_run))
        rt_dict['rt_max'].append(str(x.rt_references[0].rt_max))
        rt_dict['rt_min'].append(str(x.rt_references[0].rt_min))
        rt_dict['rt_peak'].append(str(x.rt_references[0].rt_peak))
        rt_dict['uname'].append(str(x.rt_references[0].username))
        rt_dict['rt_units'].append(str(x.rt_references[0].rt_units))
        
        return mz_dict
