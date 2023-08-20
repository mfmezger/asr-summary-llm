
spacermilli = 2000
def millisec(timeStr):
    spl = timeStr.split(":")
    s = (int)((int(spl[0]) * 60 * 60 + int(spl[1]) * 60 + float(spl[2]) )* 1000)
    return s

import re
dz = open('diarization.txt').read().splitlines()
dzList = []
for l in dz:
    start, end =  tuple(re.findall('[0-9]+:[0-9]+:[0-9]+\.[0-9]+', string=l))
    start = millisec(start) - spacermilli
    end = millisec(end)  - spacermilli
    lex = not re.findall('SPEAKER_01', string=l)
    dzList.append([start, end, lex])

print(*dzList[:10], sep='\n')
