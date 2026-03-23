from Evtx.Evtx import Evtx

with Evtx("logs/Security.evtx") as log:
    for record in log.records():
        xml = record.xml()
        if "4688" in xml:
            print(xml)
            break 
