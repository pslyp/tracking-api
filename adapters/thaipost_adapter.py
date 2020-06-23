import template

def convert(datas: dict):
    data = datas["data"]
    status = data["data"]

    arr = [ data["barcode"], "", "", "" ]

    arr2 = []

    staLen = len(status)
    for i in range(staLen):
        index = (staLen-1)-i
        arr2.append([
            "",
            status[index]["timestamp"],
            status[index]["description"],
            status[index]["location"]
        ])

    return template.json(arr, arr2)