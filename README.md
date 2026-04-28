# Flappy Gimble

## Demo
Demo Video: 

## Repository
Github Repo: [Click here](https://github.com/CrazhArt/flappy-gimble/tree/main)

## Description

Flappy Gimble is a simple game made for the purpose of entertainment. Its design is inspired by and game mechanics used from the once popular mobile game, Flappy Bird, using a cave theme to create an adventure-like scenario. The game is about a vampire named Gimble, who consumes a potion of flight to escape the treacherous crumbling caves, dodging stalagmites and stalactites that stand in her path. Its production is primarily through the use of the PyGame library, also with use of the Random library.

To create the scene, I designed a placeholder background and foreground to start mapping out the size and speed that I want before creating classes for the players, obstacles, and restarting the game. Once I was finished, I designed the final assets and replaced the placeholders. Within these classes are variables that draw each class on the screen and update their positions as the game progresses. For the player class, I added functions that update the velocity of the character, which make her rise and fall with each click. While flying, the character also flips through an image sequence of images at a constant rate, giving the illusion of animation. Once the game is over, the restart button appears, checking if it collides with the user's cursor to restart the game once clicked.

While running, the obstacles and foreground scroll to the left, creating an illusion that the character is moving to the right when in reality she is stationary in her x position. A scroll speed variable is set to give the game a movement speed that is not too fast, but not too slow as obstacles spawn at a constant rate in random positions, utilizing the Random library. A game over condition occurs when the player collides with either the obstacle or hits the ground, ending the game and giving the player the option to restart.

In the future, I would like to reproduce this same game on a proper game engine, as well as even trying to recreate the simple game concept in other languages, such as C# or C++. From here marks my start as a video game developer.