from datetime import datetime
import template

def getCode(s :str):

    if "เข้ารับพัสดุ" in s:
        return "101"
    elif "รับพัสดุเข้า" in s:
        return "103"
    elif "ส่งต่อพัสดุ" in s:
        return "207"
    elif "พัสดุถึงสาขา" in s:
        return "206"
    elif "อยู่ในระหว่างการนำส่ง" in s:
        return "301"
    elif "นำส่งสำเร็จ" in s:
        return "501"
    else:
        return "000"

def getDateTime(ts: int):
    dt = datetime.fromtimestamp(ts)
    dtStr = dt.strftime("%d/%m/%Y %H:%M")
    return dtStr

def getProvince(s: str):
    if getCode(s) == "101":
        sCut = s[s.index("Shop ")+5:s.index("เข้า")]
        return sCut

    elif getCode(s) == "103":  
        sCut = s[s.index("Shop ")+5:len(s)]
        return sCut

    elif getCode(s) == "207":
        # if s.index("Shop") > 0:
        #     print("Shop")

        sCut = s.replace(" ", "-") 
        sCut = sCut.split("-ไปยัง")
        sCut = sCut[0].split("-")      
        return sCut[len(sCut)-1]

    elif getCode(s) == "206":
        sSplitLine = s.split("-")   
        if len(sSplitLine) == 1:
            sSplitBlank = s.split(" ")
            return sSplitBlank[len(sSplitBlank)-1]
        else:
            return sSplitLine[1]

    elif getCode(s) == "301":
        return "-"

    elif getCode(s) == "501":
        return "-" 

    else:
        return ""

def convert(datas: dict):
    data = datas['data']
    status = data['parcel_routes']
    
    arr = [ 
        data['pno'], 
        "Flash Express",
        data['src_name'],
        data['dst_name']
    ]
    
    arr2 = []
    staLen = len(status)
    for i in range(staLen):         
        arr2.append([
            getCode(status[i]['message']),
            getDateTime(status[i]['routed_at']),
            status[i]['message'],
            getProvince(status[i]['message']) 
        ])

    return template.json(arr, arr2)