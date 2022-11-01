import subprocess as subp
from os.path import join
import pyaudio
import wave
import keyboard
import os
import signal
import time
import moviepy.editor as mymovie
import sys
import psutil
from moviemake import movieslap
import os



p = pyaudio.PyAudio()







def record():
	log_dir = 'E:\\VidRecord\\' # путь куда положить файл с записью
	CORE_DIR = 'C:\\' # путь где лежит ffmpeg.exe
	video_file = join(log_dir, 'video.mp4')
	FFMPEG_BIN = join(CORE_DIR, 'ffmpeg\\bin\\ffmpeg.exe')
	


	command = [f"{FFMPEG_BIN}", '-y', '-loglevel', 'error', '-f', 'gdigrab', '-framerate', '12', '-i', 'desktop',  '-s', '1280x1024', '-pix_fmt', 'yuv420p',  '-c:v', 'libx264', '-profile:v', 'main', '-fs', '50M', video_file]

	print("\n|LOG| recording video...\n")





	ffmpeg = subp.Popen(command, stdin=subp.PIPE, stdout=subp.PIPE)
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 600000
	WAVE_OUTPUT_FILENAME = "E:\\VidRecord\\output.wav"
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
		channels=CHANNELS,
		rate=RATE,
		input=True,
		input_device_index=2, 
		frames_per_buffer=CHUNK)



	print("|LOG| recording audio...\n")

	print("PRESS q TO END RECORDING: ")
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		if keyboard.is_pressed('q'):
			break
		data = stream.read(CHUNK)
		frames.append(data)




	ffmpeg.communicate(b'q')
	ffmpeg.stdin.close()

	





	print("|LOG| done recording media\n")
	stream.stop_stream()
	stream.close()
	p.terminate()
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()



	print("|LOG| Start creating clip...")

	time.sleep(3)

	movieslap()


	'''for proc in psutil.process_iter():
		if proc.name() == '':
			proc.terminate()
			print('ok')'''

	
	

	
	#subp.Popen("ffmpeg -i video_result.mp4 -c:v libx265 -c: a copy -flags -i output.wav +global_header video.mp4")

	
	 #монтаж видео
 


	#ffmpeg.stdin.write("q")
	#ffmpeg.stdin.close()



def main():
	input("Press any button to start record: ")
	record()


if __name__ == "__main__":
	main()