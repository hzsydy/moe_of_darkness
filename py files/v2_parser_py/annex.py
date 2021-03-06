from V2_parser import *

#annex_dict = {'ETH':'EGY', 'TUN':'EGY', 'MOR':'EGY', 'LIB':'EGY', 'ALD':'EGY', 'TRI':'EGY', 
#    'POR':'SPA', 'KHI':'PER', 'AFG':'PER', 'BUK':'PER', 'KOK':'PER', 'KAL':'HND', 'PAN':'HND',
#    'DEN':'SWE', 'VEN':'ITA', 'URU':'ARG', 'PRG':'ARG', 'BOL':'PEU', 'ECU':'CLM', 'VNZ':'CLM',
#    'NEP':'HND', 'BHU':'HND', 'LUA':'DAI', 'CAM':'DAI', 'JOH':'SIA', 'CHL':'ARG', 
#    'HDJ':'NEJ', 'YEM':'NEJ', 'ARM':'NEJ', 'ABU':'NEJ', 'OMA':'NEJ', 'MAD':'SPA', 
#    'SOK':'FRA', 'GRE':'TUR', 'TEX':'MEX', 'HAI':'UCA', 'CUB':'UCA', 'ITA':'SPA', 'YUG':'TUR', 'UBD':'FIN'
#}

#annex_dict = {'HND':'CLA', 'JAV':'AIR', 'BUR':'KAN', 'USA':'ANG', 'TIB':'LBU', 'SIA':'REW', 'DAI':'SIA', 'PHI':'PLA', 'ANG':'ANG'}

#annex_dict = {
#'SWI':'CCS',
#'GER':'HAY',
#'PLC':'HIG',
#'AST':'HYO',
#'AUS':'KON',
#'TUR':'LUC',
#'FRA':'MAD',
#'CHI':'NAN',
#'RUS':'ROZ',
#'SPA':'SAK',
#'ROM':'SET',
#'SWE':'SHA',
#'PER':'SUZ',
#'ENG':'TOR',
#'FIN':'ZER',
#'NET':'FAT',
#'NEJ':'FAT',
#'MOR':'MRS',
#'SET':'LUC'
#}

annex_dict = {
'NAN':'ANH',
'ROZ':'BAD',
}


class work:
    def __init__(self):
        pass
        
    def process(self, V2_struct):
        d = dict(V2_struct)
        owner_flag = None
        if 'owner' in d:
            owner_flag = d['owner']
        if owner_flag in annex_dict:
            core_flag = annex_dict[owner_flag]
            result = []
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

if __name__=='__main__':
    p = V2_parser("./../../3035/history/provinces/south america") 
    #p = V2_parser("./fuck") 
    w = work()
    p.process(w)
    