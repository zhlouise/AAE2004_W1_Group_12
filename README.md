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
        <li><a href="#c-Discussion">Discussion</a></li>
      </ol>
    </li>
    <li>
      <a href="#Compulsory-Task-2---Designing-New-Cost-Area">Compulsory Task 2 - Designing New Cost Area</a>
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
      <a href="#Additional-Task-2---Path-Planning-for-Random-Scenarios"></a>
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
  </ol>
 </details>


<!--Background of Path Planning to Aviation Engineering-->

## Background of Path Planning to Aviation Engineering

Path planning is a computational problem to find the most suitable path that consider to move the object from the starting point to the destination to pass through all obstacles or some cost intensive area. Pilots should do the path planning before their flight to make sure the navigation aid is available. In decades, some airplane accident happened around the world. Path planning can calculate the most suitable route for the flight to increase the safety, also the efficiency of the flight, not to mention to assign the appropriate costs to each segment. In particular, a common objective considered is to minimize the aircraft fuel consumption. In the aviation engineering, the most suitable path in the flight can be obtained by the path-planning system and avoid the midair accident by taking the consideration of the effect of bad weather situations.

<!--Theory of Path Planning Algorithm-->

## Theory of Path Planning Algorithm


<!--Introduction of the Engineering Tools-->

## Introduction of the Engineering Tools

### a. Python

### b. Github


<!--Compulsory Task 1 - Best Aircraft for the Given Scenarios-->

## Compulsory Task 1 - Best Aircraft for the Given Scenarios

In this task, we were given a unique set of obstacles, starting and goal points, and cost intensive areas. We were then asked to find the most optimal aircraft model among A321neo, A330-900neo, and A350-900 that would yield in the mimimum cost for each of the three given scenarios.

The below image shows the obstacle and cost intensive areas' setup assigned to our group:
<img width="700" alt="Screen Shot 2022-10-25 at 1 34 14 PM" src="https://user-images.githubusercontent.com/116058486/197690898-449eb429-0daa-49f4-b658-54dab5e9a91e.png">

The below table shows the 3 scenarios used for calculation:
|                       |Scenario 1|Scenario 2|Scenario 3|
|-----------------------|----------|----------|----------|
|Passenger per week     |3000      |1250/4    |2500      |
|Maximum flight per week|12        |5         |25        |
|Time cost              |medium    |high      |low       |
|Fuel Cost (in$/kg)     |0.76      |0.88      |0.95      |

Lastly, the below image shows the cost specifications for A321neo, A330-900neo, and A350-900:
<img width="591" alt="Screenshot 2022-11-26 at 6 31 19 PM" src="https://user-images.githubusercontent.com/116058486/204084260-55c49d91-66f4-43e5-9fef-d407889f5a3f.png">



### a. Methodology

The cost for each flight could be found by the equation C = C<sub>F</sub> * ΔF * T<sub>best</sub> +  C<sub>T</sub> * T<sub>best</sub> + C<sub>C</sub>, where:
<ul>
  <li>C<sub>F</sub> is the cost of fuel per kilogram in $/kg</li>
  <li>ΔF is the fuel consumption rate in kg/min</li>
  <li>T<sub>best</sub> is the shortest trip time calculated by the algorithm in min</li>
  <li>C<sub>T</sub> is time related cost per minute of flight in $/kg</li>
  <li>C<sub>C</sub> is the fixed cost independent of time in $</li>
</ul>

We begin our coding solution to this task by first writing the helper function ```trip_cost(passengers, weeks, max_flight, time_cost, fuel_cost)```. This function takes the total amount of passengers, the numbers of weeks to complete carrying the passengers, the maximum number of flights allowed, the time related cost per minute, and the fuel consumption rate as the input parameters. 


### b. Results

**The following show the result of different scenarios in Task1**

<img width="471" alt="Screen Shot 2022-10-31 at 10 49 42 PM" src="https://user-images.githubusercontent.com/116058486/199039639-1bf8a4bb-46f9-4548-9d44-f178ade9a0cf.png">


### c. Discussion


<!--Compulsory Task 2 - Designing New Cost Area-->

## Compulsory Task 2 - Designing New Cost Area

### a1. Methodology for trial calculation

**The following work is divided into three main parts**

**First part: Define cost reduction of the jet stream area**

We have the Delta C1 and C2 preliminary for the cost intensive area 1 and 2 respectively. Copy and modify the value to -0.05 to reduce the cost of 5% along the jet stream.

<img width="387" alt="image" src="https://user-images.githubusercontent.com/116557675/201845315-eb36dd45-50f0-41ab-a662-95bfc77997f2.png">

**Second part: Define color of the jet stream area**

Appreciate the code “oy” and “or”. That is for the color of the cost intensive area or jet stream area. Modify the code to “ob” in which the area will become blue in color.

<img width="415" alt="image" src="https://user-images.githubusercontent.com/116557675/201845375-f606be1c-a78d-4e5a-b026-3adbb6517652.png">

**Third part: Define area of the jet stream area**

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


### b. Results



**The following show the result of the most optimal aircraft in Task3**
<img width="921" alt="Screen Shot 2022-11-01 at 3 04 15 PM" src="https://user-images.githubusercontent.com/116058486/199177844-6e93ad22-82c4-416b-975f-d372184bb5e5.png">

Name for aircraft: 
Passenger capacity: 250
Engine count: 2

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

### g. Member 7 - Mark Yao (Markyaoxin)

### h. Member 8 - Haoyang Yu (YU-Haoyang22101598d)

In this course, we have learnt about the A star algorithm of path planning and done some tasks by using it. Since I have not done any coding projects, everything seems unfamiliar to me. After reading the explanation after some code, I began to understand that we should change some parameters and modify some parts of the original code while keeping the logic of the code to be clear instead of writing the whole code. During coding, I have encountered many errors and I don’t know how to solve them. Thanks to my groupmates and the teachers, I was able to figure them out in the end. This let me realize the importance of cooperation.
In the course, I also got familiar with tools for coding such as GitHub. GitHub can not only be a resource library for programmers but also provide an online platform for programmers to cooperate. It can be a useful tool to do a coding project.
All in all, this course gives me insights into the path planning of fights and practice my skills of working as a team.



## References
