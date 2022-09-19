from curses.ascii import isdigit, isspace
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import csv
import os
import moviepy.editor as mp

# name of output file
naming = 'trim_'
def get_sec(time_str):
    """Get Seconds from time."""
    time = time_str.split(':')
    if(len(time)==3):
        h = time[0]
        m = time[1]
        s = time[2]
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        m = time[0]
        s = time[1]
        return int(m) * 60 + int(s)


# sample = open(sys.argv[0], 'r') 
# csv1 = csv.reader(sample,delimiter='\n')
with open("chapters.txt", 'r', encoding="utf8") as r, open('chapters_new.txt', 'w', encoding="utf8") as o:
    for line in r:
        #strip() function
        if line.strip():
            if line[0].isdigit():
                o.write(line.strip()+"\n")
            elif line[0].isspace():
                while line[0].isspace():
                    line = line[1:]
                if line[0].isdigit():
                    o.write(line.strip()+"\n")
file1 = open('chapters_new.txt', 'r', encoding="utf8")
Lines = file1.readlines()
# print(Lines)
timestamps = []
titles = []
file_name = 'video.mp4'
for eachline in Lines:
    print(eachline)
    timestamp = eachline.split(' ')[0]
    timestamps.append(timestamp)
    length = len((eachline.split(' ')[0]))
    title = eachline[length:].strip()
    titles.append(title)
    print("title is: " + title)
for timestamp in timestamps:
    if timestamps.index(timestamp) != (len(timestamps) - 1):
        start = timestamp
        end = timestamps[timestamps.index(timestamp)+1]
        start = get_sec(start)
        end = get_sec(end)
        out_file = titles[timestamps.index(timestamp)]
        # out_file = './' + out_file + '.mp4'

        # out_file = out_file + '.mp4'
        name, ext = os.path.splitext(file_name)
        # name = timestamps.index(timestamp)
        name = titles[timestamps.index(timestamp)]
        T1 = start
        T2 = end
        index = timestamps.index(timestamp)
        targetname = "%s %s%s" % (index,name, ext)
        print(targetname)
        print(name)
        ffmpeg_extract_subclip(file_name, start, end, targetname=targetname)
        # titles[timestamps.index(timestamp)]
    else:
        start = timestamp
        # end = timestamps[timestamps.index(timestamp)+1]
        start = get_sec(start)
        out_file = str(titles[timestamps.index(timestamp)])
        # out_file = './' + out_file + '.mp4'
        name, ext = os.path.splitext(file_name)
        name = titles[timestamps.index(timestamp)]

        # name = timestamps.index(timestamp)
        duration =  mp.VideoFileClip("video.mp4").duration
        print(duration)
        T1 = start
        T2 = duration
        index = timestamps.index(timestamp)
        targetname = "%s %s%s" % (index,name, ext)

        ffmpeg_extract_subclip(file_name, start, duration, targetname=targetname)

    # # file_name = sys.argv[0]
    # out_file = eachline # naming + file_name
    # start = eachline[1]
    # start = get_sec(start)
    # end = eachline[2]
    # end = get_sec(end)

    #ffmpeg_extract_subclip(file_name, start, end, targetname=out_file)
if os.path.exists("chapters_new.txt"):
  os.remove("chapters_new.txt")