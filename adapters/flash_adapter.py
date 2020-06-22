from datetime import datetime
import template

def dateTime(ts: int):
    dt = datetime.fromtimestamp(ts)
    dtStr = dt.strftime("%d/%m/%Y %H:%M")
    return dtStr

def convert(datas: dict):
    data = datas['data']
    status = data['parcel_routes']
    
    arr = [ data['pno'], data['src_name'], data['dst_name'], "" ]
    
    arr2 = []
    staLen = len(status)
    for i in range(staLen):
        arr2.append([
            "",
            dateTime(status[i]['routed_at']),
            status[i]['message'],
            ""
        ])

    return template.json(arr, arr2)