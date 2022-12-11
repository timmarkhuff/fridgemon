# FridgeMon

## Overview
FridgeMon is a smart refrigerator system that helps users keep track of food in their fridge, 
thereby reducing waste. This was my group's final project for our Fabrication and Prototyping class at the [Global Innovation Exchange](https://gixnetwork.org/) in Bellevue, Washington. 

<img src="https://user-images.githubusercontent.com/89954856/206921636-751f83c7-815f-4f66-b62d-9b027a2bc186.png" width="350">
 
## Solution
Food containers are equipped with RFID tags that the smart fridge system can read. The user simply adds and removes containers, and the fridge automatically
detects which containers are in the fridge and how long they have been there. Each container has a unique animal design to help the user 
differentiate them. When a new container is added to the fridge, the user has the option to label the contents on the touchscreen.

The touchscreen displays the items in the fridge as well as how long each item has been inside. Items are sorted oldest 
to newest to help users prioritize what to eat next.
 
<div>
<img src="https://user-images.githubusercontent.com/89954856/206922015-09dad921-9f67-4302-9d2c-0a77b1e751f1.png" width="350">
<br><sub>FridgeMon workflow</sub>
 </div>

## Process
#### Concept
In our initial sketches, we explored the placement of the touchscreen relative to the fridge. At first, we showed the screen positioned to the side of the fridge, because we imagined that users would scan items (perhaps with a camera) before placing them in the fridge. However, we quickly realized that manually scanning each item is a hassle, so we moved away from this idea. At this point, we began to explore RFID as a means for the system to automatically detect items. We like this idea because it is automatic; the only input required of the user is to label the item on the touchscreen, which we believe is reasonable. 

<div>
<img src="https://user-images.githubusercontent.com/89954856/206921372-982a620f-bf7c-4fb3-8c1b-4c51ceb37257.png" width="350">
<br><sub>Concept sketches</sub>
 </div>

#### Labeling Items
We realized a problem at this point: if the user adds many items to the fridge at once, how can they differentiate the unlabeled boxes in order to label them? Until this point, we only considered the workflow for adding a single box and had no way of dealing with the complications that arise when multiple boxes are added at once. To solve this, we put unique animal designs on the top of each container, so that even prior to labeling the containers, the user has a way to know which box is which.

<div>
<img src="https://user-images.githubusercontent.com/89954856/206878615-717ee4a1-c4cd-42b5-b086-74c67e27e956.png" width="350">
<br><sub>Multiple unlabeled boxes, differentiated with animal designs</sub>
 </div>


#### Obtaining a Fridge
As we started to think towards the final presentation of our prototype, we realized that demoing our system would be difficult without an actual fridge. Of course, we could show a video or demo the system in isolation, but neither of those options seemed great. We decided that showing our system on an actual fridge was a must-have. We went online and found a free (but broken) mini fridge. We didn't need the fridge to work, and we were operating on a budget, so this was perfect for us. It makes our prototype much more convincing. 

<div>
<img src="https://user-images.githubusercontent.com/89954856/206874532-958a3d4a-a37c-4cab-8523-d5ab563ab141.png" width="350">
<br><sub>Mini fridge, acquired online</sub>
</div>

#### Protyping the Touchscreen Enclosure
Now that the basic functionality of the system had been determined, we returned to the question of where to place the touchscreen. Instinctively, we moved it to the door of the fridge, but this presented a problem: the user would be unable to view the screen while the fridge was open. We debated the pros and cons of this for a while. On one hand, perhaps the user shouldn't be looking at the screen while the door is open; this wastes electricity. On the other hand, perhaps users need to see what is on the screen while they are looking inside the fridge, and if they are unable, this might result in frustration and repeated door opening. In the end, we decided to err on the side of giving the user more information, and we and mounted the screen above the door. In the context of our mini fridge, this means putting the screen on top of the fridge, but in a full-sized fridge, this might mean putting it on the freezer door. 

We built the first screen prototypes out of cardboard in order to quickly explore different configurations. We chose to use a Raspberry Pi Touchscreen for our project, so all of the enclosures were built to fit that. After a few iterations of the cardboard prototypes, we had arrived at a concept that we liked. 

