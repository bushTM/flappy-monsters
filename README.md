# flappy-monsters
BSCybersecurity Applications of ict, 1st semester project

# group members:
Bushra Tariq, Manal Yasir, Hamna Sanan, Laiba.

# introduction:
This project is a simplified version of the popular flappy bird game, implemented using pygame library in python. The game allows the player to select a bird monster character, navigate through randomly generated pipes, and track scores with a high score system. The code demonstrates fundamental concepts of game  development such as event handling, collision detection, sprite rendering, and  game loops.

# Main Essence of the Code:
The Flappy Bird program is built using multiple core concepts of Python that  come together to create an interactive and enjoyable game experience.  
• Libraries: The code uses the pygame library for graphics, input handling, and  game loops, along with sys for program exit and random for generating  unpredictable pipe positions.  
• Dictionaries: Game assets such as images for background, pipes, birds, and  score digits are stored in a dictionary (IMAGES) for organized access and  efficient management.  
• Functions: The program is modular, with functions like load_images(),  choose_bird(), create_pipe_pair(), check_collision(), play_game(), and show_game_over() each handling a specific part of the game logic. This makes the code easier  to read, maintain, and extend.  
• FPS (Frames Per Second): The game loop is controlled by a clock set to 32  FPS, ensuring smooth animations and consistent gameplay speed. FPS is  crucial because it balances responsiveness with playability — too fast would  make the game unmanageable, too slow would make it boring.  
• Gameplay Mechanics: Gravity and jump strength simulate bird physics,  randomization keeps the game fresh, and collision detection ensures  challenge. 

# Code Structure:
The program is divided into several logical sections:  
• Initialization: Sets up Pygame, screen dimensions, frames per second (FPS),  and global variables.  
• Image Loading: Loads all required assets (background, ground, pipes, birds,  score digits).  
• Character Selection: Provides a menu for the player to choose their bird  sprite.  
• Pipe Creation: Randomly generates pipe pairs with a fixed gap for  gameplay.  
• Collision Detection: Checks if the bird hits pipes, ground, or screen  boundaries.  
• Game Loop: Handles player input, updates positions, manages scoring, and  renders graphics.  
• Game Over Screen: Displays score, high score, and replay/quit options.  • Main Menu: Runs continuously, waiting for the player to start the game.

# Functions Used In Our Code:
• load_images(): Loads and stores all game assets in a dictionary for easy access.  • choose_bird(): Allows the player to select a bird character using arrow keys  and confirm with Enter.  
• create_pipe_pair(): Generates a top and bottom pipe with a vertical gap equal  to one-third of the screen height.  
• check_collision(): Detects collisions between the bird and pipes, ground, or  ceiling.  
• play_game(): Core game loop that manages bird physics, pipe movement,  scoring, and rendering.  
• show_game_over(): Displays game over screen with replay and quit options. 

# Game Mechanics:
• Bird Physics: 
o Gravity pulls the bird down (gravity = 1). o Jump strength (-8) moves the  bird upward when the player presses Space or Up.  
• Pipe Movement: o Pipes move left at a constant speed (pipe_speed = -4).  o New pipes are generated as old ones leave the screen.  
• Scoring:  
o Score increases when the bird successfully passes a pipe.  
o High score is updated after each game.  
• Collision Rules:  
o Bird collides if it touches the ground, ceiling, or pipes. o Collision ends the game and triggers the game over screen.  
Thus we can summarise that The bird is affected by gravity, pulling it downward, while jumps  apply upward force. Pipes move across the screen with randomized gaps, and the player earns  points by passing them. Collision detection ensures challenge, while FPS keeps gameplay  smooth.  
