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
    elif firstTwoPosition == "TT":
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
                "company": "Non Expresss",
                "sender": "Non 1",
                "receiver": "Non 2"
            },
            "status": [{
                "code": "501",
                "date": "01/07/2563 13:00",
                "detail": "นำจ่ายสำเร็จ",
                "province": "กรุงเทพมหานคร"
            }, 
            {
                "code": "301",
                "date": "01/07/2563 08:00",
                "detail": "อยู่ระหว่างการนำจ่าย",
                "province": "กรุงเทพมหานคร"
            }]
        }
    }

    return x