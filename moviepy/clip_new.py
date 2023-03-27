from moviepy.editor import *

clip = VideoFileClip('InShot_2.mp4')
clip.write_gif('gif_1.gif', fps=5)
print(clip)
print('Done!!')
