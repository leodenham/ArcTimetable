

f = open("timetable.in", "r")

days = []
dayCount = -1

for currentLine in f:
    currentLine = currentLine.strip()
    if currentLine in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        dayCount+=1
        days.append([])
    else:
        startTime, endTime, name, hexColor, borderColor = currentLine.split(" ")
        days[dayCount].append([int(startTime), int(endTime), name, hexColor, borderColor])


startTime = 800
endTime = 1700

for day in days:
    if len(day) == 0:
        day.append([800, 1700, "Nothing", '8ecae6', 'bde0fe'])
    else:
        # if day[0][0] > 800:
        #     day.insert(0, [800, day[0][0], "Nothing"])
        for i in range(len(day)-1, 1, -1):
            if (day[i][0] > day[i-1][1]):
                day.insert(i, [day[i-1][1], day[i][0], "Nothing", "8ecae6", 'bde0fe'])
        # if (day[-1][1] < 1700):
        #     day.append([day[-1][1], 1700, "Nothing"])

fout = open("timetable.js", "w")
fout.write("window.timetable = ")
fout.write(str(days))
fout.close()
        
