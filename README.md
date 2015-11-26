# SubScribe
Python Utility to convert your video files to images transcribed with their subtitles.

##The Idea
1. Download a video using `youtube-dl https://www.youtube.com/watch?v=PTmCxbcRXs4 --write-auto-sub` 
2. Run a script that uses the mp4 file and the srt file to generate an image (or a set of images) like this:
![Image](https://scontent-hkg3-1.xx.fbcdn.net/hphotos-xpt1/v/t1.0-9/11139985_643154262493379_4766804901696677874_n.jpg?oh=97e2bc0a211442c11167744906e197de&oe=56C052AE)


## Usage
1. Download a video using `youtube-dl https://www.youtube.com/watch?v=PTmCxbcRXs4 --write-auto-sub` or just have a video file with a corresponding srt file ready.
2. How to use:

```
python script.py --help
usage: script.py [-h] video sub

positional arguments:
  video       path to video file
  sub         path to sub file

optional arguments:
  -h, --help  show this help message and exit
```

3. Examples:
`python script.py samples/a/a.webm samples/a/a.srt`

## Sample Outputs

###Moon Movie
![Image](samples/moon/selected/frame0577.jpg)
![Image](samples/moon/selected/frame0631.jpg)
![Image](samples/moon/selected/frame4188.jpg)
![Image](samples/moon/selected/frame5041.jpg)



###Sample Youtube Videos
![Image](samples/a/output/frame0034.jpg)
![Image](samples/b/output/frame0055.jpg)

## Todo
- [ ] Think of a cool name for the repo.
- [ ] Add an optional youtube-dl wrapper
- [ ] Add to pip
- [ ] Improve text overlay, make it more visible and allow it to be modified using CLI
- [x] Add demos to readme.
- [ ] Add contributing.md




## Contributing
Post issues and send PRs.
