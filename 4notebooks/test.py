import sys
from metatlas import metatlas_objects as metob
import qgrid
import metatlas.directory_watcher
import pandas as pd
atlas = metob.retrieve('Atlas', name = '%_LS_%', usename='*')
atlas = metob.retrieve('Atlas', name = '%_LS_%', username='*')
atlas
atlas[0]
atlas[0]
len(atlas)
len(atlas[0])
type(atals[0])
type(atlas[0])
cc = atlas[1]
cc.compound_identifications
len(cc.compound_identifications)
cc = atlas[0]
len(cc.compound_identifications)
cc.compound_identifications.cort
cc.compound_identifications.sort
cc.compound_identifications.sort()
cc.compound_identifications
cc.compound_identifications[0]
cc.compound_identifications[0]['compound']
cc.compound_identifications[0][0]
cc.compound_identifications[0]
a=cc.compound_identifications[0]
a.compound
a.mz_references
a.compound['name']
len(a.compound)
len(cc.compound_identifications)
a=cc.compound_identifications[1]
len(a.compound)
a=cc.compound_identifications[2]
len(a.compound)
len(a.compound)
a=cc.compound_identifications[3]
len(a.compound)
a.compound[0]
a.compound[0]['name']
a.compound[0].name
a.compound[0].name
cc.compound_identifications[0].compound
a.compound[0]
a.compound[0].name
str(a.compound[0].name)
a
a.mz_references
a.mz_references[0]
a.mz_references[0].addduct
a.mz_references[0]adduct
a.mz_references[0].adduct
for cc in atlas:
    x = cc.compound_identifications
for cc in atlas:
    x = cc.compound_identifications
    for xx in x:
        print x
for cc in atlas:
    x = cc.compound_identifications
    for xx in x:
        print x.compound.name
for cc in atlas:
    x = cc.compound_identifications
    for xx in x:
        print xx.compound.name
for cc in atlas:
    x = cc.compound_identifications
    for xx in x:
        print xx.compound
for cc in atlas:
    x = cc.compound_identifications
    for xx in x:
        print xx.compound[0].name
for cc in atlas:
    x = cc.compound_identifications
    for xx in x:
        print xx.mz_references
a=cc.compound_identifications[3]
a.compound
a.compound[0]
a.compound[0].name
a.mz_references
a.mz_references[0]
a
my_dict = dict()
my_dict = dict(list)
my_dict = dict(list())
my_dict
my_dict['a']
my_dict['a'] = 1
my_dict
my_dict = dict()
my_dict['compound'] = list()
my_dict['adduct'] = list()
my_dict['polarity'] = list()
my_dict['mz'] = list()
my_dict['tol'] = list()
my_dict['uer'] = list()
my_dict['tol_units'] = list()
atlas = metob.retrieve('Atlas', name = '%_LS_%', username='*')
cc = atlas[1]
for x in cc.compound_identifications:
    my_dict['compound'] = x.compound[0].name
my_dict
len(cc)
len(cc.compound_identifications)
len(cc.compound_identifications)
cc = atlas[0]
for x in cc.compound_identifications:
    my_dict['compound'] = x.compound[0].name
my_dict
for x in cc.compound_identifications:
    my_dict['compound'].append(x.compound[0].name)
my_dict['compound'] = list()
for x in cc.compound_identifications:
    my_dict['compound'] = str(x.compound[0].name)
my_dict
cc = atlas[0]
len(cc)
len(cc.compound_identifications)
for x in cc.compound_identifications:
    print 'hi'
for x in cc.compound_identifications:
    my_dict['compound'].append( str(x.compound[0].name))
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
my_dict['compound'] = list()
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
my_dict
my_dict['compound'] = list()
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
    my_dict['mz'].append(str(x.mz_references[0].adduct))
    my_dict['polarity'].append(str(x.mz_references[0].polarity))
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
    my_dict['mz'].append(str(x.mz_references[0].adduct))
    my_dict['detected_polarity'].append(str(x.mz_references[0].polarity))
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
    my_dict['mz'].append(str(x.mz_references[0].adduct))
    my_dict['polarity'].append(str(x.mz_references[0].detected_polarity))
my_dict
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
    my_dict['mz'].append(str(x.mz_references[0].adduct))
    my_dict['polarity'].append(str(x.mz_references[0].detected_polarity))
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
    my_dict['mz'].append(str(x.mz_references[0].mz))
    my_dict['polarity'].append(str(x.mz_references[0].detected_polarity))
my_dict
header = ['compound', 'adduct', 'polarity', 'mz', 'mz_tol', 'mz_tol_units', 'uname']
my_dict = dict()
for i in header:
    my_dict[i] = list()
my_dict
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
    my_dict['mz'].append(str(x.mz_references[0].mz))
    my_dict['polarity'].append(str(x.mz_references[0].detected_polarity))
    my_dict['mz_tol'].append(str(x.mz_references[0].mz_tolerance))
my_dict
for i in header:
    my_dict[i] = list()
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
    my_dict['mz'].append(str(x.mz_references[0].mz))
    my_dict['polarity'].append(str(x.mz_references[0].detected_polarity))
    my_dict['mz_tol'].append(str(x.mz_references[0].mz_tolerance))
    my_dict['uname'].append(str(x.mz_references[0].username))
    my_dict['mz_tol_units'].append(x.mz_references[0].mz_tolerance_units))
for x in cc.compound_identifications:
    my_dict['compound'].append(str(x.compound[0].name))
    my_dict['mz'].append(str(x.mz_references[0].mz))
    my_dict['polarity'].append(str(x.mz_references[0].detected_polarity))
    my_dict['mz_tol'].append(str(x.mz_references[0].mz_tolerance))
    my_dict['uname'].append(str(x.mz_references[0].username))
    my_dict['mz_tol_units'].append(str(x.mz_references[0].mz_tolerance_units))
my_dict
%history -f test.py
