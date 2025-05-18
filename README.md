# Embedded Input Reader - Raspberry Pi Pico (MicroPython)

*Graduation project from DECI L3 Semester 1*

A MicroPython project for Raspberry Pi Pico, simulating an input reader system with slide switches, pushbuttons, and output LEDs on Wokwi.

## Project Overview

This project reads a 4-bit binary number from slide switches, converts it to decimal, and displays the value on LEDs. The pushbuttons are monitored using interrupts with debouncing, and the system supports passcode entry to toggle LEDs based on switch positions.

The project faithfully follows the provided circuit schematics and implements all required functionalities, including:

- Reading slide switches and converting binary input to decimal.
- Monitoring pushbuttons with interrupts and debouncing.
- Passcode entry system evaluating last three button presses.
- Toggling output LEDs according to valid passcodes and switch settings.

## Features

- Slide switches control binary input, mapped to LEDs.
- Pushbuttons generate interrupts, with 200ms debouncing.
- Passcode verification toggles LEDs based on switch values.
- Clear mechanism resets button press buffer after 3 inputs.
- Real-time printout of switch values and button presses.

## Technologies Used

- MicroPython
- Raspberry Pi Pico microcontroller
- Wokwi simulator for circuit implementation

## How to Run

1. Open the diagram.js file in the Wokwi simulator to load the circuit schematic.
2. Upload and run the main.py MicroPython code on the Raspberry Pi Pico within the simulator.
3. Use the slide switches to input a 4-bit binary number; observe the decimal equivalent printed in the console.
4. Press the pushbuttons to enter passcodes; the system will toggle LEDs based on valid passcodes and provide print feedback.
5. Monitor the output LEDs for changes according to your interactions

## My Role

I designed and implemented the full system logic including switch reading, interrupt handling with debouncing, and passcode validation. I ensured strict adherence to the schematic and verified all 16 switch combinations and button press sequences.

## Project Links

- [Wokwi Project Link](https://wokwi.com/projects/431298115467740161)  
- [GitHub Repository](https://github.com/Begadbigo/embedded-input-reader)

---

