//setup the initial race


//setup the amount racing
//setup a countdown
function countdown(){
    let initialCountDown=3
    while (initialCountDown >= 1 ) {
        console.log(initialCountDown)
        initialCountDown -= 1
    }
    console.log("GO!")
}

function lapsRan(){
    let totalLaps = 3 //total laps can be changed 
    //how long do laps take?
    let lapsdistance=5
    //variable for laps completed
    let lapscompleted = 0
    //create a loop that does increments of the laps for the time a car crossed the racing checkpoint.
    while (totalLaps >= 1){
        while (lapsdistance >= 0){
            lapsdistance -= 1
        }
        lapscompleted += 1
        totalLaps -= 1

        console.log("Car crossed checkpoint! You have completed " + lapscompleted +" lap(s)! You have " +totalLaps + " left!"  )
    }
}

function completedRace(){
        console.log("Congratulations you crossed the finish line!")
    }

// setup announcer
//setup a way to restart the race so it can run again

countdown()
lapsRan()
completedRace()

let countEL = document.getElementById("count-el")

countEL.innerText