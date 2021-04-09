'''
Many of my files have acquired duplicates of the form "name 1.mp3 in addition to
"name.mp3"'''
import os, shutil, os.path


music = "Z:\\Music"
dest_1 = "z:\\Music_1"
problems = []

print(music)
start_len = len(music)
for root, dirs, files in os.walk(music):
    print(root) # Progress shown by directory
    for name in files:      # walk over the directory and file
        source = os.path.join(root, name)
            #source of the music file
        dup_chk = source[-6:-4] # characters before extension
            
        if(dup_chk==' 1'):
 #           print(source)
            orig = source[:-6]+".mp3" 

            
            if(os.path.isfile(orig)): # check for actual duplicate, rather than
                                        # title Genesis 1 (for example)
#                print(source)
                dest = dest_1+source[start_len:]
 #               print(dest)

                try:
                    os.makedirs(dest_1+root[start_len:])
                except OSError:
                    pass # avoids program exit if the directory already exists
                else:
                    pass


                
                shutil.move(source.replace("\\", "/"), dest.replace("\\", "/"))
                    
            else:
                 problems.append(source)



print(problems)  
                
 
