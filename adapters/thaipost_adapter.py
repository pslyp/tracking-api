import template

def convert(datas: dict):
    data = datas["data"]
    status = data["data"]

    arr = [ data["barcode"], "", "", "" ]

    arr2 = []

    staLen = len(status)
    for i in range(staLen):
        arr2.append([
            "",
            status[i]["timestamp"],
            status[i]["description"],
            status[i]["location"]
        ])

    return template.json(arr, arr2)