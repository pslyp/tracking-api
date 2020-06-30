def k(ss: str):
    for s in ss: 
        if ord(s) < 65 or ord(s) > 90:
            return False
    return True

def company(code: str):
    length = len(code)
    firstTwoPosition = code[0:2]
    firstThreePosition = code[0:3]
    lastTwoPosition = (code+" ")[-3:-1]

    if length == 13 and lastTwoPosition == "TH":
        return "thaipost"
    elif firstTwoPosition == "TH":
        return "flash"
    elif k(firstThreePosition):
        return "kerry"
    elif firstTwoPosition == "TS" and lastTwoPosition == "TS":
        return "test"
    else:
        return "not found"

def apiTest(no: str):
    x = {
        "status": 200,
        "message": "success",
        "data": {
            "info": {
                "no": no,
                "company": "Nonny",
                "sender": "Nonny",
                "receiver": "Nonny"
            },
            "status": [{
                "code": "301",
                "date": "01/07/2563 08:00",
                "detail": "กำลังจัดส่ง",
                "province": "กรุงเทพมหานคร"
            }]
        }
    }

    return x