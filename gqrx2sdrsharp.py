#!/usr/bin/python3

# Copyright by Vladimir Smagin
# http://blindage.org   21h@blindage.org

fileGQRX='gqrx/bookmarks.csv'
fileOUT='sdr#/frequencies.xml'

header='<?xml version="1.0"?><ArrayOfMemoryEntry xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">'
footer='</ArrayOfMemoryEntry>'

def template(data):
    i=0
    for m in data:
        data[i] = m.strip()
        i += 1
    resultString="<MemoryEntry><IsFavourite>false</IsFavourite><Name>{0[1]}</Name><GroupName>{0[4]}</GroupName><Frequency>{0[0]}</Frequency><DetectorType>{0[2]}</DetectorType><Shift>0</Shift><FilterBandwidth>{0[3]}</FilterBandwidth></MemoryEntry>".format(data)
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
    result = result.replace('Narrow FM', 'NFM')
    result = result.replace('WFM (stereo)', 'WFM')
    result = result.replace('WFM (mono)', 'WFM')
    result = result.replace('WFM (oirt)', 'WFM')
    fOUT.write(result)
fOUT.write(footer)