<div>
<img src="https://user-images.githubusercontent.com/89954856/206880983-11837cc1-5734-436c-8528-9c2e7cf51bca.png" width="350">
<br><sub>Early prototype of screen</sub>
</div>

#### 3D Printing the Enclosure
When it came time to 3D print the touchscreen enclosure, we realized we had to make a few modifications to our design. First, our design was too large to fit on the Ultimaker printer bed in the orientation we wanted. We simplied the design a bit so that it was no longer a full enclosure, but rather a facade, which worked fine for prototyping purposes. 

We included two narrows slits into which the touchscreen edges would slide and be held tightly in place. Unfortunately in our first 3D print, these slits were a little two narrow, and the screen would not fit. 

<div>
<img src="https://user-images.githubusercontent.com/89954856/206882321-f187ec5e-94a3-40f0-a4cd-448f1e397554.png" width="350">
<br><sub>First 3D Print, doesn't quite fit</sub>
</div>
<br>

After our first unsuccessful print, we did two quick test prints to find the exact dimensions for the screen slits. Eventually we achieved a snug fit. For the final print, we switched to white filament to match the color of our fridge.

<div>
<img src="https://user-images.githubusercontent.com/89954856/206882554-5b7057fb-9b30-4146-8240-cc9b977e3a63.png" width="350">
<br><sub>Test print to confirm dimensions</sub>
</div>
<br>

<div>
<img src="https://user-images.githubusercontent.com/89954856/206882656-ff0de9ad-65a0-4465-b963-16e0f85f5a09.png" width="350">
<br><sub>Final print with correct fit and white color</sub>
</div>

#### Button for the Door
Now that we had the touchscreen mounted to the fridge, it was time to add a button to detect when the door opens and closes. We found a spare button lying around from previous projects and used Fusion 360 to design a mount for it. The button snaps into the mount and 3M sticky tape holds the mount to the fridge. There are shallow recesses for the sticky tape so that the mount sits flush agains the fridge.

<div>
<img src="https://user-images.githubusercontent.com/89954856/206923441-3b9a3fd2-74ac-4e90-8623-9b9a77a3a4bd.png" width="350">
<br><sub>Mounting a button to the door</sub>
</div>

#### Software Prototype
In order to make the prototype functional, we needed to write some software. We drew several mockups of the screens and discussed which funtions would be most important to show in our software prototype. In the end, we decided on:
* User closes door, FridgeMon scans contents of fridge and adds/removes items from screen accordingly
* User can see newly added items and is prompted to label them
* As time passes, the "days in fridge" count will increment
* Items approaching expiration date are highlighted in red

