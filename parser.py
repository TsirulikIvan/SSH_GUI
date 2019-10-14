#Script which helps your to know logging time

stri = 'guest    :1       :1               16:02   ?xdm?   7:52   0.02s /usr/lib/gdm3/gdm-x-session --run-script env GNOME_SHEL'

def logging_time(data):
    res = {}
    tmp = []
    for item in data:
        if item != '':
            tmp.append(item)
    res.update([(tmp[0], tmp[3])])
    return res






print(logging_time(stri))
