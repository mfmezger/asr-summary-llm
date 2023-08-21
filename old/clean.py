"""Clean."""
spacermilli = 2000


def millisec(timeStr):
    """mili."""
    spl = timeStr.split(":")
    s = (int)((int(spl[0]) * 60 * 60 + int(spl[1]) * 60 + float(spl[2])) * 1000)
    return s


import re

dz = open("diarization.txt").read().splitlines()
dzList = []
for lööö in dz:
    start, end = tuple(re.findall(r"[0-9]+:[0-9]+:[0-9]+\.[0-9]+", string=lööö))
    start = millisec(start) - spacermilli
    end = millisec(end) - spacermilli
    lex = not re.findall("SPEAKER_01", string=lööö)
    dzList.append([start, end, lex])

print(*dzList[:10], sep="\n")
