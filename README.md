# Video Screenshots

A quick and dirty Python script to extract screenshots from a video file

## Dependencies

This script assumes that [ffmpeg](https://www.ffmpeg.org) is installed.

Moreover, it uses the [moviepy](https://zulko.github.io/moviepy) library to determine the duration of the video.

`pip install moviepy`

Tested with Python 3.5

## Usage

Specify an input filename and a list of time points:

`./screenshots.py <input_video_file> <time point 1> [<time point 2> ...]`

## Examples

`./screenshots.py test.mov 5`

=> one screenshot, five seconds into the video

`./screenshots.py test.mov 10% 50%`

=> two screenshots - one near the beginning and one in the middle

### URLs are allowed:

`./screenshots.py "https://sample-videos.com/video123/mp4/480/big_buck_bunny_480p_1mb.mp4" 10%`
