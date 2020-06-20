def json(info: [], status: [[]]):    
    statusDict = {}
    statusDictArr = []

    for i in range(len(status)):
        statusDict = {
            "code": status[i][0],
            "date": status[i][1],
            "detail": status[i][2],
            "province": status[i][3]
        }

        statusDictArr.append(statusDict)

    x = { 
        "info": {
            "no": info[0],
            "sender": info[1],
            "receiver": info[2],
            "lastStatusDate": info[3]
        },
        "status": statusDictArr    
    }

    return {
        "status": 200,
        "message": "Success",
        "data": x
    }