#Task C
import bpy
for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)
    
def makeFractal(scales=6, n=2,x=3,r=3, locations = [0,0,0], rotations = [0,0,0]):
    xAxis = 0
    yAxis = 0
    zAxis = 0
    bpy.ops.mesh.primitive_cone_add(
    vertices=3,
    radius1=1.0,
    radius2=0.0,
    depth=2.0,
    end_fill_type='NGON',
    calc_uvs=True,
    enter_editmode=False,
    align='WORLD',
    location=(locations[0], locations[1], locations[2]),
    rotation=(rotations[0],rotations[1], rotations [2]),
    scale=( scales, scales, scales),
    )
    if n == 2 and x==3 and r==3:
        scales = scales / 2
    r -= 1
    if r == 0:
        x-=1
        r=3
    if x ==0:
        n-=1
        x=3
        scales = scales / 2
    locations[0] += 3
    locations[1] -= 3
    locations[2] += 3
    if n == 0:
        return
    makeFractal(scales, n,x,r,locations,rotations)
makeFractal()