# FridgeMon
"Reduce waste and take control of your fridge."

## Overview
This repository contains prototype software for FridgeMon, a smart refrigerator system that helps users keep track of food in their fridge, 
thereby reducing waste. This was my group's final project for our Fabrication and Prototyping class at the [Global Innovation Exchange](https://gixnetwork.org/) in Bellevue, Washington. 

<div>
<img src="https://user-images.githubusercontent.com/89954856/206879927-0f4b7fb6-23af-4b48-9c42-33371dc0baa8.png" height="300">
<br><sub>Yue Sun, Tim Huff & Anqi Pan at project bazaar</sub>
 </div>
 <br>

<div>
<img src="https://user-images.githubusercontent.com/89954856/206879927-0f4b7fb6-23af-4b48-9c42-33371dc0baa8.png" height="300">
<br><sub>FridgeMon Project Poster</sub>
 </div>

## Solution
Food containers are equipped with RFID tags that the smart fridge system can read. The user simply adds and removes containers, and the fridge automatically
knows which containers are in the fridge and how long they have been there. Each container has a unique animal design on top to help the user 
differentiate the containers. When a new container is added to the fridge, the user has the option to label the contents of that container on the touchscreen.

The touchscreen displays the contents of the fridge as well as how long each item has been in the fridge. Items are sorted oldest 
to newest to help users prioritize what to eat next.

## Process
#### Concept
In our initial sketches, we explored the placement of the touchscreen relative to the fridge. At first, we showed the screen positioned to the side of the fridge, because we imagined that users would scan items (perhaps with a camera) before placing them in the fridge. However, we quickly realized that manually scanning each item is a hassle, so we moved away from this idea. At this point, we began to explore RFID as a means for the system to automatically detect items. We like this idea because it is automatic; the only input required of the user is to label the item on the touchscreen, which we believe is reasonable. 

(Pictures of initial sketches)

#### Labeling Items
We realized a problem at this point: if the user adds many items to the fridge at once, how can they differentiate the unlabled boxes in order to label them? Until this point, we only considered the workflow for adding a single box, so we hand't considered the complications that arise when multiple boxes are added at once. To solve this, we decided to put unique animal designs on the top of each container, so that even prior to labeling the containers, the user has a way to know which box is which.

<div>
<img src="https://user-images.githubusercontent.com/89954856/206878615-717ee4a1-c4cd-42b5-b086-74c67e27e956.png" height="200">
<br><sub>Multiple unlabled boxes, differentiated with animal designs</sub>
 </div>


#### Obtaining a Fridge
As we started to think towards the final presentation of our prototype, we realized that demoing our system would be difficult without an actual fridge. Of course, we could show a video or demo the system in isolation, but neither of those options seemed great. We decided that showing our system on an actual fridge was a must-have. We went online and found a free (but broken) mini fridge. We didn' need the fridge to work, and we were operating under a budget, so this was perfect for us. It makes our prototype much more convincing. 

<div>
<img src="https://user-images.githubusercontent.com/89954856/206874532-958a3d4a-a37c-4cab-8523-d5ab563ab141.png" height="300">
<br><sub>Mini fridge, acquired online</sub>
</div>


#### Obtaining a Fridge
Now that the basic functionality of the system had been determined, we returned to the question of where to place the touchscreen. Instinctively, we moved it to the door of the fridge, but this presented a problem: the user would be unable to view the screen while the fridge was open. We debated the pros and cons of this for a while. On the hand, perhaps the user shouldn't be looking at the screen while the door is open; encouraging the user to look at the screen while the door is open might waste energy. On the other hand, perhaps users need to see what is on the screen while they are looking inside the fridge, and if they are unable to, this might result in frustration and repeated door opening. In the end, we decided to err on the side of giving the user more information, and 

## Software
* logic.py: contains the basic logic and tracks the state of the smart refrigerator system.
* main.py: produces the graphical user interface. Run this file to start the program.

## Hardware
* Raspberry Pi 4
* Raspberry Pi 7-inch touchscreen
* Button (for the refrigerator door)
* 3D-printed enclosures for the touchscreen and button
* RFID antenna
* RFID tags

## Team Members
* [Anqi Pan](https://www.linkedin.com/in/anqipan/): UI/UX design, 3D printing and laser cutting of food tags and containers
* [Yue Sun](https://www.linkedin.com/in/yuesun1003/): hardware sourcing & implementation (RFID)
* [Tim Huff](https://www.linkedin.com/in/tim-huff-60a05973/): software development, 3D printing of touchscreen enclosure


## Gallery
 <table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300"></td>
    <td><img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300"></td>
    <td><img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300"></td>
  </tr>
</table> 



<table>
  <tr>
    <td>
     <img src="https://user-images.githubusercontent.com/89954856/206879009-ba4da4e0-003e-4351-bfb1-fca19fe51f18.png" height="360">
     <br>
     <sub>Yue Sun, Tim Huff & Anqi Pan at GIX project bazaar</sub>
   </td>
    <td>
     <img src="https://user-images.githubusercontent.com/89954856/206879009-ba4da4e0-003e-4351-bfb1-fca19fe51f18.png" height="360">
     <br>
     <sub>FridgeMon project poster</sub>
   </td>
  </tr>
</table> 


<table>
  <tr>
    <td>
     <img src="https://user-images.githubusercontent.com/89954856/206879326-ac4f6859-0e07-41be-9bb1-bc72c847290c.png" height="300">
     <br>
     <sub>User Testing</sub>
   </td>
    <td>
     <img src="https://user-images.githubusercontent.com/89954856/206879345-5193f48d-fef9-4fc7-89ba-9f3c8b84a0ba.png" height="300">
     <br>
     <sub>Adding new item to the fridge</sub>
   </td>
   <td>
     <img src="https://user-images.githubusercontent.com/89954856/206879484-3355d0da-ddc3-4f2a-8556-a7ad2a43aff0.png" height="300">
     <br>
     <sub>Food container with FridgeMon tag</sub>
   </td>
  </tr>
</table> 

![](https://user-images.githubusercontent.com/89954856/206879927-0f4b7fb6-23af-4b48-9c42-33371dc0baa8.png)  |  ![](https://user-images.githubusercontent.com/89954856/206879927-0f4b7fb6-23af-4b48-9c42-33371dc0baa8.png)
:-------------------------:|:-------------------------:
Yue Sun, Tim Huff & Anqi Pan at project bazaar |  FridgeMon project poster

![](https://user-images.githubusercontent.com/89954856/206879326-ac4f6859-0e07-41be-9bb1-bc72c847290c.png)  |  ![](https://user-images.githubusercontent.com/89954856/206879345-5193f48d-fef9-4fc7-89ba-9f3c8b84a0ba.png)  |  ![](https://user-images.githubusercontent.com/89954856/206879484-3355d0da-ddc3-4f2a-8556-a7ad2a43aff0.png)
:-------------------------:|:-------------------------:|:-------------------------:
User Testing |  Adding new item to fridge |  Food container with FridgeMon tag
