<div id="banner" align="left">
  <img src="https://user-images.githubusercontent.com/116058486/203708031-691173f6-6e02-424b-b602-3207e43d11ed.gif" width=100% height=auto object-fit=cover/>
</div>

<div id="header" align="center">
  <h1>PROJECT REPORT - GROUP 12</h1>
  <p>Members: Louise Zhou (zhlouise), Rainy Yuen (itsssraining), Anson Wong (Ansonwong88), Samuel Yau (SamuelYcy), Aidan Yau (yhpAidan), Angela Xu (Angelaxu2019), Mark Yao (Markyaoxin), Haoyang Yu (YU-Haoyang22101598d)<p>
</div>

# Presentation Link

<!-- Table of Content-->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#Background-of-Path-Planning-to-Aviation-Engineering">Background of Path Planning to Aviation Engineering</a></li>
    <li><a href="#Theory-of-Path-Planning-Algorithm">Theory of Path Planning Algorithm</a></li>
    <li>
      <a href="#Introduction-of-the-Engineering-Tools">Introduction of the Engineering Tools</a>
      <ol>
        <li><a href="#a-Python">Python</a></li>
        <li><a href="#b-GitHub">GitHub</a></li>
      </ol>
    </li>
    <li>
      <a href="#Compulsory-Task-1---Best-Aircraft-for-the-Given-Scenarios">Compulsory Task 1 - Best Aircraft for the Given Scenarios</a>
      <ol>
        <li><a href="#a-Methodology">Methodology</a></li>
        <li><a href="#b-Results">Results</a></li>
      </ol>
    </li>
    <li>
      <a href="#Compulsory-Task-2---Designing-Jet-Stream-Area">Compulsory Task 2 - Designing Jet Stream Area</a>
      <ol>
        <li><a href="#a-Methodology">Methodology</a></li>
        <li><a href="#b-Results">Results</a></li>
        <li><a href="#c-Discussion">Discussion</a></li>
      </ol>
    </li>
    <li>
      <a href="#Compulsory-Task-3---Designing-an-Aircraft">Compulsory Task 3 - Designing an Aircraft</a>
      <ol>
        <li><a href="#a-Methodology">Methodology</a></li>
        <li><a href="#b-Results">Results</a></li>
        <li><a href="#c-Discussion">Discussion</a></li>
      </ol>
    </li>
    <li>
      <a href="#Additional-Task-1---Adding-Check-Points">Additional Task 1 - Adding Check Points</a>
      <ol>
        <li><a href="#a-Methodology">Methodology</a></li>
        <li><a href="#b-Results">Results</a></li>
        <li><a href="#c-Discussion">Discussion</a></li>
      </ol>
    </li>
    <li>
      <a href="#Additional-Task-2---Path-Planning-for-Random-Scenarios">Additional Task 2 - Path Planning for Random Scenarios</a>
      <ol>
        <li><a href="#a-Methodology">Methodology</a></li>
        <li><a href="#b-Results">Results</a></li>
        <li><a href="#c-Discussion">Discussion</a></li>
      </ol>
    </li>
    <li>
      <a href="#Individual-Reflective-Essay">Individual Reflective Essays</a>
      <ol>
        <li><a href="#a-Member-1---Louise-Zhou-zhlouise">Louise Zhou</a></li>
        <li><a href="#b-Member-2---Rainy-Yuen-itsssraining">Rainy Yuen</a></li>
        <li><a href="#c-Member-3---Anson-Wong-Ansonwong88">Anson Wong</a></li>
        <li><a href="#d-Member-4---Samuel-Yau-SamuelYcy">Samuel Yau</a></li>
        <li><a href="#e-Member-5---Aidan-Yau-yhpAidan">Aidan Yau</a></li>
        <li><a href="#f-Member-6---Angela-Xu-Angelaxu2019">Angela Xu</a></li>
        <li><a href="#g-Member-7---Mark-Yao-Markyaoxin">Mark Yao</a></li>
        <li><a href="#h-Member-8---Haoyang-Yu-YU-Haoyang22101598d">Haoyang Yu</a></li>
      </ol>
    </li>
    <li><a href="#References">References</a></li>
    <li><a href="#Conclusion">Conclusion</a></li>
  </ol>
 </details>


<!--Background of Path Planning to Aviation Engineering-->

