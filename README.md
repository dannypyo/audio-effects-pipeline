# Audio Effects Pipeline
This project demonstrates how function composition and currying can be used to build a flexible and modular audio processing system.

## Problem Description
In a digital audio workstation, users often want to apply multiple effects (like volume changes, echo, and distortion) to an audio signal.

## Solution Overview
Each audio effect is implemented as a curried function, meaning it returns another function that operates on an audio signal.
These effects are then combined using a compose function, creating a clean and flexible processing pipeline.
