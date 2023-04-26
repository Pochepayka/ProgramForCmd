import sys
import argparse
import os

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n','--nameFile',default='test1.txt')
    parser.add_argument ('-s','--substring',default=' ')
    return parser

def readFile (nameFile):
    try:
        f = open(nameFile,'r')
    except IOError as e:
        print(u'НЕ УДАЛОСЬ ОТКРЫТЬ ФАЙЛ')
        exit()
    else:
        with f:
            print(u'ЧИТАЕМ ФАЙЛ:')
            mainString=f.readlines()
            f.close()

    return mainString

def deleteSubstring (mainString,substring):
    print("УДАЛЕНИЕ ВСЕХ ВХОЖДЕНИЙ ПОДСТРОКИ:")
    i=0
    for line in mainString:
        line=line.replace(substring,'')
        mainString[i]=line
        i+=1
    return mainString

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    print (namespace)
    contentFile=readFile(namespace.nameFile)
    print (contentFile)
    substr = namespace.substring
    result=deleteSubstring (contentFile,substr)
    print ("РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ:\n",result,sep="")
