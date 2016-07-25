from V2_parser import *

add_core_dict = {'CLA':'KEY', 'AIR':'KEY', 'KAN':'KEY', 'PLA':'KEY', 'LBU':'KEY', 'REW':'KEY'}

class work:
    def __init__(self):
        pass
        
    def process(self, V2_struct):
        d = dict(V2_struct)
        owner_flag = None
        if 'owner' in d:
            owner_flag = d['owner']
        if owner_flag in add_core_dict:
            add_flag = add_core_dict[owner_flag]
            result = []
            core_added = False
            for key, val in V2_struct:
                if key == 'owner':
                    result.append((key, owner_flag))
                elif key == 'controller':
                    result.append((key, owner_flag))
                elif key == 'add_core':
                    if not core_added:
                        result.append((key, owner_flag))
                        result.append((key, add_flag))
                        core_added = True
                    else:
                        pass
                elif key == '1836.1.1':
                    pass
                elif key == '1861.1.1':
                    pass
                elif key == 'colonial':
                    pass
                else:
                    result.append((key, val))
            return result     
        return V2_struct

if __name__=='__main__':
    p = V2_parser("./../../3035/history/provinces") 
    #p = V2_parser("./fuck") 
    w = work()
    p.process(w)
    