from V2_parser import *

country_dir = "./../../3035/history/countries"
pop_dir = "./../../3035/history/pops/1836.1.1"
province_dir = "./../../3035/history/provinces"

d_prim_culture = {}
d_owner = {}

class work_country:
    def __init__(self):
        pass
        
    def processWithFilename(self, V2_struct, name):
        d = dict(V2_struct)
        if 'primary_culture' in d:
            d_prim_culture[name] = d['primary_culture']
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
        owner_flag = None
        if '1836.1.1' in d:
            d_1836 = dict(d['1836.1.1'])
            if 'owner' in d_1836:
                owner_flag = d_1836['owner']
        else:
            if 'owner' in d:
                owner_flag = d['owner']
        return V2_struct

if __name__=='__main__':
    province = V2_parser(province_dir) 
    country = V2_parser(country_dir) 
    #pop = V2_parser(pop_dir) 
    wc = work_country()
    wpr = work_province()
    country.processWithFilename(wc)
    province.processWithFilename(wpr)
    print d_owner
    