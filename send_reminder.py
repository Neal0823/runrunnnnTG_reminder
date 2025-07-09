{\rtf1\ansi\ansicpg950\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
from datetime import datetime\
\
# === \uc0\u29992 \u25142 \u35373 \u23450  ===\
TOKEN = "7519259612:AAFa60nCfhWDf4uj-oFEhGvNafbdrzLOpQA"\
CHAT_ID = "988908445"\
\
# === \uc0\u20170 \u26085 \u26085 \u26399  ===\
today = datetime.now().strftime("%Y-%m-%d")\
weekday = datetime.now().strftime("%A")\
\
# === \uc0\u36305 \u27493 \u35336 \u30059 \u65288 \u21487 \u27599 \u36913 \u26356 \u26032 \u65289  ===\
schedule = \{\
    "Thursday": "\uc0\u55357 \u56517  \u20170 \u22825 \u26159 \u36913 \u22235 \u65306 \u31680 \u22863 \u36305  5\'966K\u65292 \u37197 \u36895  6:30/km\u65292 \u25511 \u21046  Zone 3 \u24515 \u29575  \u55357 \u56488 ",\
    "Friday": "\uc0\u55357 \u56517  \u20170 \u22825 \u26159 \u36913 \u20116 \u65306 \u36629 \u39686 \u24674 \u24489 \u36305  3\'964K\u65292 \u25918 \u39686 \u36523 \u24515  \u55358 \u56792 \u8205 \u9794 \u65039 ",\
    "Saturday": "\uc0\u55357 \u56517  \u20170 \u22825 \u26159 \u36913 \u20845 \u65306 \u38291 \u27463 \u35347 \u32244  5\'966K\u65292 800m x4\u65292 \u37197 \u36895  5:00/km \u9889 ",\
    "Sunday": "\uc0\u55357 \u56517  \u20170 \u22825 \u26159 \u36913 \u26085 \u65306 LSD \u38263 \u36317 \u38626 \u24930 \u36305  9\'9610K\u65292 \u37197 \u36895  7:30/km \u55357 \u56354 ",\
    "Monday": "\uc0\u55357 \u56517  \u20170 \u22825 \u26159 \u36913 \u19968 \u65306 \u20241 \u24687 \u26085 \u65292 \u21487 \u25289 \u20280  + \u26680 \u24515 \u35347 \u32244  \u55358 \u56792 \u8205 \u9792 \u65039 \u55357 \u56490 ",\
    "Tuesday": "\uc0\u55357 \u56517  \u20170 \u22825 \u26159 \u36913 \u20108 \u65306 \u22369 \u36947 \u36305 \u25110 \u24375 \u21270 \u35347 \u32244  4\'965K\u65292 \u21050 \u28608 \u24515 \u32954 \u33287 \u33151 \u37096  \u55357 \u56636 ",\
    "Wednesday": "\uc0\u55357 \u56517  \u20170 \u22825 \u26159 \u36913 \u19977 \u65306 \u36629 \u39686 \u36305  5K\u65292 \u28310 \u20633 \u36914 \u20837 \u19979 \u36913  \u55356 \u57088 "\
\}\
\
message = f"\{schedule.get(weekday, '\uc0\u20170 \u22825 \u27794 \u26377 \u35373 \u23450 \u35347 \u32244 \u20839 \u23481 ')\}\\n\u65288 \u33258 \u21205 \u25552 \u37266 \u65289 \u55356 \u57283 \u8205 \u9794 \u65039 "\
\
# === \uc0\u30332 \u36865 \u35338 \u24687  ===\
url = f"https://api.telegram.org/bot\{TOKEN\}/sendMessage"\
payload = \{"chat_id": CHAT_ID, "text": message\}\
res = requests.post(url, data=payload)\
\
print(f"\uc0\u35338 \u24687 \u30332 \u36865 \u29376 \u24907 \u65306 \{res.status_code\}")}