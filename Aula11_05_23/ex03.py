
for h in range(24):
    if h == 0:
        h='00'
    for m in range(0,60,15):
        if m==0:
            m='00'
        print(f"{h}:{m}")