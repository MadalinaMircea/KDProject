import netCDF4
import pandas as pd

nc_dir = 'D://Downloads//cordex-adjust.bias-adjusted-output.EUR-11.IPSL-INERIS.IPSL-IPSL-CM5A-MR.rcp45.r1i1p1.WRF331F' \
          '.v1-IPSL-CDFT22s-MESAN-1989-2005.day.tasminAdjust//output'
# nc_file = 'D://Downloads//cordex-adjust.bias-adjusted-output.EUR-11.IPSL-INERIS.IPSL-IPSL-CM5A-MR.rcp45.r1i1p1.WRF331F' \
#           '.v1-IPSL-CDFT22s-MESAN-1989-2005.day.tasmaxAdjust//output//output_tasmaxAdjust_EUR-11_IPSL-IPSL-CM5A' \
#           '-MR_rcp45_r1i1p1_IPSL-INERIS-WRF331F_v1-IPSL-CDFT22s-MESAN-1989-2005_day_19660101-19751231.nc '


# print(len(tasmax[0][0]))

# content = ''
# allLats = [i for x in lat for i in x]
# allLons = [i for x in lon for i in x]
# print(allLats)
# print(allLons)
# print(min(allLats))
# print(max(allLats))
# print(min(allLons))
# print(max(allLons))


# print(len(tasmax))
# print(len(tasmax[0]))

# for latI in range(0, len(lat) - 1):
#     for lonI in range(9, len(lon) - 1):
#         content = ''
#         for i in range(0, len(dtime) - 1):
#             content = content + str(dtime[i]) + ',' + str(tasmax[i][latI][lonI]) + '\n'
#
#         output = open(str(lat[latI]) + "_" + str(lon[lonI]) + "_" + "tasmax_WRF331F_rcp45.csv", "w+")
#         output.write(content)
#         output.close()
# #
# for latI in range(0, len(lat) - 1):
#     output = open("output.csv", "w+")
#     output.write(content)
#     output.close()

#
# # a pandas.Series designed for time series of a 2D lat,lon grid
# precip_ts = pd.Series(precip, index=dtime)
#
# precip_ts.to_csv('precip.csv', index=True, header=True)

from datetime import time
import os

def getDoubleDigit(digit):
    if(digit < 10):
        return '0' + str(digit)
    return str(digit)

def getDateStr(date):
    # return time.strftime(date,"yyyy/mm/dd")
    return str(date.year) + '/' + getDoubleDigit(date.month) + '/' + getDoubleDigit(date.day)

def splitFilename(filename):
    return filename.split('_')

tasmax_dir = 'D://Downloads//cordex-adjust.bias-adjusted-output.EUR-11.IPSL-INERIS.IPSL-IPSL-CM5A-MR.rcp45.r1i1p1.WRF331F' \
          '.v1-IPSL-CDFT22s-MESAN-1989-2005.day.tasmaxAdjust//output'


tasmin_dir = 'D://Downloads//cordex-adjust.bias-adjusted-output.EUR-11.IPSL-INERIS.IPSL-IPSL-CM5A-MR.rcp45.r1i1p1.WRF331F' \
          '.v1-IPSL-CDFT22s-MESAN-1989-2005.day.tasminAdjust//output'
#
#
# tasmaxFiles = os.listdir(tasmax_dir)
# tasminFiles = os.listdir(tasmin_dir)
#
# for fileI in range(0, len(tasmaxFiles)):
#     tasmaxFile = open(tasmaxFiles[fileI], "r")
#     tasminFile = open(tasminFiles[fileI], "r")
#
#     tasmaxLines = tasmaxFile.read().splitlines()
#     tasminLines = tasminFile.read().splitlines()
#
#     tasmaxSplitFilename = tasmaxFiles[fileI]
#     filename =
#
#     for lineI in range(1, len(tasmaxLines)):


def getDateStr(date, split):
    splitDate = date.split('/')
    return splitDate[0] + split + splitDate[1] + split + splitDate[2]





