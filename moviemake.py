import moviepy.editor as mymovie
from pydub import AudioSegment 
from pydub.playback import play 
 




def movieslap():
	input_video = "E:\\VidRecord\\video.mp4"
	input_audio = "E:\\VidRecord\\output.wav"
	
	output_video = "E:\\VidRecord\\result.mp4"


	video_clip = mymovie.VideoFileClip(input_video)
	audio_clip = mymovie.AudioFileClip(input_audio)
	
	final_clip = video_clip.set_audio(audio_clip)
	final_clip.write_videofile(output_video, fps = 60)
	sound_audio = AudioSegment.from_wav('dojyaaan.wav') 
	play(sound_audio)