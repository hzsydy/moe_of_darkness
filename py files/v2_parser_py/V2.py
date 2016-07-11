#Du 2016

import re

__metaclass__  = type



class V2:
    def __init__(self):
        self.struct = []
        self.patNotSpace = re.compile(r'\S+')
        
    def load(self, lines):
        r'''
            Load Victoria II text lines.
            input:
                lines - lines in list of string
            output:
                None
        '''
        statuskey = 0
        statusval = 1
        
        self.struct = []
        this = self.struct
        key = ''
        val = ''
        status = statuskey
        
        father_list = []
        
                
        for line in lines:
            line = (line.split('#'))[0]
            line = line.replace('=', ' = ')
            line = line.replace('{', ' { ')
            line = line.replace('}', ' } ')
            words = self.patNotSpace.findall(line)
            for word in words:
                if word == '{':
                    newdictlist = []
                    if status == statuskey:
                        print 'wtf error: {} in key detected'
                        raise
                        key = newdictlist
                    elif status == statusval:
                        val = newdictlist
                        this.append((key, val))
                        status = statuskey
                    father_list.append((this, key, val, status))
                    this = newdictlist
                    key = ''
                    val = ''
                    status = statuskey
                elif word == '}':
                    this, key, val, status = father_list.pop()
                elif word == '=':
                    if status == statuskey:
                        status = statusval
                    elif status == statusval:
                        print 'wtf error : extra = detected'
                        raise
                else:
                    #word is useful
                    if status == statuskey:
                        key = word
                    elif status == statusval:
                        val = word
                        this.append((key, val))
                        status = statuskey
    

    def save(self):
        r'''
            Save Victoria II text lines.
            input:
                None 
            output:
                lines in list of string
        '''
        save_lines = self.__deparse(self.struct, 0)
        return save_lines
        
    def __deparse(self, dictlist, tabnum):
        lines = []
        tabspace = ' '*tabnum*4
        for key, val in dictlist:
            try:
                val = val + []
            except TypeError:
                lines.append(tabspace + key + ' = ' + val + '\n')
            else:
                lines.append(tabspace + key + ' = {' + '\n')
                lines = lines + self.__deparse(val, tabnum+1)
                lines.append(tabspace + '}' + '\n')
            
        return lines

if __name__=='__main__':
    print 'this is a lib, not a executable file'