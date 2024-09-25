from visualize_gates import draw_gate_packing
from copy import deepcopy
from time import monotonic as timer


# unoccupied or not =>logic: check with every rectangle before it (rectangles with more height)
def unoccupied_or_not(j, k, height, width, ind, rects, h, w):
    if j+height>h or k+width>w:return False
    for i in range(ind):
        
        rect = dims_and_coords[rects[i]]
        if ((j+height-1>=rect[2] and j<=rect[0]+rect[2]-1)
        and (k+width-1>=rect[3] and k<=rect[1]+rect[3]-1)):
            return False

    return True

# placing rectangles according to the priority order: top, left
def place(h, w, rects):

    ind = 0
    list_of_possible_places = [[0, 0]]
    for rect in rects:
        height, width = dims_and_coords[rect][:2]
        
        for i, j in list_of_possible_places:
            if unoccupied_or_not(i, j, height, width, ind, rects, h, w):
                list_of_possible_places.append([i+height, j])
                list_of_possible_places.append([i, j+width])
                dims_and_coords[rect][2] = i
                dims_and_coords[rect][3] = j
                list_of_possible_places.remove([i, j])
                break
            
        else:return False

        list_of_possible_places.sort()

        ind+=1

    return True

# dimensions and coordinates of rectangles
dims_and_coords = {}


# uncomment to get random input generator

import random
for i in range(random.randint(20, 30)):
    dims_and_coords["g"+str(i+1)] = [random.randint(5, 20), random.randint(5, 20), 0, 0]

"""
while True:
    try:
        n, height, width = input().split()
        # height width y-coordinate x-coordinate
        dims_and_coords[n] = [int(height), int(width), 0, 0]
    except:
        break
"""
"""
with open('input.txt', 'r') as file:
    for line in file:
        for n, height, width in [line.strip().split()]:
            dims_and_coords[n] = [int(height), int(width), 0, 0]"""
# TIMER START
start_time = timer()
curr_time = start_time


num_of_rect = len(dims_and_coords)

# rectangles
rectangles = ["g"+str(i) for i in range(1, num_of_rect+1)]
rectangles.sort(key = lambda x: dims_and_coords[x][0], reverse = True)

val = 0
for i in rectangles:
    dims_and_coords[i][3] = val
    val+=dims_and_coords[i][1]

h = dims_and_coords[rectangles[0]][0]
w = val+1
w_min = max([dims_and_coords[i][1] for i in rectangles])
h_max = sum([dims_and_coords[i][0] for i in rectangles])
checker = True
optimal_dims = [[h, w], deepcopy(dims_and_coords)]
total_area = sum([dims_and_coords[i][0]*dims_and_coords[i][1] for i in rectangles])

# change after every loop (to account for bigger inputs)
step = max(1, total_area*(num_of_rect)**2//int(5e9))

while w>=w_min and h<=h_max:
    if checker:
        w-=step
    else:
        h+=step

    if h*w < total_area:
        checker = False

    elif h*w > optimal_dims[0][0]*optimal_dims[0][1]:
        checker = True

    else:
        checker = place(h, w, rectangles)
        if checker:
            optimal_dims = [[h, w], deepcopy(dims_and_coords)]

    # CHECKING IF WE MIGHT EXCEED TIME LIMIT
    # STOPPING AFTER 4 MINUTES 30 SECONDS AND RETURNING THE BEST SOLUTION EXPLORED TILL THEN
    curr_time = timer()
    if curr_time-start_time>=270:
        break


dims_and_coords = optimal_dims[1]
h, w = optimal_dims[0]

print("DIMENSIONS OF THE BOUNDING BOX: h =",h, " w =",w)
print("PACKING EFFICIENCY =", total_area/(h*w)*100, "%")
print("RUN TIME =", round(curr_time-start_time, 2))

dimensions = {i:dims_and_coords[i][:2][::-1] for i in dims_and_coords}
coordinates = {"bounding_box":[w, h]}
coordinates.update({i:dims_and_coords[i][2:][::-1] for i in dims_and_coords})

"""
print("OUTPUT: \n")
for i in coordinates:
    print(i, *coordinates[i])
"""

with open('output.txt', 'w') as file:
    for i in coordinates:
        file.write(i+" "+" ".join([str(j) for j in coordinates[i]][::-1])+"\n")


height_of_grid = h*5//4
width_of_grid = w*5//4

# dict with dimensions, dict with coordinates, (w, h)
root = draw_gate_packing(dimensions, coordinates, (width_of_grid, height_of_grid))
root.mainloop()

