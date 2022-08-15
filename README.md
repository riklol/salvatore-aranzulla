# ![Senza nome](https://user-images.githubusercontent.com/66164380/164801108-02bfda88-eae3-4162-b140-716405886277.png) Salvatore-Aranzulla
[![CodeFactor](https://www.codefactor.io/repository/github/wlafdev/salvatore-aranzulla/badge)](https://www.codefactor.io/repository/github/wlafdev/salvatore-aranzulla)
[![License: Beerware](https://img.shields.io/badge/License-Beerware-yellow)](./LICENSE)
[![version](https://img.shields.io/github/v/release/DanyB0/salvatore-aranzulla?color=orange)](https://github.com/DanyB0/salvatore-aranzulla/releases)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
#

# Commands
| **COMMAND** |        **ARGUMENTS**       |                           **DESCRIPTION**                          |
|:-----------:|:--------------------------:|:------------------------------------------------------------------:|
| ----------- | -------------------------- | ------------------------------------------------------------------ |
|  **Music**  |                            |                                                                    |
| _!join_     |                            |                       Join a voice chat (vc)                       |
| _!play_     |       song name/link       |                   Play a song in vc from YouTube                   |
| _!pause_    |                            |                         Pause a playing song                       |
| _!resume_   |                            |                         Resume a paused song                       |
| _!stop_     |                            |                         Stop a playing song                        |
| _!leave_    |                            |                        Leave the voice chat                        |
| _!lyrics_   |       artist - song        |                        Get the song lyrics                         |
| ----------- | -------------------------- | ------------------------------------------------------------------ |
|  **Weeb**   |                            |                                                                    |
| _!neko_     |                            |                          Get a neko image                          |
| _!idhent_   | hentai ID (6 digit number) | Search for the given hentai on [nhentai.net](https://nhentai.net/) |
| _!rhent_    |                            |    Get a random hentai from [nhentai.net](https://nhentai.net/)    |
| ----------- | -------------------------- | ------------------------------------------------------------------ |
|  **Other**  |                            |                                                                    |
| _!ping_     |                            |                      Get the current bot ping                      |
| _!credits_  |                            |                          Show the credits                          |

# Installing
### Windows
- Clone the repository
  ```bash
  git clone https://github.com/DanyB0/salvatore-aranzulla.git
  ```
- Install [Python>=3.8 pip](https://www.python.org/) and [FFmpeg](https://ffmpeg.org/) for playing songs
- Install the requirements
  ```bash
  pip install -r requirements.txt
  ```
  
- Create a `.env` file in the bot folder and write your bot token [(How to create a Discord bot)](https://discordpy.readthedocs.io/en/stable/discord.html)

  ```bash
  TOKEN="BOT_TOKEN"
  ```
### Linux or WSL
- Clone the repository
  ```bash
  $ git clone https://github.com/DanyB0/salvatore-aranzulla.git
  ```
- Install Python>=3.8 pip and FFmpeg for playing songs
- Create a `.env` file in the bot folder and write your bot token [(How to create a Discord bot)](https://discordpy.readthedocs.io/en/stable/discord.html)

  ```bash
  TOKEN="BOT_TOKEN"
  ```

- Run the `install.sh` script
- Run the `start.sh` script
- For updating the bot you can run the `update.sh` script

# Team
<a href="https://github.com/DanyB0/salvatore-aranzulla/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DanyB0/salvatore-aranzulla" />
</a>

# License
[Beerware License](./LICENSE)
