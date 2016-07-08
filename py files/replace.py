import os
import re

def listFiles(dirPath):
    fileList = []
    for root,dirs,files in os.walk(dirPath):
        for fileObj in files:
            fileList.append(os.path.join(root,fileObj))
    return fileList 
    
def listKeywords():
    keywordList = []
    
    keywordList.append(('GRE', 'ERG'))
    keywordList.append(('FRA', 'ARF'))
    return keywordList

def main():
    fileDir = "./fuck"
    fileList = listFiles(fileDir)
    keywordList = listKeywords()
    print keywordList
    for fileObj in fileList:
        f = open(fileObj,'r+')
        all_the_lines=f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_the_lines:
            l = line
            for key,replacement in keywordList:
                l = l.replace(key, replacement)
            f.write(l)    
        f.close()  

if __name__=='__main__':
    main() 