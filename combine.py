import os
import math
import glob

import moviepy.editor as mpy



def delete_clips ():
	for file in glob.glob ( os.path.join('clips','clip*.mp4') ):
		os.remove(file)


def stitch_clips (clips):

	video_clips = []

	for i, c in enumerate(clips):
		curr_clip = mpy.VideoFileClip('clips/clip%02d.mp4' % i) 

		w,h = curr_clip.size

		txt_clip1 = ( mpy.TextClip('\"' + c['title'] + '\"',font='Amiri-regular',fontsize=70,color='white')
			.set_duration(5)
			.set_position((10,10))
		)

		txt_clip2 = ( mpy.TextClip(c['broadcaster_name'] ,font='Amiri-regular',fontsize=30,color='white')
			.set_duration(5)
			.set_position((80,100))
		)

		txt_clip = mpy.CompositeVideoClip([txt_clip1, txt_clip2])

		txt_col = txt_clip.on_color(size=(txt_clip.w+20,txt_clip.h+90),
			color=(0,0,0), pos=(10,10), col_opacity=0.6)

		logo = (mpy.ImageClip("twitch_logo.png")
          .set_duration(5)
          .resize(width=70,height=70) # if you need to resize...
          .set_position((10,85)))

		result = mpy.CompositeVideoClip([curr_clip, txt_col, txt_clip2, logo])

		video_clips.append( result )

	# Bug in moviepy=1.0.2 throws error here, so using moviepy=1.0.0
	final_clip = mpy.concatenate_videoclips (video_clips, method='compose') 

	final_clip.write_videofile('final.mp4', fps=60)

	# Remove clip files
	delete_clips ()