## Background of Path Planning to Aviation Engineering

Path planning is a computational problem to find the most suitable path that consider to move the object from the starting point to the destination to pass through all obstacles or some cost intensive area. Pilots should do the path planning before their flight to make sure the navigation aid is available. The correct fuel calculation can be calculated by the path-planning system and save the costs by calculating the msot suitable route and the best altitude to fly. In the aviation engineering, path planning can obtain the most suitable path in the flight and avoid the midair accident.


<!--Theory of Path Planning Algorithm-->

## Theory of Path Planning Algorithm


<!--Introduction of the Engineering Tools-->

## Introduction of the Engineering Tools

### a. Python

Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of their features support functional programming and aspect-oriented programming. Python is intended to be an easy-to-read language. It is visually neatly formatted and often uses English keywords whereas other languages use punctuation. This can be beneficial for beginners like us. Python has several versions, and our group used Python 3 for coding.

### b. Github

GitHub is an Internet hosting service for software development and version control using Git which is a version control system. GitHub can be a platform that helps people solve problems by building software together. Projects on GitHub.com can be accessed and managed using the standard Git command-line interface; all standard Git commands work with it. In GitHub, the users can create their own branches and if they want to modify others’ code them can create a pull request for the others to view and to merge it into the main branch. Our team used GitHub for cooperation.

<!--Compulsory Task 1 - Best Aircraft for the Given Scenarios-->

## Compulsory Task 1 - Best Aircraft for the Given Scenarios

In this task, we were given a unique set of obstacles, starting and goal points, and cost intensive areas. We were then asked to find the most optimal aircraft model among A321neo, A330-900neo, and A350-900 that would yield in the mimimum cost for each of the three given scenarios. A starting template for the A* algorithm was given. 

The below image illustrates the obstacles and cost intensive areas' setup assigned to our group:
<img width="700" alt="Screenshot 2022-11-26 at 10 18 36 PM" src="https://user-images.githubusercontent.com/116058486/204093387-58818aaf-c20f-4fd5-a36e-056c5fd3d261.png">

The below table summarizes the 3 given scenarios studied in this task:
|                       |Scenario 1|Scenario 2|Scenario 3|
|-----------------------|----------|----------|----------|
|Passenger per week     |3000      |1250/4    |2500      |
|Maximum flight per week|12        |5         |25        |
|Time cost              |medium    |high      |low       |
|Fuel Cost (in$/kg)     |0.76      |0.88      |0.95      |

Lastly, the below image shows the cost specifications for A321neo, A330-900neo, and A350-900:
<img width="591" alt="Screenshot 2022-11-26 at 6 31 19 PM" src="https://user-images.githubusercontent.com/116058486/204084260-55c49d91-66f4-43e5-9fef-d407889f5a3f.png">

### a. Methodology

We began our coding solution to this task by first setting up the obstacles and cost intensive areas assigned to our group. This could be easily done in ```main()``` though the ```append()``` function, which adds a continuous series of x or y coordinates into their respective list. We also modified the coordinates of the starting position and the ending position, sx, sy, gx, and gy, respectively. 

We then proceeded to writing the helper function ```trip_cost(passengers, weeks, max_flight, time_cost, fuel_cost)```. This function takes the total amount of passengers, the numbers of weeks to complete carrying the passengers, the maximum number of flights allowed, the time related cost per minute, and the fuel consumption rate as the input parameters. This function would return out a printed statement specifiying which aircraft would yield the minimum cost, the minimum cost itself, as well as how many flights of that aircraft is needed. 

The first thing we wanted to make sure in our function is that, out of the three aircrafts to choose from, we could only choose the ones that has the capacity to satisfy the amount of passengers specified in the scenario. This could be done though comparing the amount of flights we needed (to satisfy the passenger demands) with the actual amount of flights that we are allowed to have. Note that we used the ceiling division finding the amount of needed flights: ```math.ceil(passengers/capacity)```. This is because the ceiling function rounds the quotient to the larger interger, which makes sense because the 'remainder' of the passengers still needs another flight.

