import response_template

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
            "company": info[1],
            "sender": info[2],
            "receiver": info[3]
        },
        "status": statusDictArr
    }

    return response_template.success(200, "Success", x)