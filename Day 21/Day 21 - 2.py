

def cal_weight_on_planet(weight_on_earth, surface_gravity_of_planet):
	mass = weight_on_earth/9.8
	mass = round(mass, 2)
	return mass * surface_gravity_of_planet

print(cal_weight_on_planet(100, 23.1))

