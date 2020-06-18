import template

def convert(datas: dict):
    info = datas["Info"]
    status = datas["Status"]

    arr = [ 
        info["consignmentNo"], 
        info["senderName"], 
        info["recipientName"], 
        info["lastStatusDate"] 
    ]

    arr2 = []
    arr3 = []
    staLen = len(status)
    for s in range(staLen):
        arr2 = [ 
            status[s]["statusCode"], 
            status[s]["statusDate"],
            status[s]["detail"], 
            status[s]["province"] 
        ]

        arr3.append(arr2)

    return template.json(arr, arr3)