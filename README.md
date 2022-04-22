# Salvatore-Aranzulla
[![CodeFactor](https://www.codefactor.io/repository/github/danyb0/salvatore-aranzulla/badge)](https://www.codefactor.io/repository/github/danyb0/salvatore-aranzulla)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
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

# Local setup
- #### Install the requirements
  ```bash
  pip install -r requirements.txt
  ```
  For playing songs [FFmpeg](https://ffmpeg.org/) needs to be installed.
  
- #### Create a `.env` file in the bot folder and write your bot token [(How to create a Discord bot)](https://discordpy.readthedocs.io/en/stable/discord.html)

  ```bash
  TOKEN="BOT_TOKEN"
  ```
