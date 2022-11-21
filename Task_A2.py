# For the purpose of finding the run-time: 
import time
start_time = time.time()


"""

A* grid planning

author: Atsushi Sakai(@Atsushi_twi)
        Nikos Kanargias (nkana@tee.gr)

See Wikipedia article (https://en.wikipedia.org/wiki/A*_search_algorithm)

"""


# Code for importing all the modules
from contextlib import nullcontext
import math
import numpy as np
import matplotlib.pyplot as plt
import random


# Statement for showing the path planning animation
show_animation = True


class AStarPlanner:


    """
    Initialize grid map for a star planning

    ox: x position list of Obstacles [m]
    oy: y position list of Obstacles [m]
    resolution: grid resolution [m]
    rr: robot radius[m]
    fc_x and fc_y: coordinates of fuel consuming area [m]
    tc_x and tc_y: coordinates of time consuming area [m]
    jc_x and jc_y: coordinates of jet stream area [m]
    """
    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y):

        self.resolution = resolution # get resolution of the grid
        self.rr = rr # robot radis
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model() # motion model for grid search expansion
        self.calc_obstacle_map(ox, oy)

        self.fc_x = fc_x
        self.fc_y = fc_y

        self.Delta_C2 = 0.4 # cost intensive area 2 modifier

        self.costPerGrid = 1 


    # Definition of a sinle node
    class Node: 
        

        def __init__(self, x, y, cost, parent_index):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index


        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)


    """
    A star path search

    input:
        s_x: start x position [m]
        s_y: start y position [m]
        gx: goal x position [m]
        gy: goal y position [m]

    output:
        rx: x position list of the final path
        ry: y position list of the final path
    """
    def planning(self, sx, sy, gx, gy):

        start_node = self.Node(self.calc_xy_index(sx, self.min_x), # calculate the index based on given position
                               self.calc_xy_index(sy, self.min_y), 0.0, -1) # set cost zero, set parent index -1
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x), # calculate the index based on given position
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict() # open_set: node not been tranversed yet. closed_set: node have been tranversed already
        open_set[self.calc_grid_index(start_node)] = start_node # node index is the grid index

        while 1:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(self, goal_node,
                                                                     open_set[
                                                                         o])) # g(n) and h(n): calculate the distance between the goal node and openset
            global current # Making current a global variable so we could use it in the trip_cost function. 
            current = open_set[c_id]

            # show graph
            if show_animation:  # pragma: no cover
                plt.plot(self.calc_grid_position(current.x, self.min_x),
                         self.calc_grid_position(current.y, self.min_y), "xc")
                # for stopping simulation with the esc key.
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event: [exit(
                                                 0) if event.key == 'escape' else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

            # reaching goal
            if current.x == goal_node.x and current.y == goal_node.y:
                print("Total Trip time required -> ",current.cost )
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            # print(len(closed_set))

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion): # tranverse the motion matrix
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2] * self.costPerGrid, c_id)
                
                # add more cost in cost intensive area 2
                if self.calc_grid_position(node.x, self.min_x) in self.fc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.fc_y:
                        # print("cost intensive area!!")
                        node.cost = node.cost + self.Delta_C2 * self.motion[i][2]
                
                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)
        # print(len(closed_set))
        # print(len(open_set))

        return rx, ry
    
    
    # This is a copy of the previous planning function while deleting the part where the program plots all the possible nodes. 
    def planning_no_animation(self, sx, sy, gx, gy):

        start_node = self.Node(self.calc_xy_index(sx, self.min_x), # calculate the index based on given position
                               self.calc_xy_index(sy, self.min_y), 0.0, -1) # set cost zero, set parent index -1
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x), # calculate the index based on given position
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict() # open_set: node not been tranversed yet. closed_set: node have been tranversed already
        open_set[self.calc_grid_index(start_node)] = start_node # node index is the grid index

        while 1:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(self, goal_node,
                                                                     open_set[
                                                                         o])) # g(n) and h(n): calculate the distance between the goal node and openset
            global current # Making current a global variable so we could use it in the trip_cost function. 
            current = open_set[c_id]

            # reaching goal
            if current.x == goal_node.x and current.y == goal_node.y:
                print("Total Trip time required -> ",current.cost )
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            # print(len(closed_set))

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion): # tranverse the motion matrix
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2] * self.costPerGrid, c_id)
                
                ## add more cost in cost intensive area 1
                if self.calc_grid_position(node.x, self.min_x) in self.tc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.tc_y:
                        # print("cost intensive area!!")
                        node.cost = node.cost + self.Delta_C1 * self.motion[i][2]
                
                # add more cost in cost intensive area 2
                if self.calc_grid_position(node.x, self.min_x) in self.fc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.fc_y:
                        # print("cost intensive area!!")
                        node.cost = node.cost + self.Delta_C2 * self.motion[i][2]

                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)
        # print(len(closed_set))
        # print(len(open_set))

        return rx, ry

    # Generate final course
    def calc_final_path(self, goal_node, closed_set):

        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)] # save the goal node as the first point
        
        parent_index = goal_node.parent_index
        
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry


    @staticmethod
    def calc_heuristic(self, n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        d = d * self.costPerGrid
        return d
    

    def calc_heuristic_maldis(n1, n2):
        w = 1.0  # weight of heuristic
        dx = w * math.abs(n1.x - n2.x)
        dy = w *math.abs(n1.y - n2.y)
        return dx + dy


    """
    calc grid position

    :param index:
    :param min_position:
    :return:
    """
    def calc_grid_position(self, index, min_position):
        pos = index * self.resolution + min_position
        return pos


    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    
    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x) 

    
    def verify_node(self, node):
        
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False

        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True


    def calc_obstacle_map(self, ox, oy):

        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))
        print("min_x:", self.min_x)
        print("min_y:", self.min_y)
        print("max_x:", self.max_x)
        print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
        print("x_width:", self.x_width)
        print("y_width:", self.y_width)

        # obstacle map generation
        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)] # allocate memory
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x) # grid position calculation (x,y)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy): # Python’s zip() function creates an iterator that will aggregate elements from two or more iterables. 
                    d = math.hypot(iox - x, ioy - y) # The math. hypot() method finds the Euclidean norm
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True # the griid is is occupied by the obstacle
                        break


    @staticmethod
    def get_motion_model(): # the cost of the surrounding 8 points
        # dx, dy, cost
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1]]

        return motion


