# osr2png - rewrite³

[![GitHub release](https://img.shields.io/github/release/xjunko/osr2png.svg?style=for-the-badge&logo=github)](https://github.com/xjunko/osr2png/releases/latest)

osr2png is a CLI thumbnail generator for osu! maps.

as I am very lazy and only update this thing few times a year, lots of stuff gonna break. if that happens please file an issue.

## Styles

## Style 1
![image](https://github.com/xjunko/osr2png/assets/44401509/98f06ad3-edf7-4998-a853-c4ed24941af3)
![image](https://github.com/xjunko/osr2png/assets/44401509/463729ef-d474-445a-93b1-d08824727f59)

## Style 2
![image](https://github.com/xjunko/osr2png/assets/44401509/d6066692-1c27-4356-b7f9-58b19b4b5e20)
![image](https://github.com/xjunko/osr2png/assets/44401509/8b548487-4ccd-4ba4-b7b4-10e700189878)


## Running

Latest binaries for Linux/Windows can be downloaded from [here](https://github.com/xjunko/osr2png/releases/latest).

Simply unpack the file somewhere and run it with your terminal.

##### Linux / Powershell

```bash
./osr2png <arguments>
```

## Run arguments

```txt
usage: main.py [-h] [-v] [-r REPLAY] [-b BEATMAP] [-m MESSAGE] [-s STYLE] [-width WIDTH] [-height HEIGHT] [-dim BACKGROUND_DIM] [-blur BACKGROUND_BLUR] [-border BACKGROUND_BORDER]

An open-source osu! thumbnail generator for lazy circle clickers.

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -r REPLAY, --replay REPLAY
                        [Optional] The path of the .osr file
  -b BEATMAP, --beatmap BEATMAP
                        [Optional] The path of the .osu file, if using a custom beatmap.
  -m MESSAGE, --message MESSAGE
                        [Optional] The extra text at the bottom
  -s STYLE, --style STYLE
                        Style of Image, [1: default 2: akatsuki]
  -width WIDTH, --width WIDTH
                        [Optional] The width of the image.
  -height HEIGHT, --height HEIGHT
                        [Optional] The width of the image.
  -dim BACKGROUND_DIM, --background-dim BACKGROUND_DIM
                        [Optional] The dim of beatmap background.
  -blur BACKGROUND_BLUR, --background-blur BACKGROUND_BLUR
                        [Optional] The blur of beatmap background.
  -border BACKGROUND_BORDER, --background-border BACKGROUND_BORDER
                        [Optional] The border of beatmap background's dim.
```

Examples:

```
./osr2png -r replay.osr

./osr2png -r replay.osr -b beatmap_file.osu

./osr2png -r replay.osr -dim 0.5 -border 50 -blur 15

./osr2png -r replay.osr -m "FINALLY FCED"
```

## Credits

- [rosu-pp](https://github.com/MaxOhn/rosu-pp): The PP calculator used in this program.
- [kitsu.moe](https://kitsu.moe/): The mirror that is used for getting the beatmap
  data.
