import sys
import pandas as pd
import qgrid

from metatlas import metatlas_objects as metob


df = pd.read_csv('/home/jimmy/data/atlas_finfo_to_be_loaded/20151208_Atlas_POS_HILIC_LS_Validated_RTcorr.csv',sep = ',')

df.columns = [x.lower() for x in df.columns]
#qgrid.show_grid(df, precision=5)

fetch_atlases = metob.retrieve('Atlas',name='%_LS_%', username='*')
for c in fetch_atlases:
    print c.name



for x in df.index:
    if not metob.retrieve('Compounds',name=df.name[x]):
        print df.name[x], "is not in database"