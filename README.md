# 🌍 World IPTV Checker — Free Live TV Channels, Updated Daily

<p align="center">
  <strong>Automatically verified IPTV playlist with working channels only</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/romaxa55/world_ip_tv/check.yml?branch=main&style=for-the-badge&label=Last%20Check&logo=github-actions&logoColor=white" alt="Last check status" />
  <img src="https://img.shields.io/badge/Channels-Daily_Verified-00C853?style=for-the-badge&logo=tv&logoColor=white" alt="Daily verified channels" />
  <img src="https://img.shields.io/github/commit-activity/m/romaxa55/world_ip_tv?style=for-the-badge&color=blueviolet&label=Commits" alt="Commit activity" />
  <img src="https://img.shields.io/github/stars/romaxa55/world_ip_tv?style=for-the-badge&color=FFD700&logo=github" alt="Stars" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License" />
</p>

<p align="center">
  <a href="https://romaxa55.github.io/world_ip_tv/output/index.m3u">📥 Download Playlist</a> •
  <a href="https://megav.app/iptv-playlists">IPTV on MegaV</a> •
  <a href="https://t.me/MegaV_VPN">Telegram @MegaV_VPN</a>
</p>

---

## Quick Start — 30 Seconds to Live TV

Copy this URL and paste it into any IPTV player:

```
https://romaxa55.github.io/world_ip_tv/output/index.m3u
```

That's it. No sign-up. No account. No payment. Just free live TV.

### How to add in VLC
1. Open VLC → **Media** → **Open Network Stream**
2. Paste the URL above → Click **Play**

### How to add in IPTV Smarters / TiviMate / Televizo
1. Add playlist → **M3U URL**
2. Paste the URL above → Save

---

## How It Works

```
  GitHub Actions (every 6 hours)
         │
         ▼
  Fetch source M3U lists
  from 50+ public sources
         │
         ▼
  Python checker tests
  every channel URL
  (HTTP 200 + stream response)
         │
         ▼
  Dead channels removed
  Working channels kept
         │
         ▼
  Clean M3U published to
  GitHub Pages (free CDN)
         │
         ▼
  You stream via
  romaxa55.github.io/world_ip_tv/
```

> With 648+ commits the automation has been running reliably since the project launched — channels that stop working are purged within hours.

---

## Supported Players

| Player | Platform | How to Add |
|---|---|---|
| **VLC** | Windows, macOS, Linux, Android, iOS | Media → Open Network Stream → paste URL |
| **IPTV Smarters Pro** | Android, iOS, Windows | Xtream / M3U URL → paste URL |
| **TiviMate** | Android TV, Fire TV | Add Playlist → M3U URL → paste URL |
| **Kodi** (PVR IPTV) | All platforms | PVR IPTV Simple Client → M3U URL |
| **Televizo** | Android, Android TV | Add playlist → URL → paste URL |
| **GSE Smart IPTV** | iOS, macOS | Remote Playlists → Add → paste URL |
| **Streamlink** | CLI / Linux | `streamlink "m3u-url" best` |

---

## Geo-Restricted Channels? Use MegaV VPN

Some channels in the playlist are **geo-restricted** — they only stream to viewers in specific countries. If a channel shows as live but won't play for you, a VPN will fix it.

**[MegaV VPN](https://megav.app)** is the recommended companion app:

- 🆓 **Free** — no subscription needed for basic use
- ⚡ **VLESS Reality** — bypasses deep packet inspection; works in Iran, Russia, China, Turkey
- 📺 **IPTV page built-in** — browse and launch playlists from inside the app
- 🔒 **No-logs** — your viewing history stays private
- 🌍 **15 languages** — EN, RU, ZH, ES, DE, FR, JA, KO, VI, AR, FA, IT, TR

> ➡️ Get MegaV VPN: **[megav.app/iptv-playlists](https://megav.app/iptv-playlists)**
> ➡️ Telegram: **[@MegaV_VPN](https://t.me/MegaV_VPN)**

---

## Channel Coverage

The playlist aggregates channels from public sources covering:

- 🌍 **Europe** — UK, Germany, France, Spain, Italy, Russia, Poland, Turkey and more
- 🌏 **Asia** — China, Japan, Korea, India, Vietnam, Iran, Saudi Arabia and more
- 🌎 **Americas** — USA, Canada, Brazil, Mexico and more
- 🌍 **Africa & Middle East** — Egypt, UAE, Morocco and more
- 📰 **News** — BBC, CNN, Al Jazeera, RT, Euronews and more
- ⚽ **Sports** — regional sports channels
- 🎬 **Movies & Entertainment** — general entertainment channels

> **Note:** All sources are publicly available. This repository does not host or redistribute any video streams — it only maintains a verified list of public stream URLs.

---

## Contributing

Found a channel that's broken, or want to add a new source list?

1. **Fork** this repository
2. Edit `sources/` to add your M3U source URL
3. Run `python checker.py` locally to verify
4. Open a **Pull Request** with a description of what you added

### Reporting broken channels
Open an [Issue](https://github.com/romaxa55/world_ip_tv/issues) with:
- Channel name
- Country
- The broken URL (if known)

The automated checker will remove it on the next run, but your report helps improve source selection.

---

## Technical Details

- **Language:** Python 3
- **CI/CD:** GitHub Actions (runs every 6 hours)
- **Output:** M3U playlist published via GitHub Pages
- **Checking method:** HTTP HEAD + GET request with stream validation
- **Timeout:** 10 seconds per channel
- **Commits:** 648+

---

## Legal

This project collects and verifies **publicly available** stream URLs. It does not:
- Host, redistribute, or store any video content
- Circumvent any access controls or DRM
- Provide access to paid or subscription content

If you are a rights holder and believe a URL in this list is infringing, please open an issue and it will be removed promptly.

---

## Give Us a Star

If this playlist saved you from paying for a TV subscription — please leave a star! It motivates continued maintenance and improvements.

<p align="center">
  <a href="https://github.com/romaxa55/world_ip_tv/stargazers">
    <img src="https://img.shields.io/github/stars/romaxa55/world_ip_tv?style=for-the-badge&color=FFD700&logo=github&label=Star+this+repo" alt="Star on GitHub" />
  </a>
</p>

---

## Keywords

`free iptv` · `iptv m3u` · `iptv playlist 2025` · `free live tv` · `m3u playlist` · `iptv checker` · `working iptv` · `iptv smarters playlist` · `tivimate playlist` · `vlc iptv` · `kodi iptv` · `free iptv channels` · `iptv github` · `world iptv` · `live tv channels` · `free streaming`

---

## Powered by MegaV VPN

<p align="center">
  <a href="https://megav.app">
    <img src="https://img.shields.io/badge/MegaV_VPN-Free_VPN_for_IPTV-blueviolet?style=for-the-badge&logo=shield&logoColor=white" alt="MegaV VPN" />
  </a>
  &nbsp;
  <a href="https://t.me/MegaV_VPN">
    <img src="https://img.shields.io/badge/Telegram-@MegaV__VPN-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram" />
  </a>
  &nbsp;
  <a href="https://github.com/romaxa55/MegaV_Public">
    <img src="https://img.shields.io/badge/GitHub-MegaV_Public-181717?style=for-the-badge&logo=github&logoColor=white" alt="MegaV on GitHub" />
  </a>
</p>

<p align="center">
  <a href="https://megav.app">megav.app</a> — The VPN that works where others fail. VLESS Reality, No-logs, Free.
</p>

---

MIT License © [romaxa55](https://github.com/romaxa55)
