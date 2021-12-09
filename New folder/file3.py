


import file1
import file2
import pushbullet

p1 = pushbullet.Pushbullet("write your long and cool key")

def body():
    a = file1.print_region()
    b = file1.print_country()
    c = file1.print_tz_id()
    d = file1.print_day()
    e = file1.print_tempinc()
    f = file1.print_tempinf()
    g = file1.print_windkph()
    h = file1.print_windmph()
    i = file1.direc_deg()
    j = file2.print_word()
    k = file2.print_meaning()
    li = [a, b, c, d, e, f, g, h, i, j, k]
    return li


result = p1.push_sms(p1.devices[0], "enter the phone number", message=body() )
print(result)
