def readData(plotSetup, os):
    i = 0
    data = []           # initialize 3D array
    for _ in plotSetup['input']:                    # replace unused variable for loop by _ (undescore)
        # acess the JSON structure
        folder = plotSetup['input'][i]['data']['folder']
        fileName = plotSetup['input'][i]['data']['filename']
        if (os == "ubuntu"):
            fullFileName = folder+"/"+fileName
        elif (os == "windows"):
            fullFileName = folder+"\\"+fileName
        
        headerLines = plotSetup['input'][i]['data']['headerLines']
        columns = plotSetup['input'][i]['data']['columns']
        nColumns = len(columns)

        # initialize 3D array
        data.append([]) 
        for j in range(nColumns):
            data[i].append([])

        # read the TXT files
        file = open(fullFileName, "r")
        for _ in range(headerLines):                
            line = file.readline()             # skip the header lines

        line = file.readline().strip()          # read the line
        while line:
            if line == "":                      # verifies the line is empty
                break
            values = line.split()               # split the line in whitespace
            for j in range(nColumns):
                col = columns[j]-1
                data[i][j].append(float(values[col]))
            line = file.readline().strip()      # read the line
        file.close() 
        i = i + 1                               # update the file index

    return data                                 # return the data (list of lists of lists)