After eliminating the aircraft that will not fulfill the specified capacity, we could calculate the trip cost for the entire scenario by multiplying the cost for each flight with the number of flights needed (which we just calculated in the previous step). 
The cost for each flight could be found by the equation C = C<sub>F</sub> * ΔF * T<sub>best</sub> +  C<sub>T</sub> * T<sub>best</sub> + C<sub>C</sub>, where:
<ul>
  <li>C<sub>F</sub> is the cost of fuel per kilogram in $/kg</li>
  <li>ΔF is the fuel consumption rate in kg/min</li>
  <li>T<sub>best</sub> is the shortest trip time calculated by the algorithm in min</li>
  <li>C<sub>T</sub> is time related cost per minute of flight in $/kg</li>
  <li>C<sub>C</sub> is the fixed cost independent of time in $</li>
</ul>

Lastly, we would like to compare, out of the aircrafts that could fulfill the specified capacity, which one of them would yield in the minimum cost. This is done though storing all the possible outcomes into the ```comparasion_array```, then by using the Python builtin function ```comparasion_array.min()```, we could find the minimum possible cost for this scenario, which would lead us to the type of aircraft that yields this minimum cost. 

The final step involves using and calling this function in ```main()```so that it could be executed: 
```
# Finding the optimal flight for scenario 1
print ("Scenario 1:")
trip_cost (3000, 1, 12, "medium", 0.76)

# Finding the optimal flight for scenario 2
print ("Scenario 2:")
trip_cost(1250, 4, 5, "high", 0.88)

# Finding the optimal flight for scenario 3
print ("Scenario 3:")
trip_cost(2500, 1, 25, "low", 0.95)
 ```

### b. Results

With the previous steps executed, we were able to yield the results of this task as the following:
```
Total Trip time required ->  59.89528855298852
Task 1 Results:
Scenario 1:
The A321neo aircraft could not fulfill the specified capacity.
The trip cost for using 10 flights of A330 is $70815.16
The trip cost for using 9 flights of A350 is $73926.09
10 flights of A330 will yield the lowest cost of $70815.16
Scenario 2:
The trip cost for using 7 flights of A321 is $40908.91
The trip cost for using 5 flights of A330 is $40223.16
The trip cost for using 4 flights of A350 is $37120.59
4 flights of A350 will yield the lowest cost of $37120.59
Scenario 3:
The trip cost for using 13 flights of A321 is $71130.56
The trip cost for using 9 flights of A330 is $69102.66
The trip cost for using 8 flights of A350 is $70551.62
9 flights of A330 will yield the lowest cost of $69102.66
```
Please note that the results above are copied from the results printed in the terminal after executing ```main.py```. 


<!--Compulsory Task 2 - Designing Jet Stream Area-->

## Compulsory Task 2 - Designing Jet Stream Area

Jet streams are certain areas where aircrafts could consume less fuel, thus reducing the operational cost of that flight. In this task, we were asked to find the most optimal position of a jet steam using Scenario 1 from Task 1 as the background. The jet stream area spans across the map laterally and is 5 units in width (vertically). 

### a. Methodology

#### a1. Methodology for Trial Calculation

The following work is divided into three main parts:

<ins>First part: Define cost reduction of the jet stream area</ins>

We have the Delta C1 and C2 preliminary for the cost intensive area 1 and 2 respectively. Copy and modify the value to -0.05 to reduce the cost of 5% along the jet stream.

```
self.Delta_C1 = 0.2 # cost intensive area 1 modifier
self.Delta_C2 = 0.4 # cost intensive area 2 modifier
self.Delta_C3 = -0.05 # jet stream area 3 modifier
```

<ins>Second part: Define color of the jet stream area</ins>

Appreciate the code “oy” and “or”. That is for the color of the cost intensive area or jet stream area. Modify the code to “ob” in which the area will become blue in color.

```
plt.plot(fc_x, fc_y, "oy") # plot the cost intensive area 1
plt.plot(tc_x, tc_y, "or") # plot the cost intensive area 2
plt.plot(jc_x, jc_y, "ob") # plot the jet stream area 3
```

<ins>Third part: Define area of the jet stream area</ins>

Copy and modify the value from the cost intensive area 1 and 2. Modify it to the Delta_C3 that we have just defined which suits for the jet stream are cost reduction. Run the program by trial, record the total trip time required for every possible area position. Obtain the result by comparing the result and state the minimal total trip time.

