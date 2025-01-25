# RandomBlenderCode

```
# specific for modelling stuff for AssettoCorsa racing simulator, Blender 2.8
# this is meant to be copied, modified to your needs (in an external editor maybe)
# then pasted into blender console mostly (Shift+F4)
# i dont know howto do it without 'if True:' sometimes
# if not mentioned otherwise: code snippets are for object mode
```

## rename objects by used imagefile
 - for all selected objects: take first material, first image used, put its name infront of objectname
```
import bpy, sys
selected_objs = bpy.context.selected_objects.copy()
for obj in selected_objs:
  for s in obj.material_slots:
    if s.material and s.material.use_nodes:
      for n in s.material.node_tree.nodes:
        if n.type == 'TEX_IMAGE':
          imageA = str(n.image.filepath).split('\\')
          if len(imageA)>1:
            image = imageA[len(imageA)-1]
          else:
            image = imageA[0]
          if not image in obj.name:
            obj.name = image + obj.name
            obj.data.name = obj.name
```

## all normals up
 - for Assetto Corsa trees, grass, skyboxes
 - in edit mode: select all (or verts to change), then in object mode run the script
 - if you dont want/cant use naming conventions to make nice tree shadows
 - makes normals for all selected objects pointing upwards
```
import bpy
objs = bpy.context.selected_objects
for o in objs:
  me = o.data
  me.use_auto_smooth = True
  # Normal custom verts on each axis
  me.normals_split_custom_set([(0, 0, 0) for l in me.loops])
  # Set normal for selected vertices
  normals = []
  for v in me.vertices:
    if v.select:
      normals.append((0, 1, 0))
    else:
      normals.append(v.normal)
  # make csn's all face up.
  me.normals_split_custom_set_from_vertices(normals)
```

## print ac-coordinates
 - usefull for AssettoCorsa animation makers
 - calc+print AC-coordinates from objects (Pivot-)position from blender world-pos (origin center of mass surface)
 - if you are working with different scaling you might need to remove the '*100' part three times
```
import bpy
for ob in bpy.context.selected_objects:
  ss=str(ob.matrix_world.to_translation()).replace('<Vector (','')
  ss=ss.replace(')>','')
  ss=ss.replace(' ','')
  sss = ss.split(',')
  print('PIVOT_POS='
      +str(round(float(sss[0])*100.0, 4) )+', '
      +str(round(float(sss[2])*100, 4) ) + ', '
      +str(round(float(sss[1])*(-100.0), 4) ) + '  ;' + ob.name )
```

## count objects and vertices
 - count selected objects and their vertices, print obj if > 60.000
 - also rename obj.data.name to obj.name
```
import bpy
if True:
  cVerts,cAll,i=0,0,0
  for m in [o.data for o in bpy.context.selected_objects if o.type == 'MESH']:
    cVerts = len(m.vertices)
    if cVerts>=60000:
      print(str(cVerts) + ' vertices for object: ' + str(m.name))
    cAll = cAll + cVerts
    i=i+1
  print(str(i) + ' objects - ' + str(cAll) + ' vertices total')
```

## renaming objects
 - rename selected objects to "prefix+number+postfix"
 - set number i to start at whatever
 - also rename obj.data.name to obj.name
```
import bpy
if True:
  i=100
  prefix='prefix_'
  postfix='_postfix'
  start=i
  for ob in bpy.context.selected_objects:
    ob.name=prefix+str(i)+postfix
    i+=1
    if ob.type == 'MESH':
      ob.data.name=ob.name
    print(ob.name)
  print(str(i-start) + ' objects renamed')
```
```
import bpy
if True:
  prefix='AC_POBJECT_'
  postfix=''
  i=1
  start=i
  for ob in bpy.context.selected_objects:
    ob.name=prefix+str(i)+postfix
    i+=1
    if ob.type == 'MESH':
      ob.data.name=ob.name
    print(ob.name)
  print(str(i-start) + ' objects renamed')
```
## remove double materials - removes ie. ".00x"; use this as a script in Blender rather than on console only:
  - source: https://blender.stackexchange.com/a/195474
```
import bpy

def replace_material(bad_mat, good_mat):
    bad_mat.user_remap(good_mat)
    bpy.data.materials.remove(bad_mat)

def get_duplicate_materials(og_material):
    common_name = og_material.name
    if common_name[-3:].isnumeric():
        common_name = common_name[:-4]
    duplicate_materials = []
    for material in bpy.data.materials:
        if material is not og_material:
            name = material.name
            if name[-3:].isnumeric() and name[-4] == ".":
                name = name[:-4]

            if name == common_name:
                duplicate_materials.append(material)

    text = "{} duplicate materials found"
    print(text.format(len(duplicate_materials)))
    return duplicate_materials

def remove_all_duplicate_materials():
    i = 0
    while i < len(bpy.data.materials):
        og_material = bpy.data.materials[i]
        print("og material: " + og_material.name)
        # get duplicate materials
        duplicate_materials = get_duplicate_materials(og_material)
        # replace all duplicates
        for duplicate_material in duplicate_materials:
            replace_material(duplicate_material, og_material)

        # adjust name to no trailing numbers
        if og_material.name[-3:].isnumeric() and og_material.name[-4] == ".":
            og_material.name = og_material.name[:-4]
        i = i+1

remove_all_duplicate_materials()
```
