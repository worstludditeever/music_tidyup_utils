# music_tidyup_utils
Utilities I used to tidy up my mess of music files from multiple locations


collate.py walks through all the directories listed in the file, and copies .wma and .mp3 files(leaving the originals) to the collated directory.
As this is a lazy one off utility, directory names are hard coded as variables.

convert.py converts all the music files from .wma to .mp3 if they are not already converted.

purge1.py moves wma files to another directory, while maintaining the directory structure.

purge2.py looks for duplicates of the form "filename 1.mp3" checking whether "filename.mp3" also exists.
          This check will retain "Genesis 1.mp3" from my audio bible for example.
