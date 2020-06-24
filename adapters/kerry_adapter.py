import template

def getCode(s: str):
    code = {
        "010": "101",
        "005": "103",
        "100": "206",
        "103": "206",
        "045": "301",
        "COD": "501",
        "POD": "501" 
    }

    return code[s]

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
            getCode(status[s]["statusCode"]), 
            status[s]["statusDate"],
            status[s]["detail"], 
            (status[s]["province"]).split("-")[1].strip() 
        ]  

        arr3.append(arr2)

    return template.json(arr, arr3)