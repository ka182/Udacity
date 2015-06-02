import time
import webbrowser

total_breaks = 3
break_count = 0
num_hour = 10

while (break_count < total_breaks):
    time.sleep(num_hour)
    webbrowser.open("http://www.dublinvipers.com")
    print(break_count)
    break_count += 1