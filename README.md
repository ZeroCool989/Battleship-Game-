# Battleship Game Build in Python

## Portfolio Project 3 - Python Essentials

The objective of the third project was to construct an interactive, logical game that facilitates user engagement in a competitive setting with a computer-based opponent.

# Table of Contents
1. Link to app
3. How to play
4. Code Structure
5. Technologies Used
6. Testing
7. Deployment
8. Credits
9. Acknowledgements
# Link to app
The app can be found <a href="https://pp3-battleship-game.herokuapp.com/" target="_blank" rel="noopener">here</a>. (Note: Right click on link to open a new tab).

# How to Play 
1.Run the code in a Python environment.
![image](https://github.com/ZeroCool989/Battleship-Game-/assets/75548207/f6ea11c9-541d-4b94-b49f-79796a7b3c90)
2.Enter your name when prompted.
![image](https://github.com/ZeroCool989/Battleship-Game-/assets/75548207/e13231cd-cb0e-44ba-a3b0-f29571de6c8a)
3.For each turn, enter a row and column guess.
![image](https://github.com/ZeroCool989/Battleship-Game-/assets/75548207/432f9538-e834-450b-8272-145f7f4c13be)
4.If your guess matches the location of the battleship, you win the game.
5.If you use up all 5 turns without guessing the correct location, you lose the game.
![image](https://github.com/ZeroCool989/Battleship-Game-/assets/75548207/b9f7d16b-300c-4a5f-8118-aacdf947c51f)
6.You will be prompted to play again or quit.
![image](https://github.com/ZeroCool989/Battleship-Game-/assets/75548207/0743fede-d879-4303-bc80-6f6c648a6a75)
## Code Structure 

The Battleship game is coded in Python. Below is a simple overview of the game's setup:

1. **Creating the Game Board (`create_board`):**
   - Makes an 8x8 board using a 2D array. Each spot can either be a battleship location or a player guess.

2. **Placing the Battleship (`place_ship`):**
   - Randomly places the battleship on the board. The exact location remains hidden from the player.

3. **Showing the Board (`print_board`):**
   - This function displays the current state of the game board, indicating the spots guessed by the player.

4. **Getting the Player's Guess (`get_user_input`):**
   - Prompts the player for row and column guesses and ensures the input is valid and within the game board's range.

5. **The Main Game Loop (`main`):**
   - Manages the gameplay, allowing up to 5 guesses for the player to find the battleship and updates the board after each guess.

6. **Checking Win or Lose Conditions:**
   - Inside the `main` function, the game checks if the player has successfully found the battleship within the allowed guesses.

7. **Scores and Leaderboard (`save_score`, `display_leaderboard`):**
   - Records players' scores based on their performance and displays the top scores from the leaderboard.

8. **Replay Option (In `main`):**
   - After each game, players are given a choice to play again or exit the game.

9. **Starting the Game:**
   - The game begins by running the `main` function, which is the entry point when the script is executed.

# Technologies Used:
### Programming Languages:
* Python
### Git
* Git was used for version control by utilizing the codeanywhere terminal to commit to Git and Push to GitHub.
### Github
* GitHub is used to store the projects code after being pushed from Git.

# Testing
## Functionality testing
* Each piece of code was tested in Gitpod.
* I also tested the app once the final product was deployed.
## Code Validation
* The code was checked using CI Python Linter online checker.

# Deployment
The project was deployed to GitHub Pages using the following steps, I used Gitpod as a development environment where I commited all changes to git version control system. I used the push command in Gitpod to save changes into GitHub:

1. Log in to GitHub and locate the GitHub Repository.
2. At the top of the Repository, click on the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch" and click on save.
5. The page will automatically refresh.
6. The now published site link shows at the top of the page.

The project was then deployed to Heroku using the following steps:

1. Log in to Heroku and add a new app.
2. Link the project from GitHub to Heroku.
4. Add the Python and NodeJS buildpacks.
5. Manually deploy the project (I used the manual deploy option in order to control what version was deployed to the live environment).

# Credits
* The code for the structure of the game board was adapted from the below example (right click to open in new tab).
   https://coderspacket.com/battleship-game-in-python
* Youtube was great resource for answering questions I had. Where several tutorials where helpful. 
    * https://www.youtube.com/watch?v=7Ki_2gr0rsE
    * https://www.youtube.com/watch?v=alJH_c9t4zw
    * https://www.youtube.com/watch?v=u3yo-TjeIDg
    * https://www.youtube.com/watch?v=n0ngeLBJBNU

# Acknowledgements
* Slack Community
* My mentor for support, advice and feedback.
