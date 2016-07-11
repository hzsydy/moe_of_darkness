from V2_parser import *

class work:
    def __init__(self):
        pass
        
    def process(self, V2_struct):
        result = []
        d = dict(V2_struct)
        if '1836.1.1' in d:
            d_1836 = dict(d['1836.1.1'])
            owner_flag = d_1836['owner']
        else:
            owner_flag = d['owner']
        core_added = false
        for key, val in V2_struct:
            if key == 'controller':
                result.append((key, owner_flag))
            elif key == 'add_core' && !core_added:
                core_added = true
                result.append((key, owner_flag))
            elif key == '1836.1.1':
                pass
            elif key == '1861.1.1':
                pass
            else:
                result.append((key, val))
        return result

if __name__=='__main__':
    #p = V2_parser("./../../3035/history/provinces") 
    p = V2_parser("./fuck") 
    w = work()
    p.process(w)
    