import numpy as np
import random
import math
from time import perf_counter

gates = {}
pins = {}
clusters = {}

class Pin:
    def __init__(self, name, x, y):
        self.name = name
        self.gate_name = name.split(".")[0]
        self.x = x
        self.y = y
        self.directly_connected_pins = []
        self.parent_pin = 0

class Gate:
    def __init__(self, name, width, height, pins):
        self.name = name         # Name of the gate (e.g., "g1", "g2")
        self.width = width       # Width of the gate
        self.height = height     # Height of the gate
        self.x = 0               # X-coordinate of the bottom-left corner
        self.y = 0               # Y-coordinate of the bottom-left corner
        self.pins = pins

    """def __repr__(self):
        return f"{self.name}: ({self.x}, {self.y}), W: {self.width}, H: {self.height}"
    """

    def overlaps(self, other):
        return not (self.x + self.width <= other.x or other.x + other.width <= self.x or
                    self.y + self.height <= other.y or other.y + other.height <= self.y)

def estimate_total_wire_length():
    estimated_wire_length = 0
    for i in clusters:
        min_x = gates[clusters[i][0].gate_name].x + clusters[i][0].x
        min_y = gates[clusters[i][0].gate_name].x + clusters[i][0].x
        max_x = gates[clusters[i][0].gate_name].y + clusters[i][0].y
        max_y = gates[clusters[i][0].gate_name].y + clusters[i][0].y
        for j in clusters[i]:
            min_x = min(min_x, gates[j.gate_name].x + j.x)
            max_x = max(max_x, gates[j.gate_name].x + j.x)
            min_y = min(min_y, gates[j.gate_name].y + j.y)
            max_y = max(max_y, gates[j.gate_name].y + j.y)
        estimated_wire_length += max_x-min_x + max_y-min_y

    return estimated_wire_length

def swap_gates(order):
    i, j = random.sample(range(len(gates)), 2)
    new_order = order[:]
    gates[order[i]].x, gates[order[j]].x = gates[order[j]].x, gates[order[i]].x
    gates[order[i]].y, gates[order[j]].y = gates[order[j]].y, gates[order[i]].y
    new_order[i], new_order[j] = new_order[j], new_order[i]
    return new_order

def min_expression(c, d):
    return 3*(c+d) + abs(c-d)

def check_for_overlaps(gate):
    for i in gates:
        if i!=gate and gates[i].overlaps(gates[gate]):
            return True
    return False

def check_all_overlaps():
    for i in range(len(gates)):
        for j in range(i+1, len(gates)):
            i1 = "g"+str(i+1)
            j1 = "g"+str(j+1)
            if gates[i1].overlaps(gates[j1]):
                return True
    return False


