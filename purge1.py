'''
move duplicate wma files
'''
import os, shutil


music = "Z:\\Music"
wma_dest = "z:\\wma_music"
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
            dest = wma_dest+source[start_len:]
            print(dest)

            try:
                os.makedirs(wma_dest+root[start_len:])
            except OSError:
                pass # avoids program exit if the directory already exists

            shutil.move(source.replace("\\", "/"), dest.replace("\\", "/"))


        
          
                
 
