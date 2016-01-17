#!/usr/bin/python3

fileGQRX = 'gqrx/bookmarks.csv'
fileOUT = 'sdrtouch/SDRTouchPresets.xml'

header = '<?xml version="1.0" encoding="UTF-8"?><sdr_presets version="1"><category id="-1" />'
footer = '</sdr_presets>'


fIN = open(fileGQRX, 'r+')
fOUT = open(fileOUT, 'w')

# первая таблица с тегами
fIN.readline()  # строка с заголовками полей - пропустить
categories = []
for line in fIN:
    if line == "\n":
        break
    else:
        categories.append(line.split(';')[0].strip())

#таблица частот
fIN.readline() #строка с заголовками полей - пропустить
stations = []
for line in fIN:
    data = line.split(';')
    i = 0
    for m in data:
        data[i] = m.strip()
        i += 1
    stations.append(data)

#записываем в файл
fOUT.write(header)
idCategory = 0
for category in categories:
    fOUT.write('<category id="{}" name="{}">'.format(idCategory, category))
    idCategory += 1
    idStation=0
    for station in stations:
        if station[4] == category:
            #dem: 0 - FM, 1 - NFM, 2 - AM
            dem = 0
            if station[2] == 'Narrow FM': dem='1'
            if station[2] == 'WFM (stereo)': dem='0'
            if station[2] == 'WFM (mono)': dem='0'
            if station[2] == 'WFM (oirt)': dem='0'
            if station[2] == 'AM': dem='2'
            resultString='<preset id="{0}" name="{1[1]}" freq="{1[0]}" centfreq="{1[0]}" offset="0" order="1" filter="{1[3]}" dem="{2}" />'.format(idStation, station, dem)
            idStation += 1
            print(resultString)
            fOUT.write(resultString)
    fOUT.write('</category>')
fOUT.write(footer)
