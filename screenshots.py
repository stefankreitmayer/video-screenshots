import subprocess
from moviepy.editor import VideoFileClip

def main():
    # video_path = 'https://sample-videos.com/video123/mp4/480/big_buck_bunny_480p_1mb.mp4'
    # video_path = 'https://sample-videos.com/video123/mp4/360/big_buck_bunny_360p_30mb.mp4'
    video_path = 'https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_30mb.mp4'
    clip = VideoFileClip(video_path)
    duration = clip.duration
    print('Video: ', video_path, '\tDuration in seconds: ', duration)
    n_thumbnails = 2
    FFMPEG_PATH = 'ffmpeg'
    for i in range(n_thumbnails):
        jpg_path = 'thumb_' + str(i+1) + '_of_' + str(n_thumbnails) + '.jpg'
        t = int((i+0.5) * duration / n_thumbnails)
        print('Creating thumbnail at', t, 'seconds')
        cmd = [ FFMPEG_PATH, '-y', '-loglevel', 'warning', '-i', video_path, '-ss', str(t), '-frames:v', '1', jpg_path ]
        print(' '.join(cmd))
        subprocess.call(cmd)


if __name__ == '__main__':
    main()