```
# Set cost intesive area 1 (time-consuming area)
tc_x, tc_y = [], []
for i in range(20, 30):
    for j in range(30, 40):
        tc_x.append(i)
        tc_y.append(j)
    
# Set cost intesive area 2 (fuel-consuming area)
fc_x, fc_y = [], []
for i in range(10, 30):
    for j in range(50, 60):
        fc_x.append(i)
        fc_y.append(j)
        
# Set jet stream area 3 (fuel-conserving area)
jc_x, jc_y = [], []
for i in range(-10, 60):
    for j in range(26, 31):
        jc_x.append(i)
        jc_y.append(j)       
```

#### a2. Methodology for Program Calculation

For this task, we wrote a function named ```jet_stream(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y, sx, sy, gx, gy)```. This function involves calculating the total trip time ```current.cost``` for every single possible configurations of the jet steam area in the map. We could simply achieve that through using a for loop, setting the jet stream area to be a new one in each iteration: 

```
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
```
Note that we ran each iteration in an alternative function ```a_star.planning_no_animation(sx, sy, gx, gy)``` that does not plot animations to reduce the time it takes for the program to run.

Then, we are to compare all the different resulting costs. We created an empty dictionary that was used to store all the resulting ```current.cost``` values for each iteration. The keys of the dictionary are the lower bounds of the jet stream area while the values corresponding to each key is the cost that specific jet stream yields. Lastly, we use the Python built-in function ```min()``` to find the lower bound of the best jet stream ```ymin```and deduce the value of the upper bound ```ymax```as well. 

```
# Create an empty dictionary that will be used to store all the possible costs for each iteration runned.
comparasion_dict = {}
......
# Finding the key (ymin) for the minimum cost within the comparasion dictionary
ymin = min(comparasion_dict.keys(), key=(lambda k: comparasion_dict[k]))
ymax = ymin + 5
```
With the information we obtained about the most optimal jet stream position, we could finally set the actual jet stream of the program: 
```
jc_x, jc_y = [], []
for i in range(-10, 60):
    for j in range(ymin, ymax):
        jc_x.append(i)
        jc_y.append(j)
```

### b. Results

Both methods that we used indicated that the best jet stream area is between 27 and 32 on the vertical axis: 
```
Task 2 Results:
The optimal jet-stream ranges from y=27 to y=32.
```
Please note that the results above are copied from the results printed in the terminal after executing ```main.py```.

The plotted result that the program returns is as illustrated below, where the area shaded in blue is the most optimal jet stream area.

<img width="415" alt="image" src="https://user-images.githubusercontent.com/116557675/201847987-d9232159-e366-4174-8a56-2812dc983b81.png">

### c. Discussion

<ins>Comparison between two methods</ins>

For the trial calculation, we need to have each scenario tested manually, which indicates that the efficiency of completing the task is lower. However, the result of the task can be predicted based on experience. For example, there will be no difference of the result when the jet stream area location is already exceeded j (40, 45). It is apparent that the result is not altered by the jet stream area because the shortest routes are not included in that area. This can improve the efficiency of using man calculation by trial. However, designing a code can prevent human error and improve the efficiency.

For the program calculation, some levels of coding knowledge is required. In addition, the method of running through every possible iteration means that the program would have a relatively longer execution time. In our case, the execution time is around 50 seconds. The run-time could be improved if we have some advanced knowledge of optimizing a programe. Nevertheless, it prevents the use of human calculation and hence minimizes the risk of human error. All in all, program calculation is still preferable if there is a programmer who is confident in coding.


<!--Compulsory Task3 - Designing an Aircraft-->

## Compulsory Task 3 - Designing an Aircraft

In this task, we were asked to design an aircraft that is most suitable for the Scenario 1, provided in Task 1. Some factors to be considered are the passenger capacity of the aircraft, as well as the number of engines on the aircraft. 

Restrictions are given that:
<ul>
  <li>The aircraft could have a minimum capacity of 100 passengers and a maximum capacity of 450 passengers. </li>
  <li>The base time related cost per minute of flight is 12$/min. However, for every 50 passengers, the time related cost is increased by 2$/min.</li>
  <li>The base design is a twin-engine aircraft. However, if the passenger capacity exceeds 300 (inclusive), we must switch to a 4-engined aircraft. </li>
    <ul>
      <li>The fixed cost for a twin-engine aircraft is $2000 while the fixed cost for a 4-engine aircraft is $2500.</li>
      <li>Each engine consumes fuel at a rate of 20 kg/min. </li> 
    </ul>
  <li>The cost of fuel is $882.30 per metric tonnes.</li>
