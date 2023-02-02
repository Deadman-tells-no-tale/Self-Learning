"""#Fueltype = list("woodpellets,gas,coal,log,firewood,Softwood_dry,Softwood_wet,Hardwood_dry, Hardwood_wet,peat,lignite,subbituminous,bituminous,anthracite")

from time import time


create a fuel type
create a firebox  type
types of wood 
types of coal
types of gas
how much smoke
how long will burn roughly
ease of starting?
coal quality
types of coal
smell good?
quantity of wood burning at once.
type of wood placement or effeciency
efficiency = output/input*100
calculate heat
calculate burn time
calculate smoke production
calculate woodmath (length times volume )
"""



is_covered = False
is_smoking = False
is_on_fire = False


fuel_source ={
    "Pellets":["Alder","Almond","Apple","Apricot","Cherry","Chestnut","Hickory","Lemon","Maple","Mesquite","Mulberry","Nextarine","Oak","Orange","Peach","Pear","Pecan","Plum","Walnut"],
    "HardWood":["Oak","Birch","Ash","Walnut","Hickory","Pecan","White_Oak","Beech","Red_Oak","Yellow_Birch","Green_Ash","Black_Walnut","Maple","Cherry","Hackberry","Gum","Elm","Sycamore","Alder","Yellow_Poplar","Cottonwood","Basswood","Aspen"],
    "SoftWood":["Cedar","Fir","Juniper","Pine","Redwood","Spruce","Yew"],
    "Charcoal": "coal",
    "Coal":"Peat",
    "Propane": "gas"

}
fuel_source = input("select the type of fuel are you using?: (pellets(1),wood(2),coal(3),propane(4), fantasy(5)")
    #if fuel_source ==
fuel_type = fuel_source
    # Define the parameters of the simulation
wood_heat_rate = 1000 # Heat released by the wood per second (in Joules/s)
water_heat_capacity = 4200 # Heat capacity of water (in Joules/degree Celsius)
water_temperature_initial = 20 # Initial temperature of the water (in degrees Celsius)
water_temperature_final = 100 # Final temperature of the water (in degrees Celsius)
    
    # Calculate the total heat required to raise the water temperature
heat_required = (water_temperature_final - water_temperature_initial) * water_heat_capacity
    
    # Calculate the length of time that the wood will burn
burn_time = heat_required / wood_heat_rate
print(f"The wood will burn for {burn_time:.2f} seconds.")