# (Task 1) Function for calculating the trip cost from avaliable numbers of each scenario
def trip_cost(passengers, weeks, max_flight, time_cost, fuel_cost):
    
    # The ceiling function rounds the number of flights to a larger integer (eg. from 2.3 to 3 flights).
    A321_num_flight = math.ceil(passengers/200)
    A330_num_flight = math.ceil(passengers/300)
    A350_num_flight = math.ceil(passengers/350)
    
    # Setting the time cost each possible aircraft type
    if time_cost=="low":
        CT_A321 = 10
        CT_A330 = 15
        CT_A350 = 20
    elif time_cost=="medium":
        CT_A321 = 15
        CT_A330 = 21
        CT_A350 = 27
    elif time_cost=="high":
        CT_A321 = 20
        CT_A330 = 27
        CT_A350 = 34
    
    # The total amount of flight that is allowed in the scenario specified
    total_flight_allowed = weeks*max_flight
    
    # Determining whether an aircraft could fulfill the capacity reqirements. If yes, then proceed to calculating the trip cost. 
    # If statements are used to determine whether the number for flights needed exceeds the total amount of flights allowed in the scenario. 
    if A321_num_flight>total_flight_allowed:
        A321 = "The A321neo aircraft could not fulfill the specified capacity."
        print (A321)
    else: 
        A321 = (fuel_cost*54*current.cost+CT_A321*current.cost+1800)*A321_num_flight
        print ("The trip cost for using {} flights of A321 is ${:.2f}".format(A321_num_flight, A321))
    
    if A330_num_flight>total_flight_allowed:
        A330 = "The A330-900neo aircraft could not fulfill the specified capacity."
        print (A330)
    else: 
        A330 = (fuel_cost*84*current.cost+CT_A330*current.cost+2000)*A330_num_flight
        print ("The trip cost for using {} flights of A330 is ${:.2f}".format(A330_num_flight, A330))
    
    if A350_num_flight>total_flight_allowed:
        A350 = "The A350-900 aircraft could not fulfill the specified capacity."
        print (A350)
    else: 
        A350 = (fuel_cost*90*current.cost+CT_A350*current.cost+2500)*A350_num_flight
        print ("The trip cost for using {} flights of A350 is ${:.2f}".format(A350_num_flight, A350))
    
    # Setting up an array to store all the cost information so that we could use the function min() to determine the minmum cost needed. 
    comparasion_array = np.array([])
     
    '''
    The if statements are used to see if the cost variables(A321, A330, and A350) are floats or not.
    Recall that if the aircraft's capacity does not fulfill the capacity requirements, we set the cost variables to a string that says the capacity is not enough. 
    Thus, if the aircraft does fulfill the capacity requirements, we could then proceed to storing its cost into the comparasion array. 
    '''
    if isinstance(A321, float)==True:
        comparasion_array = np.append(comparasion_array, A321)
    if isinstance(A330, float)==True:
        comparasion_array = np.append(comparasion_array, A330)
    if isinstance(A350, float)==True:
        comparasion_array = np.append(comparasion_array, A350)
    
    # To find the lowest cost stored into the array
    lowest_cost = comparasion_array.min()
    
    # To find which aircraft type the lowest cost belongs to and print the results
    if lowest_cost==A321:
        print("{} flights of A321 will yield the lowest cost of ${:.2f}".format(A321_num_flight,A321))
    elif lowest_cost==A330:
        print("{} flights of A330 will yield the lowest cost of ${:.2f}".format(A330_num_flight,A330))
    elif lowest_cost==A350:
        print("{} flights of A350 will yield the lowest cost of ${:.2f}".format(A350_num_flight,A350))


