<div id="banner" align="left">
  <img src="https://im3.ezgif.com/tmp/ezgif-3-a060d74a4c.gif" width=100% height=auto object-fit=cover/>
</div>

<div id="header" align="center">
  <h1>PROJECT REPORT - GROUP 12</h1>
  <p>Members: Louise Zhou (zhlouise), Rainy Yuen (itsssraining), Anson Wong (Ansonwong88), Samuel Yau (SamuelYcy), Aidan Yau (yhpAidan), Angela Xu (Angelaxu2019), Mark Yao (Markyaoxin), Haoyang Yu (YU-Haoyang22101598d)<p>
</div>

# Presentation Link

<!-- Table of Content-->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <li><a href="#Background-of-Path-Planning-to-Aviation-Engineering">Background of Path Planning to Aviation Engineering</a></li>
  <li><a href="#Theory-of-Path-Planning-Algorithm">Theory of Path Planning Algorithm</a></li>
  <li><a href="#Introduction-of-the-Engineering-Tools">Introduction of the Engineering Tools</a></li>
  <li><a href="#Compulsory Task-1 - Scenarios">Compulsory Task 1 - Scenarios</a></li>
  <li><a href="#Compulsory Task-2 - Designing New Cost Area">Compulsory Task 2 - Designing New Cost Area</a></li>
  <li><a href="#Compulsory Task-3 - Designing an Aircraft">Compulsory Task 3 - Designing an Aircraft</a></li>
  <li><a href="#Additional Task-2 - Adding Check Points">Additional Task 1 - Adding Check Points</a></li>
  <li><a href="#Individual Reflective-Essay">Individual Reflective Essays</a></li>
  <li><a href="#References">References</a></li>
 </details>
    
               

<img width="1006" alt="Screenshot 2022-11-15 at 2 19 44 PM" src="https://user-images.githubusercontent.com/116058486/201841746-86859c4e-b873-46a7-b711-25906b196144.png">




<!--Background of Path Planning to Aviation Engineering-->

## Background of Path Planning to Aviation Engineering








<!--Theory of Path Planning Algorithm-->

## Theory of Path Planning Algorithm





<!--Introduction of the Engineering Tools-->

## Introduction of the Engineering Tools

### a. Python

### b. Github







<!--Task 1 - Scenarios-->

## Compulsory Task 1 - Scenarios

The below image show the current scenario for our group.

<img width="1216" alt="Screen Shot 2022-10-25 at 1 34 14 PM" src="https://user-images.githubusercontent.com/116058486/197690898-449eb429-0daa-49f4-b658-54dab5e9a91e.png">

**Scenario 1**
1. 3000 Passengers need to travel within this week from the start to the destination
2. 12 flights maximum for one week
3. Time cost = medium and Fuel cost = 0.76 $/kg

**Scenario 2**
1. 1250 Passengers need to travel within this month from the start to the destination
2. 5 flights maximum for one week
3. Time cost = high and Fuel cost = 0.88 $/kg

**Scenario 3**
1. 2500 Passengers need to travel within this week from the start to the destination
2. 25 flights maximum for one week
3. Time cost = low and Fuel cost = 0.95 $/kg

### a. Methodology



### b. Results

**The following show the result of different scenarios in Task1**

<img width="471" alt="Screen Shot 2022-10-31 at 10 49 42 PM" src="https://user-images.githubusercontent.com/116058486/199039639-1bf8a4bb-46f9-4548-9d44-f178ade9a0cf.png">




### c. Discussion






<!--Task 2 - Designing New Cost Area-->



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






<!--Task3 - Designing an Aircraft-->


## Compulsory Task 3 - Designing an Aircraft

### a. Methodology

### b. Results

**The following show the result of the most optimal aircraft in Task3**
<img width="921" alt="Screen Shot 2022-11-01 at 3 04 15 PM" src="https://user-images.githubusercontent.com/116058486/199177844-6e93ad22-82c4-416b-975f-d372184bb5e5.png">

Name for aircraft: 
Passenger capacity: 250
Engine count: 2

### c. Discussion










<!--Task 4 -->


## Additional Task 1 - Adding Check Points

### a. Methodology

### b. Results




## Individual Reflective Essay

### a. Member 1 - Louise Zhou (zhlouise)

### b. Member 2 - Rainy Yuen (itsssraining)

### c. Member 3 - Anson Wong (Ansonwong88)

The python system and Githib is totally Greek to me as a student that is majoring in radiotherapy. As such, this is a fresh and new task as an amateur to try the power of coding and the A star algorithm. When I first get touch with the python system, it is very difficult for me to learn the coding language as they share different language system among different programs. Therefore, I can only do modification from the sample code with the aids of those small explanation aside in the code. It is a new experience for me to understand the code, not to mention to create new codes. I had a hard time struggling with the coding part. However, after inspired by those lecture and introduction, I know that it is important for an engineering student to learn coding as this is highly related to their future career. 

I have learnt how to apply the program in aviation and the rationale behind. To integrate the knowledge that I have learnt in aviation study, I appreciate the decision-making process behind when the airline is designing airline route. For example, how the jet stream area will alter the cost and efficiency of that route. This is all based on the systematic protocol and calculation to obtain the conclusion. All in all, this project had broadened my horizon on the aviation industry and will be a remarkable point in my minor study. 

### d. Member 4 - Samuel Yau (SamuelYcy)

### e. Member 5 - Aidan Yau (yhpAidan)

### f. Member 6 - Angela Xu (Angelaxu2019)

### g. Member 7 - Mark Yao (Markyaoxin)

### h. Member 8 - YU Haoyang (YU-Haoyang22101598d)



## References
