# FridgeMon
<img src="https://user-images.githubusercontent.com/89954856/205183749-ebe33c10-e898-447b-a48f-16283a04357f.png" height="300">

## Overview
This repository contains prototype software for FridgeMon, a smart refrigerator system that helps users keep track of food in their fridge, 
thereby reducing waste. 
This was my group's final project for our Fabrication and Prototyping class at the [Global Innovation Exchange](https://gixnetwork.org/) in Bellevue, Washington. 

## Solution
We mounted a touchscreen to a refrigerator to display the contents and track how long each item has been in the fridge. Items are sorted oldest 
to newest to help users prioritize what should be eaten next. 

Food containers are equipped with RFID tags that the smart fridge system can read. The user simply adds and removes containers, and the fridge automatically
knows which containers are in the fridge and how long they have been there. Each container has a unique animal design on top to help the user 
differentiate the containers. When a new container is added to the fridge, the user has the option to label the contents of that container.

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
* [Tim Huff](https://www.linkedin.com/in/tim-huff-60a05973/)
* [Yue Sun](https://www.linkedin.com/in/yuesun1003/)
* [Anqi Pan](https://www.linkedin.com/in/anqipan/)
