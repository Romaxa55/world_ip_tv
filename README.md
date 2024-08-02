# 🌍 World IPTV Checker 🚀

![GitHub](https://img.shields.io/github/license/Romaxa55/world_ip_tv) ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Romaxa55/world_ip_tv/check_iptv.yml) ![GitHub last commit](https://img.shields.io/github/last-commit/Romaxa55/world_ip_tv)

## 📜 Description

Welcome to the **World IPTV Checker** project! This repository automates the daily checking of IPTV channel availability and generates a new playlist with the available channels. The results of the check are available at the following URL:

📥 [Download Playlist](https://romaxa55.github.io/world_ip_tv/output/index.m3u)

## ⚙️ How It Works

Every day at midnight (UTC), GitHub Actions runs a script to check all channels from the specified playlists. Channels that pass the check are added to a new playlist, which is then published on GitHub Pages.

## 🚀 How to Use

1. **Download the Playlist**: The playlist is available at the following URL: [https://romaxa55.github.io/world_ip_tv/output/index.m3u](https://romaxa55.github.io/world_ip_tv/output/index.m3u).
2. **Add to IPTV Player**: Open your IPTV player (e.g., VLC, IPTV Smarters, GSE Smart IPTV) and add the playlist using the provided URL.
3. **Enjoy Watching**: The playlist is automatically updated daily, ensuring you always have access to the latest working channels.

## 🛠️ Installation and Setup

### 🖥️ Running Locally

If you want to run this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Romaxa55/world_ip_tv.git
    cd world_ip_tv
    ```

2. **Install Dependencies**:
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

3. **Run the Script**:
    ```bash
    python -m iptv_checker
    ```

### 🤖 GitHub Actions

This project is set up to use GitHub Actions for automatically checking channels and updating the playlist. The workflow file `.github/workflows/check_iptv.yml` is configured to run daily and can also be triggered manually through the GitHub interface.

### 🔑 Setting Up Access

To automatically commit changes, a Personal Access Token (PAT) is used. Make sure you create a token and add it to your repository's secrets on GitHub under the name `GH_PAT`.

## 💡 Contributions

If you have suggestions or find bugs, please create an issue or submit a pull request. We welcome community contributions to improve this project!

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for more information.

## 🔍 Resources

- **IPTV Checker Script**: Automates the process of checking and generating the IPTV playlist.
- **GitHub Actions**: Ensures daily checks and updates.
- **GitHub Pages**: Hosts the generated playlist for easy access.

![Coding GIF](https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif)
