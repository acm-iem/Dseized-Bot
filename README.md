<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/acm-iem/Dseized-Bot">
    <img src="https://github.com/acm-iem/Dseized-Bot/blob/master/data/Deseized%20Logo%20V2%20Transparent-01.png" alt="Logo">
  </a>

  <h3 align="center">Dseized Bot</h3>

  <p align="center">
    For all your bot needs !
    <br />
    <a href="https://github.com/acm-iem/Dseized-Bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/acm-iem/Dseized-Bot">View Demo</a>
    ·
    <a href="https://github.com/acm-iem/Dseized-Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/acm-iem/Dseized-Bot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installing-dependencies">Installing Dependencies</a></li>
        <li><a href="#setting-up-the-bot-and-running-it">Setting up the bot and running it</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributions">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="centre">
  <a href="https://github.com/acm-iem/Dseized-Bot">
    <img src="https://github.com/acm-iem/Dseized-Bot/blob/master/data/About%20the%20project.png" alt="preview" width="1280">
  </a>
  <br>
  <br>
  <br>
</div>


This repository contains all of the code required **NOTE** you may need to download other dependencies which will be mentioned below. This bot has many features such as playing songs in multiple servers and making a queue for songs. [Discord.py](https://pypi.org/project/discord.py/)


Make sure you have [**Python**](https://python.org) installed on your computer before continuing.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

[Python](https://python.org)


<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

* Python (Preferablyy version 3.9)
* Discord API
* Youtube-dl
* MAL (My anime list) API
* FFMPEG


<p align="right">(<a href="#top">back to top</a>)</p>

### Installing Dependencies


* **You have to install the pypi packages given below:**
    * [Discord.py](https://pypi.org/project/discord.py/)
        * `$ pip install discord.py`
        * `$ pip install discord.py[voice]`
    * [Youtube-dl](https://pypi.org/project/youtube_dl/)
        * `$ pip install youtube_dl`
    * [mal-api 0.4.0 ](https://pypi.org/project/mal-api/)
        * `$ pip install mal-api`

* **Install FFMPEG**
   * Download **ffmpeg** from [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)
   * **Extract** the zip file 
   

Change the API key from your own by getting it from developer portal in [Discord](https://discord.com/developers/applications)


<p align="right">(<a href="#top">back to top</a>)</p>


 ##  Repository's sections:
   ### **This repository is divided in 6 sub sections :** 
   * [Cogs](https://github.com/acm-iem/Dseized-Bot/tree/master/Cogs) -This folder contains the extensions and some APIs which the bot uses to perform operations like music playing etc.
   * [data folder](https://github.com/acm-iem/Dseized-Bot/tree/master/data) - This folder contains token text file which stores the data inputted by user while using bot commands.
   * [bot.py](https://github.com/acm-iem/Dseized-Bot/blob/master/bot.py) - This .py file contains the code of Dseized bot which loads and unloads data using some extensions listed in      [Cogs](https://github.com/acm-iem/Dseized-Bot/tree/master/Cogs) folder.
   * [Readme file](https://github.com/acm-iem/Dseized-Bot/blob/master/README.md) - This file contains the essential details of the project along with mentioned prerequisites required to run this Discord Bot on your device.
   * [Contributing file](Contributing.md) - This file contains the rules and preworks in the form of *Documentation* which are essentials for contributing to this project.
   * [License file](https://github.com/acm-iem/Dseized-Bot/blob/master/LICENSE) - This file contains the legal information such as copyright ownership of this project.
   
  
 ###   Setting up the bot and running it

1. Clone the repo
   ```sh
   git clone https://github.com/acm-iem/Dseized-Bot.git
   ```
2. Enter your token to your generated BOT token in ./data/token.txt

3. Run bot.py

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Add more functionalities
- [ ] Publishing it in a cloud server
- [ ] Quality of life changes


See the [open issues](https://github.com/acm-iem/Dseized-Bot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributions

### **For contributing to this project, kindly read rules mentioned in [Contributing.md](Contributing.md) file.**<br>
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/acm-iem/Dseized-Bot.svg?style=for-the-badge
[contributors-url]: https://github.com/acm-iem/Dseized-Bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/acm-iem/Dseized-Bot.svg?style=for-the-badge
[forks-url]: https://github.com/acm-iem/Dseized-Bot/network/members
[stars-shield]: https://img.shields.io/github/stars/acm-iem/Dseized-Bot.svg?style=for-the-badge
[stars-url]: https://github.com/acm-iem/Dseized-Bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/acm-iem/Dseized-Bot.svg?style=for-the-badge
[issues-url]: https://github.com/acm-iem/Dseized-Bot/issues
[license-shield]: https://img.shields.io/github/license/acm-iem/Dseized-Bot.svg?style=for-the-badge
[license-url]: https://github.com/acm-iem/Dseized-Bot/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/acm-iem/