# (Task 2) Function for finding the best jet stream area that yields in a minimal cost per flight (minimum flight duration)
def jet_stream(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y, sx, sy, gx, gy):
    
    # Create an empty dictionary that will be used to store all the possible costs for each iteration runned.
    comparasion_dict = {}
    
    # Running all the possible jet stream areas to calculate the cost and storing the values into the comparasion dictionary.
    for k in range(-10, 56):
        # Set the jet stream area in the current iteration
        jc_x, jc_y = [], []
        for i in range(-10, 60):
            for j in range(k, k+5):
                jc_x.append(i)
                jc_y.append(j)
        # Run the AStar algorithm without plotting the animations to determine the cost for the current iteration.
        a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y, jc_x, jc_y)
        rx, ry = a_star.planning_no_animation(sx, sy, gx, gy)
        # Storing the current cost for this iteration to the comparasion dictionary
        comparasion_dict[k] = [current.cost]
    
    # Finding the key (ymin) for the minimum cost within the comparasion dictionary and turning its datatype from tuple into integer
    ymin = min(comparasion_dict.keys(), key=(lambda k: comparasion_dict[k]))
    ymax = ymin + 5

   # set jet stream area 3 (fuel-conserving area)
    jc_x, jc_y = [], []
    for i in range(-10, 60):
        for j in range(ymin, ymax):
            jc_x.append(i)
            jc_y.append(j)
    
    return jc_x, jc_y, ymin, ymax


