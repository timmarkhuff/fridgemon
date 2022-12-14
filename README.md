# FridgeMon

## Overview
FridgeMon is a smart refrigerator system that helps users keep track of food in their fridge, 
thereby reducing waste. This was my group's final project for our Fabrication and Prototyping class at the [Global Innovation Exchange](https://gixnetwork.org/) in Bellevue, Washington. [This short video](https://www.youtube.com/watch?v=WqKrQHDvA54) shows how it works.

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
<img src="https://user-images.githubusercontent.com/89954856/206934471-d11f0e04-8b60-4de8-8248-c5b801e0ca27.png" width="350">
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
<img src="https://user-images.githubusercontent.com/89954856/206933923-c805b4cc-5aaf-4b7c-8c04-d79cc31633fd.png" width="350">
<br><sub>Mini fridge, acquired online</sub>
</div>

#### Prototyping the Touchscreen Enclosure
Now that the basic functionality of the system had been determined, we returned to the question of where to place the touchscreen. Instinctively, we moved it to the door of the fridge, but this presented a problem: the user would be unable to view the screen while the fridge was open. We debated the pros and cons of this for a while. On one hand, perhaps the user shouldn't be looking at the screen while the door is open; this wastes electricity. On the other hand, perhaps users need to see what is on the screen while they are looking inside the fridge, and if they are unable, this might result in frustration and repeated door opening. In the end, we decided to err on the side of giving the user more information and mounted the screen above the door. In the context of our mini fridge, this means putting the screen on top of the fridge, but in a full-sized fridge, this might mean putting it on the freezer door. 

We built the first screen prototypes out of cardboard in order to quickly explore different configurations. We chose to use a Raspberry Pi Touchscreen for our project, so all of the enclosures were built to fit that. After a few iterations of the cardboard prototypes, we had arrived at a concept that we liked. 

<div>
<img src="https://user-images.githubusercontent.com/89954856/206880983-11837cc1-5734-436c-8528-9c2e7cf51bca.png" width="350">
<br><sub>Early prototype of screen</sub>
</div>

#### 3D Printing the Enclosure
When it came time to 3D print the touchscreen enclosure, we realized we had to make a few modifications to our design. First, our design was too large to fit on the Ultimaker printer bed in the orientation we wanted. We simplified the design a bit so that it was no longer a full enclosure, but rather a facade, which worked fine for prototyping purposes. 

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
Now that we had the touchscreen mounted to the fridge, it was time to add a button to detect when the door opens and closes. We found a spare button lying around from previous projects and used Fusion 360 to design a mount for it. The button snaps into the mount and 3M sticky tape holds the mount to the fridge. There are shallow recesses for the sticky tape so that the mount sits flush against the fridge.

<div>
<img src="https://user-images.githubusercontent.com/89954856/206923441-3b9a3fd2-74ac-4e90-8623-9b9a77a3a4bd.png" width="350">
<br><sub>Mounting a button to the door</sub>
</div>

#### Software Prototype
In order to make the prototype functional, we needed to write some software. We drew several mockups of the screens and discussed which functions would be most important to show in our software prototype. In the end, we decided on:
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
<br>
<img src="https://user-images.githubusercontent.com/89954856/206934334-26768c5d-f3b3-4d6d-a9ef-5f62de30c5a8.png" width="350">
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
<img src="https://user-images.githubusercontent.com/89954856/206934622-e3eccdaa-a61c-43c4-a333-d7da696f5d27.png" width="350">
<br><sub>RFID receiver in fridge</sub>
</div>

## Conclusion
Our prototype reached a high level of fidelity and communicates an effective and novel approach for reducing food waste in refrigerators. As a next step, we would like to expand the range of the RFID antenna, build more functions into the user interface, such as the ability to scroll, type custom labels with an on-screen keyboard and edit the expiration dates of items. With these additions, we could provide a fully-functional prototype with which we could conduct user testing to gain further insight. 

<div>
<img src="https://user-images.githubusercontent.com/89954856/206934212-65914080-a0b3-485b-80b6-54d152f48ef4.png" width="350">
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

## Gallery
<p>
    <img src="https://user-images.githubusercontent.com/89954856/206935151-55b73f89-44ef-4c42-8373-c16513369b7a.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935038-16fc8794-5606-4068-b920-e4aca327030a.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935060-b0258ee1-d6e8-425f-bfa5-7cf5a1382989.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935099-274f415a-56bc-4b29-95e9-231c2d9b833a.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935118-9600ab70-a6a1-49fe-b0ce-926c565f5e66.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935188-ea2f4d0f-54ad-404b-bd10-fbc4fc7c2523.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935212-91af5cb9-4c1d-4c74-84e2-8523faf33b9c.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935234-81bc2954-9a9c-4b31-9eaa-50226b1de832.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935491-4c904d48-ec08-4786-9ca6-f783bbf65961.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935517-32727164-9642-403e-8c63-e5334f3b4977.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935546-f375355f-dd0d-4ca6-9387-798f66f1a69b.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935568-d1f7abb5-b504-4c9a-902c-4b7fa2fba9aa.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935594-c13c9075-540a-46cf-8fee-794b78165088.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935616-d99cd4d2-cf79-4c57-a1f9-78d3bc2273a2.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935651-212b5bfb-3ba7-4f02-adcf-d31c5538f713.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935683-9c81201a-0696-4048-a708-68f0b4ab9aa7.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935722-9e778f00-6726-4f62-ac13-3b7aaf3c6632.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935770-521dbe30-e62d-42b5-8d21-9d1ac18b2454.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935789-5694d557-84b8-46fa-93e5-ed38be4876ef.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935818-9c3da9e4-d4e4-4f4e-935f-4c39fc10e7e0.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935851-e43801ec-b161-4515-992a-bf44734debe8.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935879-f79bec67-310c-40f4-a995-5c88254e81b9.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935903-819440ee-2626-4655-9655-1961e72c2ccb.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935937-185780ae-ed0d-4af0-8747-544565a7890b.png" height="250">
    <img src="https://user-images.githubusercontent.com/89954856/206935957-aff46afd-d0e2-46cb-848b-ccc601768d3a.png" height="250">
 </p>
