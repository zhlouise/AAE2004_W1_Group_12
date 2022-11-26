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
    <li><a href="#Conclusion">Conclusion</a></li>
  </ol>
 </details>


<!--Background of Path Planning to Aviation Engineering-->

## Background of Path Planning to Aviation Engineering


<!--Theory of Path Planning Algorithm-->

## Theory of Path Planning Algorithm


<!--Introduction of the Engineering Tools-->

## Introduction of the Engineering Tools

### a. Python

### b. Github


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

<img width="360" alt="image" src="https://user-images.githubusercontent.com/116557675/201845433-be4c61f9-fc67-437a-af46-155a68f4a580.png">

### a2. Methodology for program calculation

Program calculation involve the use of the iteration calculation to obtain the minimal total trip time (minimal cost). First, create an empty dictionary that will be used to store all the possible costs for each iteration run. Run and repeat all the possible place of jet stream area inside the box by defining j in range from k to k+5, which +5 is defining the 5-unit length vertically. Run the A star algorithm without plotting the animations to preserve time. When one calculation for one position is done, store inside the comparison dictionary and loop for the second location of jet stream area.

<img width="415" alt="image" src="https://user-images.githubusercontent.com/116557675/201846212-2da215ae-f6a9-44aa-afb1-8681bd6aec1f.png">

After running through all the possible location of the jet stream area, calculation is done. Extract the minimum total trip time from the comparison dictionary. Set it as the jet stream area and shown in the animation.

<img width="415" alt="image" src="https://user-images.githubusercontent.com/116557675/201846271-9b37bb08-4886-4765-ad36-10436fd59810.png">

Result shown in this format 

<img width="415" alt="image" src="https://user-images.githubusercontent.com/116557675/201846326-57d94b51-5059-4ec5-9141-bbdd5c38dcd5.png">

### b. Results

<img width="415" alt="image" src="https://user-images.githubusercontent.com/116557675/201847987-d9232159-e366-4174-8a56-2812dc983b81.png">

<img width="344" alt="image" src="https://user-images.githubusercontent.com/116557675/201848029-bf6b65ca-305f-4b0b-91e1-1869be1796eb.png">


### c. Discussion

**Comparison between two methods**

For the trial calculation, the programmer needs to have each scenario tested, which the efficiency of completing the task is lower. However, the result of the task can be predicted based on the experience. For example, there will be no difference of the result when the jet stream area location is already exceeded j (40, 45). It is apparent that the result is not altered by the jet stream area because the shortest routes are not included in that area. This can improve the efficiency of using man calculation by trial. However, designing a code prevent human error and improve the efficiency.

For the program calculation, a higher level of code standard is required. The knowledge of iteration and comparison dictionary is used in the code. Nevertheless, it prevents the use of human calculation and hence reduce the risk of human error. All in all, program calculation is still preferable if there is a programmer who is confident in coding. 


<!--Compulsory Task3 - Designing an Aircraft-->

## Compulsory Task 3 - Designing an Aircraft

### a. Methodology

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


## Conclusion

## References
