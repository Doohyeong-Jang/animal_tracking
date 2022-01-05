# if python-ffmpeg is installed, it might makes issues
# pip install ffmpeg-python
import ffmpeg
import os
# put the path and original format inlcuding '.' for clarification
path = "D:/BHT/apple/ffmpeg-4.3.1-2020-11-19-full_build/bin"
original_format = ".mp4"

def convert_video(raw_video, frame_rate=30, format='avi'):
    try:
        # put the files in the variable "stream"
        stream = ffmpeg.input(raw_video)
            
        # see the header 
        print(ffmpeg.probe(raw_video))
        
        # define the format of ouput using input....
        stream = ffmpeg.output(stream, raw_video[:-4]+"_converted.avi",  vcodec='rawvideo', pix_fmt = 'nv12', 
                                    format = format, framerate =frame_rate)    
        
        # process the videos
        ffmpeg.run(stream, capture_stdout=True, capture_stderr=True)
    
    # errors raising 
    except ffmpeg.Error as e:
        print('stdout:', e.stdout.decode('utf8'))
        print('stderr:', e.stderr.decode('utf8'))
        raise e        


os.chdir(path)

# show the file list in the paths
file_list = os.listdir(path)
print(file_list)

# inspect every files
for i in file_list:
    
    # target the typical files that end with mp4
    if i.endswith(original_format) == True:
        convert_video(i, frame_rate=30, format='avi')
        
# hello

# what is 
print("this is for the test")

print("test2")