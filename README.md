# Chess-Pygame
This project is a chess game that supports online multiplayer games as well as offline singleplayer games. This project was made with Python 3.8 along with the Pygame, Sockets and threading modules. The multiplayer mode runs a simple client-server system in which the server will handle the client connections and game management, and the client will handle the user interface and game play.

## Installation

### Windows:

#### Single-Player:
1. Ensure that you have _python_ and _pip_ installed on your machine. You can install from here: https://www.python.org/downloads/
2. Use the following command in command prompt to install _Pygame_: `pip install pygame`
3. Clone this repository to a local directory or download it as a zip and unzip it.
4. For the single-player game open the command prompt and _cd_ to the _single-plyaer_ folder.
5. Use the following command in command prompt to begin the game: `python Chess.py`

#### Multi-Player:
1. Ensure that you have _python_ and _pip_ installed on your machine. You can install from here: https://www.python.org/downloads/
2. Use the following command in command prompt to install _Pygame_: `pip install pygame`
3. Clone this repository to a local directory or download it as a zip and unzip it.
4. For the multi-player game open the command prompt and _cd_ to the _multi-player_ folder.
5. You will have to change the server address in the `server.py` and `network.py` files to the IPv4 address of the machine you will run the server script on.
6. Now you will run the `server.py` file and two instances of the `client.py` file to play online chess.

## Gameplay
This is a short demonstration of how a single-player chess game looks.

![gameplay2 demo](screenshots/gameplay2.gif)