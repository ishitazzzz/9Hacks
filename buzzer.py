import os
def buzzer():
    with open('redlist.txt','r') as f:
        x = f.read() 
        if os.path.getsize('./buzzer.py') == 0:
            print("empty")
        else:
            print("intruder detected")
            f.close()
            with open('redlist.txt','w'):
                pass
        f.close()