To write the software, we chose a Python package called [Tkinter](https://docs.python.org/3/library/tkinter.html). It works well with Raspberry Pi and is easy to use. This GitHub repository contains the following Python files:
* logic.py: contains the basic logic and tracks the state of the smart refrigerator system.
* main.py: produces the graphical user interface. Run this file to start the program.

<div>
<img src="https://user-images.githubusercontent.com/89954856/206923667-d19e624c-ae6e-46eb-946f-f8baad5f1ca0.png" width="350">
<br><sub>Mockup of UI</sub>
</div>
<br>

<div>
<img src="https://user-images.githubusercontent.com/89954856/206924009-fa1db2dd-a534-42d6-b57a-a2390d1f5ebb.png" width="350">
<br><sub>FridgeMon code, using Tkinter</sub>
</div>
<br>

<div>
<img src="https://user-images.githubusercontent.com/89954856/206924145-285cb3b4-2e08-4def-9080-7c98c1cd70b9.png" width="350">
<br><sub>Final software prototype</sub>
</div>

#### Creating the Tags
We prototyped 3 different mechanisms for attaching RFID tags to food items, including:
* glass boxes
* magnetic clips
* sealing clips

Each mechanism is embedded with an RFID tag and has an animal design to help users distinguish unlabeled items. We used laser cutting, 3D printing and some store-bought components for this prototyping exercise. 
<div>
<img src="https://user-images.githubusercontent.com/89954856/206925569-e7168b20-a782-4db2-a011-1a5046d3f71e.png" width="350">
<br><sub>Sealing clip with RFID tag</sub>
</div>
<br>

<div>
<img src="https://user-images.githubusercontent.com/89954856/206921891-df7d1082-0d52-47ff-af62-39ea68fe1963.png" width="350">
<br><sub>Food container with RFID tag</sub>
 </div>
 <br>

#### Implementing RFID
The final piece of the puzzle was to integrate the RFID antenna with our prototype. Most of the affordable RFID antennas on the market are very short-range; users must tap the tag right next to the antenna. For our purposes, we wanted a longer range antenna. We found one that was affordable and seemed like it would work, but unfortunately there were some compatibility issues with it and the RFID tags. In the end, we had to use an antenna that was short range. Although it did work, the user has to put the food item right next to the antenna for it to be detected, which is not ideal. In the interest of having a better demo, we wrote a version of our software that simulates the scanning process and randomly adds and removes food items each time the user closes the door. This simulation was adequate for our prototype and was able to effectively communicate the concept.

<div>
<img src="https://user-images.githubusercontent.com/89954856/206922238-8e5e03a1-2146-4910-a550-999b83e1c45e.png" width="350">
<br><sub>RFID receiver in fridge</sub>
</div>

## Conclusion
Our prototype reached a high level of fidelity and communicates an effective and novel approach for reducing food waste in refrigerators. As a next step, we would like to expand the range of the RFID antenna, build more functions into the user interface, such as the ability to scroll, type custom labels with an on-screen keyboard and edit the expiration dates of items. With these additions, we could provide a fully-functional protype with which we could conduct user testing to gain further insight. 

<div>
<img src="https://user-images.githubusercontent.com/89954856/206882157-c08b62e7-f4b6-4066-9e9e-aea7b59e5cbd.png" width="350">
<br><sub>Final FridgeMon prototype</sub>
 </div>

## Hardware Components
Below are the key hardware components used in this prototype:
* Raspberry Pi 4
* Raspberry Pi 7-inch touchscreen
* Button (for the refrigerator door)
* 3D-printed enclosures for the touchscreen and button
* Enclosures for RFID tags, made with 3D printing and laser cutting
* RFID antenna
* RFID tags

## Team Members
* [Anqi Pan](https://www.linkedin.com/in/anqipan/): UI/UX design, 3D printing and laser cutting of food tags and containers
* [Yue Sun](https://www.linkedin.com/in/yuesun1003/): hardware sourcing & implementation (RFID), software development
* [Tim Huff](https://www.linkedin.com/in/tim-huff-60a05973/): software development, 3D printing of touchscreen enclosure

<div>
<img src="https://user-images.githubusercontent.com/89954856/206879009-ba4da4e0-003e-4351-bfb1-fca19fe51f18.png" width="350">
<br><sub>Yue Sun, Tim Huff & Anqi Pan at GIX project bazaar</sub>
 </div>
 <br>

## Gallery
<p>
    <img src="https://user-images.githubusercontent.com/89954856/206879326-ac4f6859-0e07-41be-9bb1-bc72c847290c.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206879009-ba4da4e0-003e-4351-bfb1-fca19fe51f18.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206879326-ac4f6859-0e07-41be-9bb1-bc72c847290c.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206878615-717ee4a1-c4cd-42b5-b086-74c67e27e956.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206879009-ba4da4e0-003e-4351-bfb1-fca19fe51f18.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206879009-ba4da4e0-003e-4351-bfb1-fca19fe51f18.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206879326-ac4f6859-0e07-41be-9bb1-bc72c847290c.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206879009-ba4da4e0-003e-4351-bfb1-fca19fe51f18.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206879326-ac4f6859-0e07-41be-9bb1-bc72c847290c.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206878615-717ee4a1-c4cd-42b5-b086-74c67e27e956.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206879009-ba4da4e0-003e-4351-bfb1-fca19fe51f18.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/206879009-ba4da4e0-003e-4351-bfb1-fca19fe51f18.png" height="300">
    <img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300">
 </p>
