import bpy
from random import randint
#Task A creating 50 Cubes
for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)
alphabet = "abcdefghijklmnopqrstuvwxyz"
zAxis = 2
yAxis = 2
for i in range(50):
    if zAxis == 2:
        zAxis = -2
    elif zAxis == -2:
        zAxis = 2
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False,
    align='WORLD', location=(yAxis, 0, zAxis), scale=(1, 1, 1))
    cube = bpy.context.selected_objects[0]
    randomName = ""
    yAxis += 2
    for i in range(3):
        randomName += alphabet[randint(0,len(alphabet)-1)]
        cube.name = randomName + "/" + str(randint(100, 999))
        
NumberOfObjects = 0 
for object in bpy.data.objects:
    NumberOfObjects += 1

numberOfMaterilas = 0
for material in bpy.data.materials:
    numberOfMaterilas += 1

print("Number of objects " + str(NumberOfObjects), "Number of materials " + str(numberOfMaterilas))
print("total number = " + str(NumberOfObjects+numberOfMaterilas))

#Task B
for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)
positions = [
[4,6,3],
[6,6,3],
[3,3,3],
[3,2,3],
[7,3,3],
[7,2,3],
[4,1,3],
[5,1,3],
[6,1,3]
]



for position in positions:
    r = randint(0,1000)/1000
    g = randint(0,1000)/1000
    b = randint(0,1000)/1000
    a = 1
    print(r,g,b)
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False,
    align='WORLD', location=(position[0], position[1], position[0]),
    scale=(1, 1, 1), rotation=(randint(0,360),randint(0,360),randint(0,360)))
    cube = bpy.context.selected_objects[0].data
    randomColor = bpy.data.materials.new(str(r)+str(g)+str(b))
    randomColor.diffuse_color = (r,g,b,a)
    cube.materials.append(randomColor)

#Task C
