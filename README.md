# Twitch Video Maker
This program gathers recent Twitch clips of a certain game and stitches them together into a single video, while also attributing the clips' respective owners.

[Here](https://drive.google.com/file/d/133_dwMS-HZ-Lvl3rnEFK64MwImZZb_6N/view?usp=sharing) is an example video.

The clips are retrieved using the [Twitch API](https://dev.twitch.tv/docs/api/), downloaded using `youtube_dl`, and concenated/edited with `moviepy=1.0.0`.

If you want to use this program, you will need to create a file called `key.txt` that contains your Twitch API key.
It takes a *looonnnng* time to edit the clips into a single video with `moviepy`, but I haven't found a better alternative. `opencv` doesn't include audio, so that isn't an option, either.