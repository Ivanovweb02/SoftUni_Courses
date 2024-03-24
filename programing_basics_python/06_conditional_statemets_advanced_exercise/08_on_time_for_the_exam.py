exam_hour = int(input())    # 0-23
exam_minutes = int(input())    # 0-59
arrive_hour = int(input())    # 0-23
arrive_minutes = int(input())    # 0-59

exam_time_as_minutes = exam_hour * 60 + exam_minutes
arrive_time_as_minutes = arrive_hour * 60 + arrive_minutes

diff = arrive_time_as_minutes - exam_time_as_minutes

if diff > 0:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hh = diff // 60
        mm = diff % 60
        print(f"{hh}:{mm:02d} hours after the start")
elif diff >= -30:
    print("On time")
    if not diff == 0:
        print(f"{abs(diff)} minutes before the start")
else:
    print("Early")
    if diff > -60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hh = abs(diff) // 60
        mm = abs(diff) % 60
        print(f"{hh}:{mm:02d} hours before the start")
