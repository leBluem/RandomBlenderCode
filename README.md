# RandomBlenderCode

```
# this is for blender console mostly (Shift+F4)
# i dont  know howto do it without 'if True:'
```

## Count
 - count objects/vertices, print obj if > 60.000
 - also rename obj.data to meshname
```
import bpy
if True:
  cVerts,cAll,i=0,0,0
  for m in [o.data for o in bpy.context.selected_objects if o.type == 'MESH']:
    ob.data.name = ob.name
    cVerts = len(m.vertices)
    if cVerts>=60000:
      print(str(cVerts) + ' vertices for object: ' + str(m.name))
    cAll = cAll + cVerts
    i=i+1
  print(str(i) + ' objects - ' + str(cAll) + ' vertices total')
#end script
```

## Rename
 - rename selected to "prefix+number+postfix"
 - set number i to start at whatever
 - also rename obj.data to meshname
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
#end script
```
