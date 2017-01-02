# Heads Up

Visualization system for my wearable, built on top of the Vufine+.

## The system

To start, this system attempts to implement several ideas from [Barbara Oakley's "Learning to Learn"](https://www.youtube.com/watch?v=V5BXuZL1HAg).  In particular, the initial prototype implements a split-screen pomodoro timer and flash card system.  The current version of the flash card system does not implement any real interactivity, limiting the utility.

## How it works

The system is built on top of python flask.  It serves a small local webpage that is divided into a grid via flexboxes.  The page loads additional content by setting the innerhtml of the flexboxes to stubs recieved from server endpoints.  This allows a moderate amount of decoupling between display and content.  To run, ""

For the mandarin flashcards, requires a chinese font set like fonts-arphic-ukai or fonts-arphic-uming.