</ul>

### a. Methodology

To tackle this task, we first defined 2 helper functions in our code: ```aircraft_cost(capacity)``` and ```optimal_cost()```.

<ins>```aircraft_cost(capacity)```</ins>
This function takes in the capacity of the aircraft as an input parameter and returns the cost per flight. 

Before we start the calculation process for the cost, we first wanted to know how many engines the aircraft has. This could be done using a simple if-else statement; if the capacity is lower than 300, return the parameters (fixed cost and fuel consumption rate) for a twin-engine aircraft, else return those for a 4-engine aircraft:
```
 # To determine the fixed cost per flight and the total rate of fuel consumption of all engines (whether the plane has 2 engines or 4 engines), depending on the aircraft's capacity.
if capacity >= 300:
    Cc = 2500
    delta_F = 20*4
else:
    Cc = 2000
    delta_F = 20*2
```
Then we converted the cost of fuel into units of $ per kilogram through dividing 882.30 by 1000. 

Next, based on the aircraft's passenger capacity, we could calculate the time related cost per minute of flight. Note that the ```math.floor()``` function is used here to round the numbers of groups of 50 passengers to the lower number (eg. if there are 70 passengers, we only increase CT by one $2, since we only increase CT for every 50 passengers).
```
 CT = 12 + math.floor(capacity/50)*2  # CT is the time related cost per minute of flight (base CT = $12/min, for every 50 passengers increase CT by $2)
```

With all the parameters for calculating the cost obtained, we could finally calculate the trip cost by simply plugging all the parameters into the cost equation C = C<sub>F</sub> * ΔF * T<sub>best</sub> +  C<sub>T</sub> * T<sub>best</sub> + C<sub>C</sub>. (Note that T<sub>best</sub> is ```current.cost```, the trip time calculated by the A* algorithm.)

<ins>```optimal_cost()```</ins>
This function runs through every possible capacity (100<=capacity<=450) and finds out the minimum cost, which in turn would lead us to the most optimal capacity.

We first started off by setting a cost for the resulting calculated cost to compare with. Then, we proceeded to setting a for loop that runs through all the possible capacities. Inside the for loop, we first decided whether the specified aircraft capacity would fulfill the amount of passengers as required in Scenario 1. If not, we would skip the iteration for this specific capacity. However, if the capacity in this iteration meets the passenger requirement, we would proceed to calculate the flight cost and compare this newly obtained flight cost to the cost stored as the ```cost``` variable. If this new cost is lower than the stored cost, we would store this new cost as into the ```cost``` variable instead. If not, the for loop proceeds into the next iteration of calcuation for a new capacity.

```
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
```

As a result, the optimal capacity and the optimal cost is stored into the ```capacity``` and ```cost``` variables, respectively. 

### b. Results
```
Task 3 Results:
The optimal passenger capacity for scenario 1 is 250. There are 2 engines on the aircraft. This yields in a minimal operating cost of $5431.52 per flight. 
```
Please note that the results above are copied from the results printed in the terminal after executing ```main.py```.



### c. Discussion


<!--Additional Task 1 - Adding Check Points-->

## Additional Task 1 - Adding Check Points

### a. Methodology

### b. Results

## Additional Task-2 - Path Planning for Random Scenarios

### a. Methodology

## b. Results


## Individual Reflective Essay

### a. Member 1 - Louise Zhou (zhlouise)

