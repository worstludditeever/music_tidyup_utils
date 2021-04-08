import os
import shutil

    # TODO: change the list of directories to whatever places you have your files
    # stored at the moment.
music_locs = [
              "Z:\Shared drive\Music",
              "Z:\Shared drive\Music - Copy"]

destination = "Z:\Music2" # TODO: set the root location for the collated collection

''' for root, dir, files in os.walk(directory):
        for name in files:
#            print(os.path.join(root, name))
'''


for directory in music_locs:
    print(directory)
    start_len = len(directory) # calculate once per directory
    for root, dirs, files in os.walk(directory):
        print(root)
        for name in files:      # walk over the directory and file
            try:
                os.makedirs(destination+root[start_len:])
            except OSError:
                pass # avoids program exit if the directory already exists
            else:
                pass
                
            source = os.path.join(root, name) #source of the music file
            
            file_type = source[-3:]
            dest = destination+source[start_len:]
            # dest is the compiled destination maintaining directory and album structure
            if(file_type=='wma' or file_type=='mp3'): # TODO: change if other formats to be included
 #               print(source)
                    # On windows I had the \\ is replaced with / - incompatibiltiy in path names
                    # otherwise.
                shutil.copy2(source.replace("\\", "/"), dest.replace("\\", "/"))

            
            #currently copying both .mp3 and .wav files
                


