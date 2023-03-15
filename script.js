




window.onload = function(){
    const d = new Date();
    let currentDay = window.timetable[d.getDay()-2];
    let timetableDiv = document.getElementById("timetableDiv");

    let frWidths = ""
    for (let i = 0; i < currentDay.length; i++){
        let currentTimePeriod = document.createElement("div");
        currentTimePeriod.setAttribute("id", "timeslot");
        frWidths += " " + (currentDay[i][1]-currentDay[i][0])/100 + "fr";
        currentTimePeriod.style.backgroundColor = "#"+currentDay[i][3];
        currentTimePeriod.style.border = "2px solid #" + currentDay[i][4];

        currentTimePeriod.innerHTML = currentDay[i][2];
        timetableDiv.append(currentTimePeriod);
    }


    timetableDiv.style.gridTemplateColumns = frWidths;

    
}

