#!/usr/bin/python3

# Copyright by Vladimir Smagin
# http://blindage.org   21h@blindage.org

fileGQRX='gqrx/bookmarks.csv'
fileOUT='hdsdr/user.csv'

header='Name;LO;Tune;Mode;SrateOut;LoCut;HiCut'
footer=''

def template(data):
    i=0
    for m in data:
        data[i] = m.strip()
        i += 1
    resultString="{0[1]};{0[0]};{0[0]};{0[2]};{0[3]};100;4500\r\n".format(data)
    return resultString

fIN = open(fileGQRX, 'r+')
fOUT = open(fileOUT, 'w')

#пропустить первую таблицу с тегами
for line in fIN:
    if line=="\n": break
fIN.readline() #строка с заголовками полей - пропустить
#таблица частот
fOUT.write(header)
for line in fIN:
    data = line.split(';')
    result = template(data)
    result = result.replace('Narrow FM', 'FM')
    result = result.replace('WFM (stereo)', 'FM')
    result = result.replace('WFM (mono)', 'FM')
    result = result.replace('WFM (oirt)', 'FM')
    fOUT.write(result)
fOUT.write(footer)
