# RandomBlenderCode

```
# this is meant to be copied, modified to your needs (in an external editor maybe)
# then pasted into blender console mostly (Shift+F4)
# i dont  know howto do it without 'if True:'
# if not mentioned otherwise: code snippets are for object mode
```

## Count
 - count selected objects and their vertices, print obj if > 60.000
 - also rename obj.data.name to obj.name
```
import bpy
if True:
  cVerts,cAll,i=0,0,0
  for m in [o.data for o in bpy.context.selected_objects if o.type == 'MESH']:
    o.data.name = o.name
    cVerts = len(m.vertices)
    if cVerts>=60000:
      print(str(cVerts) + ' vertices for object: ' + str(m.name))
    cAll = cAll + cVerts
    i=i+1
  print(str(i) + ' objects - ' + str(cAll) + ' vertices total')
```

## Rename
 - rename selected objects to "prefix+number+postfix"
 - set number i to start at whatever
 - also rename obj.data.name to obj.name
```
import bpy
if True:
  i=100
  prefix='prefix_'
  prefix='_postfix'
  start=i
  for ob in bpy.context.selected_objects:
    ob.name=prefix+str(i)+postfix
    i+=1
    if ob.type == 'MESH':
      ob.data.name=ob.name
    print(ob.name)
  print(str(i-start) + ' objects renamed')
```

## All normals up
 - for Assetto Corsa trees, grass, skyboxes
 - if you dont want/cant use naming conventions to make nice tree shadows
 - makes normals for all selected objects (see #quirky note) pointing upwards
```
# quirky note: you have to select all vertices in edit mode before 
# but the snippet itself works in object mode only
```
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

## ac-coordinates
 - usefull for AssettoCorsa animation makers
 - calc+print object's (Pivot-)position from blender world-pos (origin center of mass surface)
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
