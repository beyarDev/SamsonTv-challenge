import bpy
from random import randint
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

