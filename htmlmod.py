month_english = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_chinese = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
week_english = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
week_chinese = ["一", "二", "三", "四", "五", "六", "日"]
border_old = ['border="0" cellpadding="0" cellspacing="0" class="year"']
border_new = ['border="1" cellpadding="0" cellspacing="0" class="year"']

myfind_list = month_english + week_english + border_old
myreplace_list = month_chinese + week_chinese +border_new
# print(myfind_list)
# print(myreplace_list)


with open("old.html", "r") as f:
    oldtext = f.read()

newtext = oldtext
for myfind, myreplace in zip(myfind_list, myreplace_list):
    # print(myfind)
    # print(myreplace)
    newtext = newtext.replace(myfind, myreplace)

with open("new.html", "w", encoding= 'utf-8') as f:
    f.write("<html>\n")
    f.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
    f.write("<head>\n")
    f.write(newtext)
