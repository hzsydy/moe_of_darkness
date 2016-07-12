from V2_parser import *

unity_flag = ['HND', 'GER', 'AUS', 'PLC', 'ITA', 'NET', 'FIN', 'UBD', 'YUG', 'ROM', 'CAN', 'TUR']

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
        if owner_flag != None:
            result = []
            corenum = 0
            core_flag = None
            for key, val in V2_struct:
                if key == 'add_core':
                    corenum = corenum + 1
                    core_flag = val
                    if val in unity_flag:
                        corenum = 1
                        break
            if corenum == 1:
                if (core_flag != owner_flag):
                    for key, val in V2_struct:
                        if key == 'owner':
                            result.append((key, core_flag))
                        elif key == 'controller':
                            result.append((key, core_flag))
                        elif key == 'add_core':
                            result.append((key, core_flag))
                        elif key == '1836.1.1':
                            pass
                        elif key == '1861.1.1':
                            pass
                        else:
                            result.append((key, val))
                else:
                    core_added = False
                    for key, val in V2_struct:
                        if key == 'owner':
                            result.append((key, core_flag))
                        elif key == 'controller':
                            result.append((key, core_flag))
                        elif key == 'add_core':
                            if not core_added:
                                result.append((key, core_flag))
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
        return V2_struct

if __name__=='__main__':
    p = V2_parser("./../../3035/history/provinces") 
    #p = V2_parser("./fuck") 
    w = work()
    p.process(w)
    