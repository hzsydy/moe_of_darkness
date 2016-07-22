from V2_parser import *

country_dir = "./../../3035/history/countries"
#country_dir = "./fuck"
pop_dir = "./../../3035/history/pops/1836.1.1"
province_dir = "./../../3035/history/provinces"

d_prim_culture = {}
d_religion = {}
d_owner = {}

class work_country:
    def __init__(self):
        pass
        
    def processWithFilename(self, V2_struct, name):
        d = dict(V2_struct)
        if name != 'REB' and name.find('bp_settings') == -1:
            #if 'primary_culture' in d:
            d_prim_culture[name] = d['primary_culture']
            #if 'religion' in d:
            d_religion[name] = d['religion']    
        return V2_struct
        
class work_province:
    def __init__(self):
        pass
        
    def processWithFilename(self, V2_struct, name):
        d = dict(V2_struct)
        if 'owner' in d:
            d_owner[name] = d['owner']
        return V2_struct

class work:
    def __init__(self):
        pass
        
    def process(self, V2_struct):
        d = dict(V2_struct)
        res = []
        for provname, val in d:
            if provname in d_owner:
                d_prof = {}
                for profname, val_prof in val:
                    if key_prof in d_prof:
                        d_prof[key_prof] = d_prof[key_prof] + dict(val_prof)['size']
                    else:
                        d_prof[key_prof] = dict(val_prof)['size']
                prof_list = []
                for profname, pop_size in d_prof:
                    pop_list = []
                    pop_list.append(('culture', d_prim_culture[provname]))
                    pop_list.append(('religion', d_religion[provname]))
                    pop_list.append(('size', d_religion[provname]))
                    prof_list.append((profname, pop_list))
                res.append((provname, prof_list))
            else:
                res.append((provname, val))
        return res

if __name__=='__main__':
    province = V2_parser(province_dir) 
    country = V2_parser(country_dir) 
    pop = V2_parser(pop_dir) 
    wc = work_country()
    wpr = work_province()
    wpop = work()
    country.processWithFilename(wc)
    province.processWithFilename(wpr)
    pop.process(wpop)
    