def place_gates(gates_list, max_height, max_width, dim_grid):
    ct = 0
    for i in gates_list:
        gates[i].x = max_width*(ct%dim_grid)
        gates[i].y = max_height*(ct//dim_grid)
        ct+=1

def compress(best_orientation):
    for i in best_orientation[1]:
        while gates[i].x>=0 and not check_for_overlaps(i):
            gates[i].x-=1
        gates[i].x+=1
    for i in best_orientation[1]:
        while gates[i].y>=0 and not check_for_overlaps(i):
            gates[i].y-=1
        gates[i].y+=1

def print_gates(l = gates):
    for i in l:
        print(i, l[i].x, l[i].y)


def solve(max_iter, start_temperature, alpha, init_order, max_height, max_width, dim_grid):
    curr_temperature = start_temperature
    place_gates(init_order, max_height, max_width, dim_grid)
    curr_orientation = [estimate_total_wire_length(), init_order]
    curr_order = init_order[:]
    best_orientation = [curr_orientation[0], init_order] # O(1000)
    iteration = 0
    interval = (int)(max_iter / 10)
    while iteration < max_iter: # O(1000)
        new_order = swap_gates(curr_order) # O(1)
        new_orientation = estimate_total_wire_length() # O(40000)
        if new_orientation < curr_orientation[0]:  # better route so accept
            curr_orientation = [new_orientation, new_order] # O(1000)
            curr_order = new_order[:]
            if curr_orientation[0] < best_orientation[0]:
                best_orientation = [new_orientation, new_order] # O(1000)

        else:          # adjacent is worse
            accept_p = np.exp((curr_orientation[0] - new_orientation) / curr_temperature)
            p = random.random()
            if p < accept_p:  # accept anyway
                curr_orientation = [new_orientation, new_order] # O(1000)
                curr_order = new_order[:]
            # else don't accept
        if iteration % interval == 0:
            print("iter = %6d | curr error = %7.2f | temperature = %10.4f " % (iteration, best_orientation[0], curr_temperature))

        if curr_temperature < 0.00001:
            curr_temperature = 0.00001
        else:
            curr_temperature *= alpha
        iteration += 1

    place_gates(best_orientation[1], max_height, max_width, dim_grid) # O(1000)
    compress(best_orientation) # O(1000*1000*1000*100)
    best_orientation[0] = estimate_total_wire_length() # O(40000)

    return best_orientation

def eval_line_of_pins(l, curr_gate, pins):
    t = []
    for i in range(0, len(l), 2):
        name = curr_gate[0]+".p"+str(i//2+1)
        t.append(Pin(name, int(l[i]), int(l[i+1])))
        pins[name] = t[-1]
    return t

def calc_bounding_box():
    min_x = gates["g1"].x
    max_x = min_x + gates["g1"].width
    min_y = gates["g1"].y
    max_y = min_y + gates["g1"].height
    for i in gates:
        min_x = min(min_x, gates[i].x)
        max_x = max(max_x, gates[i].x+gates[i].width)
        min_y = min(min_y, gates[i].y)
        max_y = max(max_y, gates[i].y+gates[i].height)
    return (max_x - min_x), (max_y - min_y)

def main():
    print("\nBegin Wiring Aware Gate Positioning simulated annealing demo ")
    # test_case_1000_gates.txt
    with open("input3.txt", 'r') as file:
        is_gate = 0
        curr_gate = ["", 0, 0, []]
        for line in file:
            if line[0] == "g":
                is_gate = 1
                curr_gate[0] = line.split()[0]
                curr_gate[1] = int(line.split()[1])
                curr_gate[2] = int(line.split()[2])
            else:
                if is_gate==1:
                    curr_gate[3] = eval_line_of_pins(line.split()[2:], curr_gate, pins)
                    gates[curr_gate[0]] = Gate(*curr_gate)
                else:
                    pin1 = (line.split()[1])
                    pin2 = (line.split()[2])
                    pins[pin1].directly_connected_pins.append(pins[pin2])
                    pins[pin2].directly_connected_pins.append(pins[pin1])
                    par1 = pins[pin1].parent_pin
                    par2 = pins[pin2].parent_pin
                    if par1 != 0 and par2 == 0:
                        pins[pin2].parent_pin = par1
                        clusters[par1.name].append(pins[pin2])
                    elif par2 != 0 and par1 == 0:
                        pins[pin1].parent_pin = par2
                        clusters[par2.name].append(pins[pin1])
                    elif par1 != 0 and par2 != 0:
                        if par1==par2:
                            continue
                        temp = par2.name
                        for i in clusters[temp]:
                            i.parent_pin = par1
                            clusters[par1.name].append(i)
                        del clusters[temp]
                    else:
                        parent = pins[pin1]
                        pins[pin1].parent_pin = parent
                        pins[pin2].parent_pin = parent
                        clusters[parent.name] = [pins[pin1], pins[pin2]]
                is_gate = 0

    l = [i for i in gates]
    random.shuffle(l)

    max_height = max([gates[i].height for i in gates])
    max_width = max([gates[i].width for i in gates])
    dim_grid = int(math.ceil(math.sqrt(len(l))))

    max_iter = round(10**6/math.pow(len(l), 0.5), -1)
    start_temperature = 50000*dim_grid*(max_height+max_width)
    alpha = math.pow(start_temperature, -1.2/max_iter)

    print("\nSettings: ")
    print("max_iter = %d " % max_iter)
    print("start_temperature = %0.1f " % start_temperature)
    print("alpha = %0.5f " % alpha)
    print("number of gates =", len(l))

    start_time = perf_counter()

    soln = solve(max_iter, start_temperature, alpha, l, max_height, max_width, dim_grid)
    print("bounding_box", *calc_bounding_box())
    print_gates(gates)
    print("wire_length",soln[0])

    end_time = perf_counter()
    print("\n\nTime taken by program:", end_time-start_time)

if __name__ == "__main__":
    main()