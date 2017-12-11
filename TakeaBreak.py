import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program stated at "+time.ctime())

while (break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=j2QX6Vyj1jI&t=842s")
	break_count += 1