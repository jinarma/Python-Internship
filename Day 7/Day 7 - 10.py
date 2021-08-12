from math import pi as PI

def area_of_circle(radius):
	return PI*pow(radius, 2)

R = int(input('Enter the radius of circle (cm): '))

area = area_of_circle(R)
print('{%.2f} sqcm'.format(area))
