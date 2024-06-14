import math
year=int(input("Please input Year:"))
month=int(input("Please input month:"))
w=["Sun",'Mon','Tue','Wed','Thr','Fri','Sat']
print(" ".join(w))
t=[0,3,2,5,0,3,5,1,4,6,2,4]
if month==1 or month==2:
    year=year-1
    a=math.floor(year/4)
    b=math.floor(year/100)
    c=math.floor(year/400)
    first_week_day=(year+a-b+c+t[month-1]+1)%7
    print("  0 "*(first_week_day),end=" ")
else:
    a=math.floor(year/4)
    b=math.floor(year/100)
    c=math.floor(year/400)
    first_week_day=(year+a-b+c+t[month-1]+1)%7
    print("  0 "*(first_week_day),end=" ")
year_type=0
if year%4==0:
    if year%100==0:
        if year%400:
            year_type="leap_year"
        else:
            year_type="nleap_year"
    else:
        year_type="leap_year"
else:
    year_type=="nleap_year"
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    num_days=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    if first_week_day==0:
        print(num_days[:7],'\n',num_days[7:14],"\n",num_days[14:21],"\n",num_days[21:28],"\n",num_days[28:32])
    elif first_week_day==1:
        print(num_days[:6],'\n',num_days[6:13],"\n",num_days[13:20],"\n",num_days[20:27],"\n",num_days[27:32])
    elif first_week_day==2:
        print(num_days[:5],'\n',num_days[5:12],"\n",num_days[12:19],"\n",num_days[19:26],"\n",num_days[26:32])
    elif first_week_day==3:
        print(num_days[:4],'\n',num_days[4:11],"\n",num_days[11:18],"\n",num_days[18:25],"\n",num_days[25:32])
    elif first_week_day==4:
        print(num_days[:3],'\n',num_days[3:10],"\n",num_days[10:17],"\n",num_days[17:24],"\n",num_days[24:32])
    elif first_week_day==5:
        print(num_days[:2],'\n',num_days[2:9],"\n",num_days[9:16],"\n",num_days[16:23],"\n",num_days[23:32])
    else:
        print(num_days[:1],'\n',num_days[1:8],"\n",num_days[8:15],"\n",num_days[15:22],"\n",num_days[22:32])
elif month==4 or month==6 or month==9 or month==11:
    num_days=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
    if first_week_day==0:
        print(num_days[:7],'/n',num_days[7:14],"/n",num_days[14:21],"/n",num_days[21:28],"/n",num_days[28:31])
    elif first_week_day==1:
        print(num_days[:6],'/n',num_days[6:13],"/n",num_days[13:20],"/n",num_days[20:27],"/n",num_days[27:31])
    elif first_week_day==2:
        print(num_days[:5],'/n',num_days[5:12],"/n",num_days[12:19],"/n",num_days[19:26],"/n",num_days[26:31])
    elif first_week_day==3:
        print(num_days[:4],'/n',num_days[4:11],"/n",num_days[11:18],"/n",num_days[18:25],"/n",num_days[25:31])
    elif first_week_day==4:
        print(num_days[:3],'/n',num_days[3:10],"/n",num_days[10:17],"/n",num_days[17:24],"/n",num_days[24:31])
    elif first_week_day==5:
        print(num_days[:2],'/n',num_days[2:9],"/n",num_days[9:16],"/n",num_days[16:23],"/n",num_days[23:31])
    else:
        print(num_days[:1],'/n',num_days[1:8],"/n",num_days[8:15],"/n",num_days[15:22],"/n",num_days[22:31])
elif month==2:
    if year_type=="leap_year":
        num_day=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"]
        if first_week_day==0:
            print(num_days[:7],'/n',num_days[7:14],"/n",num_days[14:21],"/n",num_days[21:28],"/n",num_days[28:30])
        elif first_week_day==1:
            print(num_days[:6],'/n',num_days[6:13],"/n",num_days[13:20],"/n",num_days[20:27],"/n",num_days[27:30])
        elif first_week_day==2:
            print(num_days[:5],'/n',num_days[5:12],"/n",num_days[12:19],"/n",num_days[19:26],"/n",num_days[26:30])
        elif first_week_day==3:
            print(num_days[:4],'/n',num_days[4:11],"/n",num_days[11:18],"/n",num_days[18:25],"/n",num_days[25:30])
        elif first_week_day==4:
            print(num_days[:3],'/n',num_days[3:10],"/n",num_days[10:17],"/n",num_days[17:24],"/n",num_days[24:30])
        elif first_week_day==5:
            print(num_days[:2],'/n',num_days[2:9],"/n",num_days[9:16],"/n",num_days[16:23],"/n",num_days[23:30])
        else:
            print(num_days[:1],'/n',num_days[1:8],"/n",num_days[8:15],"/n",num_days[15:22],"/n",num_days[22:30])
    

    else:
        num_day=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
        
        if first_week_day==0:
            print(num_days[:7],'/n',num_days[7:14],"/n",num_days[14:21],"/n",num_days[21:28],"/n",num_days[28:29])
        elif first_week_day==1:
            print(num_days[:6],'/n',num_days[6:13],"/n",num_days[13:20],"/n",num_days[20:27],"/n",num_days[27:29])
        elif first_week_day==2:
            print(num_days[:5],'/n',num_days[5:12],"/n",num_days[12:19],"/n",num_days[19:26],"/n",num_days[26:29])
        elif first_week_day==3:
            print(num_days[:4],'/n',num_days[4:11],"/n",num_days[11:18],"/n",num_days[18:25],"/n",num_days[25:29])
        elif first_week_day==4:
            print(num_days[:3],'/n',num_days[3:10],"/n",num_days[10:17],"/n",num_days[17:24],"/n",num_days[24:29])
        elif first_week_day==5:
            print(num_days[:2],'/n',num_days[2:9],"/n",num_days[9:16],"/n",num_days[16:23],"/n",num_days[23:29])
        else:
            print(num_days[:1],'/n',num_days[1:8],"/n",num_days[8:15],"/n",num_days[15:22],"/n",num_days[22:29])
    

    
   