# (Task 3) Function that calculates and returns the cost per flight according to scenario 1 and the first line in the fuel cost table, given the aircraft's capacity
def aircraft_cost(capacity):
    
    T_best = current.cost  # T_best is the cruising time of the flight
    
    # To determine the fixed cost per flight and the total rate of fuel consumption of all engines (whether the plane has 2 engines or 4 engines), depending on the aircraft's capacity.
    if capacity >= 300:
        Cc = 2500
        delta_F = 20*4
    else:
        Cc = 2000
        delta_F = 20*2
    
    CF = 882.30/1000  # CF is the fuel cost in $/kg ($882.30 per metric tonnes from the fuel cost table provided - "Jet Fuel Price" - first row)
    
    CT = 12 + math.floor(capacity/50)*2  # CT is the time related cost per minute of flight (base CT = $12/min, for every 50 passengers increase CT by $2)
    # The floor function is used here to round the numbers of groups of 50 passengers to the lower number (eg. if there are 70 passengers, we only increase CT by one $2)

    # To calculate the total cost of one flight, according to the cost equation
    C = CF * delta_F * T_best + CT * T_best + Cc
    
    # Returning the result of the total cost
    return C


# (Task 3) Function for finding the minimum cost per flight; printing out the result for the optimal aircraft capacity and engine count
def optimal_cost():
    
    # The cost for having the maximum amount of capacity alotted on an aircraft (we stored it here so that the following calculation costs could have a starting value to compare with)
    cost = aircraft_cost(450) 
    
    # Running every possible capacity and calculating its cost
    for c in range (100, 451):
        # If the capacity does not meet the capacity reqirement, skip the calcuation for its cost
        if c*12<3000:
            continue
        # If the new cost of the capacity running in this iteration is smaller than the previously stored cost, store this capacity and its cost for comparasion in the next iteration. 
        if aircraft_cost(c)<cost:
            capacity = c
            cost = aircraft_cost(c)
    
    # Finding the amount of engines needed for the optimal capacity
    if capacity >= 300:
        engine_count = 4
    else:
        engine_count = 2
    
    # Printing the results
    print("The optimal passenger capacity for scenario 1 is {}. There are {} engines on the aircraft. This yields in a minimal operating cost of ${:.2f} per flight.". format(capacity, engine_count, cost))


# (Additional Task 2) Function for randomly generating obstacles according to a given relativistic density
def random_obstacles (ox, oy, number_of_obstacles):
    
    for i in range(0, number_of_obstacles):
        x = random.randint(-10,60)
        y = random.randint(-10,60)
        ox.append(x)
        oy.append(y)

    return ox, oy


def main():
    
    print(__file__ + " start the A star algorithm demo !!") # print simple notes

    # Start and goal position
    sx = 10.0  # [m]
    sy = 0.0  # [m]
    gx = 0.0  # [m]
    gy = 40.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]

    # Set fuel-consuming area
    lower_x = random.randint(-10,30)
    lower_y = random.randint(-10,30)
    fc_x, fc_y = [], []
    for i in range(lower_x, lower_x+30):
        for j in range(lower_y, lower_y+30):
            fc_x.append(i)
            fc_y.append(j)

    # Set obstacle positions (graph's border)
    ox, oy = [], []
    for i in range(-10, 60): # draw the button border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60): # draw the right border
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60): # draw the top border
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60): # draw the left border
        ox.append(-10.0)
        oy.append(i)

    # Setting the randomly occuring obstacles
    random_obstacles (ox, oy, 600)
    
    # Plotting the opstacles, positions, areas, axes, and grids
    if show_animation:  # pragma: no cover
        plt.plot(fc_x, fc_y, "oy") # plot the cost intensive area 1
        
        plt.plot(ox, oy, ".k") # plot the obstacle
        plt.plot(sx, sy, "og") # plot the start position 
        plt.plot(gx, gy, "xb") # plot the end position

        plt.grid(True) # plot the grid to the plot panel
        plt.axis("equal") # set the same resolution for x and y axis 
    
    print("The results of the compulsory tasks start here:")
    a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-r") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.show() # show the plot


if __name__ == '__main__':
    main()


# For the purpose of finding the total run time: 
print("Program execution time: " , time.time()-start_time)
