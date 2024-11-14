# PixelTagzZ - Gaming Optimized Tags Generation

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Structure](#code-structure)
- [Future Improvements](#future-improvements)
- [Developer Information](#developer-information)

## Project Overview
**PixelTagzZ** is an innovative Python application designed to empower gamers and content creators by generating optimized tags for their gaming content. With a user-friendly interface, this tool allows users to seamlessly input their in-game details and receive personalized, trending hashtags to enhance their visibility on platforms like YouTube and Instagram. By leveraging a robust MySQL database, **PixelTagzZ** ensures that users access relevant and up-to-date tags, making it easier to engage with their audience. Whether you're a casual player or a dedicated streamer, **PixelTagzZ** is your go-to solution for maximizing your online presence in the gaming community.

## Features
- **User-Friendly Interface**: Engages users with a series of prompts to gather relevant information for tag generation.
- **Customizable Tags**: Generates tags based on specific user inputs related to their gameplay experience.
- **Optimized for Social Media**: Provides tags tailored for platforms such as YouTube, Twitch, and Instagram.
- **Dynamic Database Connection**: Utilizes a MySQL database to store and retrieve relevant gaming data and tags.

## Technologies Used
- **Programming Language**: Python
- **Database**: MySQL
- **Libraries**: 
  - `mysql.connector` for database connectivity
  - `random` for tag selection

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd PixelTagzZ
   ```
3. Install the Python and MySQL Connector. You can install it using pip:
   ```bash
   pip install mysql-connector-python
   ```
4. Set up the MySQL database using the provided .CSV files to create the necessary tables.
   - Create a MySQL database named `PixelTagzZ`.
   - Create the tables: `ValorantGameData` and `ValorantTagsData`.
   - Import the .CSV files into the respective tables using the `Table Data Import Wizard` option.

## Usage
1. Run the script:
   ```bash
   python pixelTagzZ.py
   ```
2. Follow the prompts to enter your in-game name, age, country, and social media presence.
3. Based on your inputs, the tool will generate and display optimized tags for your Valorant gameplay.

## Project Structure
- **PixelTagzZ.py**: Main script containing all the functionalities.
- **Database Setup**: MySQL database containing all the required data.
- **Comma Separated Value Files**: The .CSV files containing the tags and game data.

## Code Structure
- **Modules**: 
  - `mysql.connector`: For database connectivity.
  - `random`: For randomizing tag selection.
- **Functions**:
  - `databaseConnectFunc()`: Connects to the MySQL database.
  - `welcomeMsg()`: Displays a greeting message.
  - `userInGameNameFunc()`: Prompts for the user's in-game name.
  - `userAgeFunc()`: Validates and retrieves user age.
  - `userCountryFunc()`: Captures the user's country.
  - `userSocialsFunc()`: Collects social media information.
  - `projectDescriptionFunc(userInGameName)`: Describes the project to the user.
  - `gratitudeMsg(userInGameName)`: Thanks the user for using the application.
- **Class**:
  - `Valorant`: Class to handle data and tag generation algorithms.

## Future Improvements
- **Expanded Game Support**: Adding support for more games and corresponding tag generation.
- **Web Application Version**: Creating a web interface for easier access and usage.
- **Enhanced User Customization**: Allowing users to save their preferences and tag templates.

## Developer Information
- **Developer Name**: Yashank Yadav
- **In-Game Name**: ChampKillzZ
- **Instagram Gaming Handle**: [champkillzz](https://www.instagram.com/champkillzz)
