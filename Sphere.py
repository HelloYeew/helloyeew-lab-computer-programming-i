import math
r = float(input("Enter sphere radius: "))
def sphere_volume(r):
    return (4 / 3) * math.pi * (r ** 3)
    print(f"Sphere volume is {sphere_volume(sphere_radius)}")
def sphere_surface_area(r):
    return 4 * math.pi * (r ** 2)
    print(f"Sphere surface area is {sphere_surface_area(sphere_radius)}")
sphere_volume(r)
sphere_surface_area(r)
print(f"Sphere volume is {sphere_volume(r):.2f}")
print(f"Sphere surface area is {sphere_surface_area(r):.2f}")
