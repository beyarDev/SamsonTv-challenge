import bpy
from random import randint
#Task A creating 50 Cubes
for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)
alphabet = "abcdefghijklmnopqrstuvwxyz"
zAxisCollection = []
zAxis = 0
yAxis = 0
memoZaxis = -1
vertices = 0
for i in range(50):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False,
    align='WORLD', location=(yAxis, 0, zAxis), scale=(1, 1, 1))
    cube = bpy.context.selected_objects[0]
    vertices += len(cube.data.vertices)
    randomName = ""
    yAxis += 1
    if zAxis < 3 and zAxis > memoZaxis:
        memoZaxis = zAxis
        zAxis += 1
    elif zAxis > -3:
        memoZaxis = zAxis
        zAxis -= 1
    else:
        zAxis += 1
        memoZaxis = zAxis -1
    for i in range(3):
        randomName += alphabet[randint(0,len(alphabet)-1)]
        cube.name = randomName + "/" + str(randint(100, 999))
        
NumberOfObjects = 0 
for object in bpy.data.objects:
    NumberOfObjects += 1

numberOfMaterilas = 0
for material in bpy.data.materials:
    numberOfMaterilas += 1



print("Number of objects " + str(NumberOfObjects), "Number of materials " + str(numberOfMaterilas), "Number of vertices " + str(vertices))
print("total number = " + str(NumberOfObjects+numberOfMaterilas + vertices))
#Task B

