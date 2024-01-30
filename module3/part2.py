time = int(input("Enter the current time(in hours) -->          "))
wait_time = int(input("Enter the hours to wait for the alarm -->     "))

print("Time on 24-hour clock when time goes off --> ", (time + wait_time) % 24)