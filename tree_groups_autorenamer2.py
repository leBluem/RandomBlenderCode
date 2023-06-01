### paste this script in blender script editor

# -select all trees with same material
# -maybe switch to Local view
#
# 1. select some trees, only those you want to be in a group
# 2. run script, it renames them to something like this (free number found automatically)
# KSTREE_GROUP_ks0_0
# KSTREE_GROUP_ks0_1
# ...
# next group will get a higher number
# KSTREE_GROUP_ks1_0
# KSTREE_GROUP_ks1_1
# ...
# 3. after renaming, those trees will be hidden (unhide later with ALT+H)
# 4. repeat from step 1
#
# exit localview

import bpy, os, traceback

BASENAME     = 'KSTREE_GROUP_ks'
THECOUNTER   = 0
maxObjCount  = 1000
maxVertCount = 60000
doHide       = True

selected_objs = bpy.context.selected_objects.copy()
bpy.ops.object.select_all(action='DESELECT')

### find free name
allobjs = []
for obj in bpy.context.blend_data.objects:
    #if BASENAME.lower() in obj.name.lower():
    allobjs.append(obj.name.lower())

print(str(len(allobjs)))

THECOUNTER=-1
while THECOUNTER<100000:
    THECOUNTER+=1
    # if not (BASENAME.lower() + str(i)) in allobjs:
    dobreak = True
    for j in range(len(allobjs)):
        if (BASENAME.lower() + str(THECOUNTER))  in  allobjs[j]:
            dobreak = False
            break
    if dobreak:
        break

### tree group base name
prefix=BASENAME + str(THECOUNTER) + '_'
print(prefix)

c=0
obc=0
vertNums = 0
vertNumssel = 0

for obj in selected_objs:
    obc += 1
    vertNums += len(obj.data.vertices)

    ### failsafe to not include too much
    if vertNums < maxVertCount and obc < maxObjCount:
        vertNumssel = vertNums
        print('rename ' + prefix + str(c))

        ### rename!!!
        # obj.name = prefix + str(c)
        # obj.data.name = obj.name

        ### deselect/hide
        if doHide:
            # bpy.data.objects[ obj.name ].select_set(False)
            bpy.data.objects[obj.name].hide_set(True)
        # add 1
        c += 1
    else:
        ### not renamed! select again
        bpy.data.objects[ obj.name ].select_set(True)

print(str(len(selected_objs)-c) + ' still selected, ' +  str(c) + ' objs renamed, ' + str(vertNumssel) + ' verts')
