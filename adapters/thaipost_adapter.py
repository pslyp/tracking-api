import json_template

def getCode(s: str):
    code = {
        "เตรียมการฝากส่ง": "101",
        "รับฝากผ่านตัวแทน": "102",
        "รับฝาก": "103",
        "อยู่ระหว่างการขนส่ง": "201",
        "ดำเนินพิธีการศุลกากร": "202",
        "ส่งคืนต้นทาง": "203",
        "ถึงที่ทำการแลกเปลี่ยนระหว่างประเทศขาออก": "204",
        "ถึงที่ทำการแลกเปลี่ยนระหว่างประเทศขาเข้า": "205",
        "ถึงที่ทำการไปรษณีย์": "206",
        "เตรียมการขนส่ง": "207",
        "ส่งออกจากที่ทำการแลกเปลี่ยนระหว่างประเทศขาออก": "208",
        "อยู่ระหว่างการนำจ่าย": "301",
        "นำจ่าย ณ จุดรับสิ่งของ": "302",
        "นำจ่ายไม่สำเร็จ": "401",
        "นำจ่ายสำเร็จ": "501"
    }

    return code[s]

def convert(datas: dict):
    data = datas['data']
    status = data['data']

    arr = [ 
        data['barcode'],
        "Thailand Post", 
        "",
        "" 
    ]

    arr2 = []

    staLen = len(status)
    for i in range(staLen):
        index = (staLen-1)-i
        arr2.append([
            getCode(status[index]['description']),
            status[index]['timestamp'],
            status[index]['description'],
            status[index]['location']
        ])

    return json_template.json(arr, arr2)