import os

folder = "../KDProject/date/"
indicesFolder = folder + "indices/"

#resultsFolder = folder + "new_indices/"

contentDict = {}
separator = '_'

x = 1000

indicesList = ["csdi_ANN", "dtr_ANN", "txx_ANN", "wsdi_ANN"]
#

for indexFolder in os.listdir(indicesFolder):
    x-=1
    if x > 0:
        continue

    indicesFolderPath = indicesFolder + indexFolder

    for indicesFile in os.listdir(indicesFolderPath):
        indicesFilePath = indicesFolderPath + '/' + indicesFile

        fileNameSplit = indicesFile[:-4].split(separator)
        annual = fileNameSplit[-1]
        isAnnual = annual == "ANN"

        indexName = separator.join(fileNameSplit[5:])

        if indexName[-1] == ")":
            paranthI = indexName.find("(")
            indexName = indexName[:paranthI]

        # print(indexName)
        # print(indexName in indicesList)

        if indexName in indicesList:
            newFolderPath = "result/" + indexName


            if not os.path.exists(newFolderPath):
                os.mkdir(newFolderPath)

            fileHandle = open(indicesFilePath, "r")
            fileContent = fileHandle.read()
            fileLines = fileContent.splitlines()

            lat = fileLines[2].split(',')[1]
            lon = fileLines[3].split(',')[1]

            fileLines = fileLines[6:]
            colHeads = fileLines[0].split(',')
            colN = len(colHeads)

            for i in range(1, colN):
                newFilePath = newFolderPath + "/" + colHeads[i] + ".csv"
                firstLine = ''
                addFirstLine = False
                if not os.path.exists(newFilePath):
                    addFirstLine = True
                f = open(newFilePath, "a+")

                firstLine = 'Latitudine,Longitudine'
                secondLine = lat + "," + lon

                for line in fileLines[1:]:
                    splitLine = line.split(',')
                    if addFirstLine:
                        firstLine = firstLine + "," + splitLine[0]

                    secondLine = secondLine + "," + splitLine[i]

                if addFirstLine:
                    f.write(firstLine + '\n')

                f.write(secondLine + '\n')

                f.close()



        # newFileName = indexName + ".csv"
        #
        # print(newFileName)

        # if indexName not in contentDict:
        #     contentDict[indexName] = {}
        #


        # x+=1
        # if(x == 2):
        #     print(contentDict)
        #     exit(1)

# for folder in contentDict:
#     os.mkdir(folder)
#     for index in contentDict[folder]:
#         newFile = resultsFolder + index + ".csv"
#         csvContent = 'Anul,Luna,Ziua,Tasmax,Tasmin\n'
#             # if (os.path.exists(csvFilename)):
#             csvContent = ''
#         file = open(newFile, "a+")
#         newContent = ''
#         for line in contentDict[folder][index]:

