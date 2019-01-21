#! /usr/bin/env python

import sys
import subprocess
import re
from moviepy.editor import VideoFileClip


def main():
    if len(sys.argv) < 3 or sys.argv[1]=='-h':
        print_usage_and_exit()
    video_path = sys.argv[1]
    print('Video: ', video_path)
    clip = VideoFileClip(video_path)
    duration = clip.duration
    print('Duration in seconds: ', duration)
    time_args = sys.argv[2:]
    times = [ (float(t[:-1])*duration/100 if '%' in t else float(t)) for t in time_args ]
    print(times)
    FFMPEG_PATH = 'ffmpeg'
    for i,t in enumerate(times):
        path_fragment = re.sub(r'[/.]', '_', video_path)
        path_fragment = re.sub(r'\W', '', path_fragment)
        jpg_path = 'screenshot_' + path_fragment + '-' + str(round(t, 3)).replace('.', '_') + '.jpg'
        print('Creating screenshot at', t, 'seconds')
        cmd = [ FFMPEG_PATH, '-y', '-loglevel', 'warning', '-i', video_path, '-ss', str(t), '-frames:v', '1', jpg_path ]
        print(' '.join(cmd))
        subprocess.call(cmd)


def print_usage_and_exit():
    script = sys.argv[0]
    print('\nUSAGE:', script, '<input_video_file> <time point 1> [<time point 2> ...]')
    print('\nThis script expects an input filename and a list of time points (at least one).')
    print('\nEXAMPLES\n')
    print(script, 'test.mov 5')
    print('=> one screenshot at five seconds into the video')
    print()
    print(script, 'test.mov 10% 50%')
    print('=> two screenshots - one near the beginning and one in the middle')
    print()
    print(script, '"https://sample-videos.com/video123/mp4/480/big_buck_bunny_480p_1mb.mp4" 10%')
    print('=> URLs are also allowed.')
    print()
    print(script, '-h')
    print('=> show this information')
    sys.exit(1)


if __name__ == '__main__':
    main()
