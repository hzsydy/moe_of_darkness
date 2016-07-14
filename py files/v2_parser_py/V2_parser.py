#Du 2016
import re
import os
from V2 import *

__metaclass__  = type

class V2_parser:
    def __init__(self, fileDir):
        self.fileDir = fileDir
        self.fileList = []
        for root,dirs,files in os.walk(self.fileDir):
            for fileObj in files:
                self.fileList.append(os.path.join(root,fileObj))
    
    def process(self, proccls):
        for fileObj in self.fileList:
            print "fucking " + fileObj
            f = open(fileObj,'r+')
            all_the_lines=f.readlines()
            f.seek(0)
            
            v2 = V2()
            v2.load(all_the_lines)
            v2.struct = proccls.process(v2.struct)
            save_lines = v2.save()
            
            f.truncate()
            for line in save_lines:
                f.write(line)
            f.close()  
            
    def processWithFilename(self, proccls):
        for fileObj in self.fileList:
            print "fucking " + fileObj
            f = open(fileObj,'r+')
            all_the_lines=f.readlines()
            f.seek(0)
            
            v2 = V2()
            v2.load(all_the_lines)
            
            filename = re.findall(r'\\(\w+)\s*[-|\.txt]', fileObj)[0]
            v2.struct = proccls.processWithFilename(v2.struct, filename)
            save_lines = v2.save()
            
            f.truncate()
            for line in save_lines:
                f.write(line)
            f.close() 

if __name__=='__main__':
    print 'this is a lib, not a executable file'
     