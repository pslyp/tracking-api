import default_adapter

def convert(datas: dict):
    print(datas["Info"])

    info = datas["Info"]
    status = datas["Status"]

    arr = []
    arr[0] = info["consignmentNo"]
    arr[1] = info["senderName"]
    arr[2] = info["recipientName"]
    arr[3] = info["lastStatusDate"]

    arr2 = []
    arr2[0] = status[""]
    arr2[1] = status[""]
    arr2[2] = status[""]
    arr2[3] = status[""]

    arr3 = []

    return default_adapter.convert(arr, arr3)