# Smart Home Device System

## Overview
Python program demonstrating OOP principles with smart devices sys.

## Classes
- SmartDevice (Parent): device_id, name, is_on. Methods: power_on(), power_off(), info()
- SmartLight (Child): Extra brightness 0-100. Method: adjust()
- TemperatureSensor (Child): Extra temp. Method: read()
- SecurityCamera (Child): Extra recording. Method: record()

## OOP Concepts Used
1. Inheritance: 3 child classes inherit from SmartDevice via super()
2. Encapsulation: All core attributes are private __ with validation
