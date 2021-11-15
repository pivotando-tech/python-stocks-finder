import json

filePath = '.././userData.json'


def readFile():
    with open(filePath) as json_file:
        data = json.load(json_file)
        return data


def updateFile(key, data):
    with open(filePath, 'r+') as file:
        fileData = json.load(file)
        fileData[key].append(data)
        file.seek(0)
        json.dump(fileData, file, indent=4)


infos = '{"name": "cash3"}'


# updateFile('wallet', infos)

test = readFile()


print(type(test['wallet'][5]))
