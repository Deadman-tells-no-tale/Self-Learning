package main
import (
	"fmt"
	"math/rand"
	"time"
)


func main(){
	rand.Seed(time.Now().Unix())
	restaurants:= []string{
		"Samurai Noodles",
		"Teriyaki Boy",
		"Lolo Hawaiian BBQ",
		"Leatherby's",
		"Panda Express",
		"Cubby's",
		"Black Bear Diner",
		"Garage Grill",
		"Oak Wood Fire Kitchen",
		"Big Eye Poke",
		"Even Stephen's Sandwhiches",
		}


	fmt.Println("here's your choice ya indecisive animals...", restaurants[rand.Intn(len(restaurants))])
}