for inputFile in os.listdir("date/tasmax/"):
    splitInputFile = inputFile.split('_')

    lat = splitInputFile[0]
    lon = splitInputFile[1]

    tasmaxFilename = "date/tasmax/" + inputFile
    tasminFilename = "date/tasmin/" + lat + '_' + lon + "_tasmin_WRF331F_rcp45.csv"

    tasmaxFile = open(tasmaxFilename, "r")
    tasminFile = open(tasminFilename, "r")

    tasmaxLines = tasmaxFile.read().splitlines()
    tasminLines = tasminFile.read().splitlines()

    csvFilename = "date/climpact/csv/" + lat + '_' + lon + "_WRF331F_rcp45_climpact.csv"
    txtFilename = "date/climpact/txt/" + lat + '_' + lon + "_WRF331F_rcp45_climpact.txt"

    csvContent = 'Anul,Luna,Ziua,Tasmax,Tasmin\n'
    if (os.path.exists(csvFilename)):
        csvContent = ''

    txtContent = "Anul\t\tLuna\t\tZiua\t\tTasmax\t\tTasmin\n"
    if (os.path.exists(txtFilename)):
        txtContent = ''

    csvFile = open(csvFilename, "a+")
    txtFile = open(txtFilename, "a+")

    for lineI in range(1, len(tasmaxLines)):
        # print(getDateStr(dtime[dayI]))
        tasmaxSplitLine = tasmaxLines[lineI].split(',')
        tasminSplitLine = tasminLines[lineI].split(',')

        csvLine = getDateStr(tasmaxSplitLine[0], ',') + "," + tasmaxSplitLine[1] + "," + tasminSplitLine[1] + '\n'
        txtLine = getDateStr(tasmaxSplitLine[0], "\t\t") + "\t\t" + tasmaxSplitLine[1] + "\t\t" + tasminSplitLine[1] + '\n'

        csvContent += csvLine
        txtContent += txtLine

    csvFile.write(csvContent)
    csvFile.close()

    txtFile.write(txtContent)
    txtFile.close()









# for inputFile in os.listdir(nc_dir):
#     print(inputFile)
#     nc_file = nc_dir + "//" + inputFile
#     nc = netCDF4.Dataset(nc_file, mode='r')
#
#     nc.variables.keys()
#
#     lat = nc.variables['lat'][:]
#     lon = nc.variables['lon'][:]
#
#     time_var = nc.variables['time']
#     dtime = netCDF4.num2date(time_var[:], time_var.units)
#     tasmax = nc.variables['tasminAdjust'][:]
#
#     for latI in range(0, len(lat)):
#         for latJ in range(0, len(lat[latI])):
#             # print(str(lat[latI][latJ]) + ' ' + str(lon[latI][latJ]))
#             # print(str(int(lat[latI][latJ] * 1000000)) + ' ' + str(int(lon[latI][latJ] * 1000000)))
#             filename = "date/tasmin/" + str(int(lat[latI][latJ] * 1000000)) + '_' + str(int(lon[latI][latJ] * 1000000)) + "_tasmin_WRF331F_rcp45.csv"
#
#             content = 'Data,Terperatura minima\n'
#             if (os.path.exists(filename)):
#                 content = ''
#
#             file = open(filename, "a+")
#
#             for dayI in range(0, len(dtime)):
#                 # print(getDateStr(dtime[dayI]))
#                 line = getDateStr(dtime[dayI]) + ',' + str(tasmax[dayI][latI][latJ]) + '\n'
#                 content += line
#                 # if(dtime[dayI].month == 12 and dtime[dayI].day == 30):
#                 #     if(dayI + 1 == len(dtime) - 1) or (dayI + 1 < len(dtime) - 1 and (dtime[dayI + 1]).day != 31):
#                 #         line = str(dtime[dayI].year) + '/12/31,-99.9\n'
#                 #         content += line
#             file.write(content)
#             file.close()
