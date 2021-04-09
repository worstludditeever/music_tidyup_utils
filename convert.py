'''
Requires installation of ffmpeg added to PATH.
Also installing the python library ffmpeg

'''
from pydub import AudioSegment
import os, shutil


music = "Z:\\Music"

problems = []

print(music)
start_len = len(music)
for root, dirs, files in os.walk(music):
    print(root) # Progress shown by directory
    for name in files:      # walk over the directory and file
                
        source = os.path.join(root, name)
            #source of the music file
        file_type = source[-3:]
            
        if(file_type=='wma'):
            print(source)
            dest_mp3 = source[:-3]+"mp3"
            if(not(os.path.isfile(dest_mp3))):
                try:
                    #convert
                    print('Converting: '+ source) 
                    song = AudioSegment.from_file(source.replace("\\", "/"))
                    song.export(dest_mp3, format='mp3')

                except Exception as e:
                    problems.append(source)
                    print(e)
                


print(problems)
        
          
                
 