If someone were to ask me about path planning in aviation before this course, I would possibly picture a sophisticated map and procedures too complicated to understand for someone who just graduated high school months ago. In fact, at the beginning of this project, I indeed saw it as a tremendous challenge, given the fact that I was brand new to both Python and coding algorithms. However, with the given example code and some introductory lectures, I was able to understand the fundamental concepts of computer algorithms. In short and simple language, an algorithm is equivalent to asking the program to do all the work too tedious for a human to complete. The program could run through all the possible paths given the object's position at the instant, which yields some kind of estimation on the time cost, which is then used to decide where the object would go next. (In my opinion, it is somewhat logically similar to the principle of least action in Lagrangian mechanics.) Calculating with computer programs is critical because it is the only efficient way to perform complex calculations quickly and accurately, especially given that our path planning scenarios are only overly simplified versions of real-life scenarios. Being able to use computer algorithms at our convenience also has implications beyond path planning. For example, we could utilize regression algorithms to find the most suitable curve for modeling the flow of a fluid or to predict stock market trends. In addition to learning about the importance of coding algorithms, we were also introduced to the collaborative programming platform, GitHub. We were able to learn how to collaborate efficiently with other programmers while taking advantage of the platform ourselves. I was amazed by the fact that there are many open-sourced codes for us to discover and modify to satisfy our own requirements. Moreover, writing some parts of the README file helped me revisit some basic HTML knowledge. All in all, this project provided me with new insights into computer algorithms as well as collaborative programming. They will undoubtedly be useful in the future not only for performing complex calculations but also for bringing potential ideas to life.

### b. Member 2 - Rainy Yuen (itsssraining)

### c. Member 3 - Anson Wong (Ansonwong88)

The python system and Githib is totally Greek to me as a student that is majoring in radiotherapy. As such, this is a fresh and new task as an amateur to try the power of coding and the A star algorithm. When I first get touch with the python system, it is very difficult for me to learn the coding language as they share different language system among different programs. Therefore, I can only do modification from the sample code with the aids of those small explanation aside in the code. It is a new experience for me to understand the code, not to mention to create new codes. I had a hard time struggling with the coding part. However, after inspired by those lecture and introduction, I know that it is important for an engineering student to learn coding as this is highly related to their future career. 

I have learnt how to apply the program in aviation and the rationale behind. To integrate the knowledge that I have learnt in aviation study, I appreciate the decision-making process behind when the airline is designing airline route. For example, how the jet stream area will alter the cost and efficiency of that route. This is all based on the systematic protocol and calculation to obtain the conclusion. All in all, this project had broadened my horizon on the aviation industry and will be a remarkable point in my minor study. 

### d. Member 4 - Samuel Yau (SamuelYcy)

### e. Member 5 - Aidan Yau (yhpAidan)

Although I have learnt the python coding in other subjects like the the Foundamentals of AI and Data Analysis, but this coding part and A star algorithm in this course is totally new to me and also difficult to me. In this project, I have tried to do and successfully finished the compulsary task 1 but task 2 and 3 is really hard for me. Fortunately, my groupmates have a stronger coding skill and they have finished all the compulsary task so my job is to do the read.me section. This path planning course really built a foundation in my aviation knowledge. If I had a chance to do this project again, I would learn the coding part more deeply and try to understand all the function of the code like A star algorithm. In conclusion, this github course helps me a lot as a first project in my university life.

### f. Member 6 - Angela Xu (Angelaxu2019)

As a person who is totally new to programming, I have never learn any coding befor entering the university. When I first know that we need to do this project, I thought it is nearly impossible for me, since I have only learnd basic Python programming in my IC training course, while the required tasks assigned in this project are much diificult than that. Due to limited capability, I did not do much coding in the project, but I have still learn a lot from the project. I have know the theory of path fligh path planing, which I thought it is designed only based on the time consumed. After start doing the project, I have a chance to know that to plan a path, there are depending facts to consider when desigh a flight, including cost intensify area, time slot of the flight, and even the type of aircraft used. By doing this project, although it is quite a challenge for me, it can still help me to become more familiar to coding, and how to coorporate with others to finish a project together, which is a great receipt for me.

### g. Member 7 - Mark Yao (Markyaoxin)

### h. Member 8 - Haoyang Yu (YU-Haoyang22101598d)

In this course, we have learnt about the A star algorithm of path planning and done some tasks by using it. Since I have not done any coding projects, everything seems unfamiliar to me. After reading the explanation after some code, I began to understand that we should change some parameters and modify some parts of the original code while keeping the logic of the code to be clear instead of writing the whole code. During coding, I have encountered many errors and I don’t know how to solve them. Thanks to my groupmates and the teachers, I was able to figure them out in the end. This let me realize the importance of cooperation.
In the course, I also got familiar with tools for coding such as GitHub. GitHub can not only be a resource library for programmers but also provide an online platform for programmers to cooperate. It can be a useful tool to do a coding project.
All in all, this course gives me insights into the path planning of fights and practice my skills of working as a team.


## Conclusion

## References
