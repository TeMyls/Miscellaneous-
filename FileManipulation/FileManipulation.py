import os
from PIL import Image
from moviepy.editor import VideoFileClip,concatenate_videoclips,AudioFileClip,vfx,CompositeAudioClip
import math
import numpy as np
#from numpy import asarray
from moviepy.decorators import apply_to_audio, apply_to_mask, requires_duration
import cv2
#import potrace




def make_folder(folder_name):
    parent_dir = os.getcwd()
    folder_path = os.path.join(parent_dir,folder_name)
    #this makes the folder in the same directory as the script
    os.makedirs(folder_name)
    return folder_name



def convert_mp4_to_jpgs(video_path,folder_path = os.getcwd()):
    video_capture = cv2.VideoCapture(video_path)
    still_reading, image = video_capture.read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"{folder_path}/frame_{frame_count:03d}.png", image)
        
        # read next image
        still_reading, image = video_capture.read()
        frame_count += 1

def convert_to_vector(input_image_path, output_image_path):
    # Read the input image
    image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection to find outlines
    edges = cv2.Canny(gray_image, 100, 200)

    # Find contours (shapes) in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a new blank image to draw the vectorized image
    vector_image = np.zeros_like(image)

    # Draw contours on the blank image to form vectorized shapes
    cv2.drawContours(vector_image, contours, -1, (255, 255, 255), 1)

    # Save the vectorized image
    cv2.imwrite(output_image_path, vector_image)


        
def image_folder_to_gif(folder_path,gif_name_without_filetype,ms_speed):
    #Takes the name of the folder containing the images you wish to convert in the current directory and outputs a gif 
    #in the current directory
    #All the images must be the exact same size
    
    images = []
    for image in os.listdir(folder_path):
        #the exact path to the image in the folder
       
        image_Path = os.path.join(folder_path,image)
        img = Image.open(image_Path)
        images.append(img)
    
    images[0].save(f"{gif_name_without_filetype}.gif",format = "GIF",save_all=True, append_images=images,  duration = ms_speed, loop=0)
    return f"{gif_name_without_filetype}.gif"



def strip_frames_from_gif(gif_filepath,target_folder):
    im = Image.open(gif_filepath)
    key_frame_num = 0
    all_gif_frames = im.n_frames
    #extracting the frames of the gif
   
    choice = input("Do you want a specific frame count? y/n? ")
    if choice.lower() == 'y':
        key_frame_num = int(input("How many frames do you want?\nEnter a number:"))
        for i in range(key_frame_num):
            im.seek(all_gif_frames // key_frame_num * i) 
            im.save(target_folder + f'/frame_{i:03d}.png')
            
            
    if choice.lower() == 'n':
        for i in range(all_gif_frames):
            
            im.seek(i)
            im.save(target_folder + f'/frame_{i:03d}.png')
          
           
            
                
                
    print('Frames Striped')
    
    

def make_transparent(folder_with_no_transparency,folder_with_transparency):
    #making the white background of the gif's images transparent
    tick = 0
    for image in os.listdir(folder_with_no_transparency):
        newImage = []
        image_Path = os.path.join(folder_with_no_transparency,image)
        img = Image.open(image_Path)
        img = img.convert("RGBA")
        for item in img.getdata():
            if item[0] >= 200 and item[1] >= 200 and item[2] >= 200:
                newImage.append((255, 255, 255, 0))
            else:
                newImage.append(item)

        img.putdata(newImage)
        img.save(folder_with_transparency + f'/{tick:03d}.png')
        tick = tick + 1
        
    
    
    print('Transparency Done!')


def make_spritesheet(folder_with_frames,spritesheet_folder,gif):
    #Making into spritesheet
    #Note all images must be of equal sizes
    #This was made with frames of a gif in mind
    
    img_ls = []
    img_2ls = []
    for trimg in os.listdir(folder_with_frames):
        image_Path = os.path.join(folder_with_frames,trimg)
        timg = Image.open(image_Path)
        img_ls.append(timg)
    
    im = Image.open(gif)
    print(f"Rows and Colums multiplied together have to be  {im.n_frames}")
    rows = int(input("How many rows: "))
    cols = int(input("How many columns: "))  
    width = img_ls[0].size[0]
    height = img_ls[0].size[1] 
    new_im = Image.new('RGBA',(cols*width,rows*height))
   
    #print(len(img_2ls))
    cnt = 0
    
    for i in range(cols):
        
        for j in range(rows):
            
            new_im.paste(img_ls[cnt],(j*width,i*height))
            cnt += 1
    new_im.save(spritesheet_folder + f"/ss.png")
    print('Spritesheet made')  
    
    
def make_svg_trace(folder_with_no_trace,folder_with_trace):   
    #couldn't get this to work
    for image in os.listdir(folder_with_no_trace):
        image_Path = os.path.join(folder_with_no_trace,image)
        img = Image.open(image_Path)
        numpydata = np.asarray(img)
        bmp = potrace.Bitmap(numpydata)
        path = bmp.trace()
        for curve in path:
        
            for segment in curve:
                
                end_point_x, end_point_y = segment.end_point
                if segment.is_corner:
                    c_x, c_y = segment.c
                else:
                    c1_x, c1_y = segment.c1
                    c2_x, c2_y = segment.c2
                
def image_folder_to_comic_strip(folder_with_frames,comic_folder):
    #Making into spritesheet
    #Note all images must be of equal sizes
    #This was made with frames of a gif in mind
    
    folder_img_count = 0
    img_ls = []
    img_2ls = []
    
    for trimg in os.listdir(folder_with_frames):
        image_Path = os.path.join(folder_with_frames,trimg)
        timg = Image.open(image_Path)
        img_ls.append(timg)
        folder_img_count += 1
    
    #im = Image.open(gif)
    
    
    choice = input("Vertical(V), Horizontal(H),or Neither(N) Comic? ")
    width = img_ls[0].size[0]
    height = img_ls[0].size[1] 
    filename = input("What will be the file name? ")
    file_ex = input("What will be the file extension? jpg or png? Please enter without the period and lowercase: ")
    new_im = ''
    if choice.upper() == 'H':
        if file_ex == 'png':
            new_im = Image.new('RGBA',((len(img_ls))*width,height))
        elif file_ex == 'jpg' or file_ex == 'jpeg':
            new_im = Image.new('RGB',((len(img_ls))*width,height))
            
        while img_ls:
            new_im.paste(img_ls[len(img_ls) - 1],((len(img_ls) - 1)*width,0))
            img_ls.pop()
        new_im.save(comic_folder + f"/{filename}.{file_ex}")
            
    elif choice.upper() == 'V':
        if file_ex == 'png':
            new_im = Image.new('RGBA',(width,(len(img_ls))*height))
        elif file_ex == 'jpg' or file_ex == 'jpeg':
            new_im = Image.new('RGB',(width,(len(img_ls))*height))
            
        while img_ls:
            new_im.paste(img_ls[len(img_ls) - 1],(0,(len(img_ls) - 1)*height))
            img_ls.pop()
        new_im.save(comic_folder + f"/{filename}.{file_ex}")
    else:
        print(f"Rows and Colums multiplied together have to be  {folder_img_count}")
        rows = int(input("How many rows: "))
        cols = int(input("How many columns: "))  
        if file_ex == 'png':
            new_im = Image.new('RGBA',(cols*width,rows*height))
        elif file_ex == 'jpg' or file_ex == 'jpeg':
            new_im = Image.new('RGB',(cols*width,rows*height))
        #print(len(img_ls)," ",img_ls," ", width," ", height)
        cnt = 0
        cur_row = 0
        cur_col = 0
        while img_ls:
            new_im.paste(img_ls[len(img_ls) - 1],(cur_col*width,cur_row*height))
            if cur_col == cols:
                cur_row += 1
                cur_col = -1
            cur_col += 1
            
            img_ls.pop()
        new_im.save(comic_folder + f"/{filename}.{file_ex}")
        """
        for i in range(cols):
            
            for j in range(rows):
                print(j*width,i*height)
                new_im.paste(img_ls[cnt],(j*height,i*width))
                cnt += 1
        new_im.save(comic_folder + f"/{filename}.{file_ex}")
        """
    print('comic made')  

def mp4_to_gif_old(video_path,new_folder_name,gif_name):
    #makes and entire folder of images
    print("starting\t")
    new_folder_name = make_folder(new_folder_name)
    convert_mp4_to_jpgs(video_path,new_folder_name)
    image_folder_to_gif(new_folder_name,gif_name)
    print("finished\n")

def mp4_to_gif_new(video_path,gif_name_without_filetype,save_folder_without_seperator = ""):
    print("starting\t")
    #new_folder_name = make_folder(new_folder_name)
    #convert_mp4_to_jpgs(video_path,new_folder_name)
    
    video_capture = cv2.VideoCapture(video_path)
    still_reading, image = video_capture.read()
    image_list = []
    while still_reading:
        
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        PIL_image = Image.fromarray(img)
        image_list.append(PIL_image)
        # read next image
        still_reading, image = video_capture.read()
    
    
    if save_folder_without_seperator:
        image_list[0].save(f"{save_folder_without_seperator}/{gif_name_without_filetype}.gif",format = "GIF",save_all=True, append_images=image_list,  duration = 80, loop=0)
    else:
        image_list[0].save(f"{gif_name_without_filetype}.gif",format = "GIF",save_all=True, append_images=image_list,  duration = 80, loop=0)
    #return f"{gif_name_without_filetype}.gif"
    #image_folder_to_gif(new_folder_name,gif_name)
    print("finished\n")
    if save_folder_without_seperator:
        return f"{save_folder_without_seperator}/{gif_name_without_filetype}.gif"
    else:
        return f"{gif_name_without_filetype}.gif"


def gif_to_spritesheet(gif):
    #the gif should be in current dir not in folder
    gif_name = gif.split(".")[0]
    #you have to make empty folders to deposit the frames into
    #making folders
    parent_dir = os.getcwd()
    normal_frames_folder = make_folder(gif_name + '_frames')
    transparent_folder = make_folder(gif_name + '_transparent')
    Spritesheet_folder = make_folder(gif_name + '_spritesheet')
    
    strip_frames_from_gif(gif,normal_frames_folder)
    make_spritesheet(normal_frames_folder,Spritesheet_folder,gif)
    make_transparent(Spritesheet_folder,transparent_folder)
    
    
    
def to_other_img(folder_name_in_directory,from_file_type,to_file_type):
    #Takes the name of the folder containing the webps you wish to convert in the current directory and outputs another folder  
    #filetype being coverted to
    #file_type = input("Which image file type would you like to convert to? Enter without the dot:")
    
    
    #gettingthe current image directory
    parent_dir = os.getcwd()
    #full path of subfolder containing undesired filetype
    folder_name = os.path.join(parent_dir,folder_name_in_directory)
    #name of new folder of images where pngs will be dumped
    new_folder = make_folder(folder_name+ f'_{to_file_type}')
    
  
    cnt = 0
    print('Processing')
    print(folder_name)
    
    for image in os.listdir(folder_name):
        #the exact path to the image in the folder
        image_Path = os.path.join(folder_name,image)
        img = Image.open(image_Path)
        if image.endswith(f'.{from_file_type}'):
            #for webps and jpgs
            img = img.convert('RGB')
            img.save(new_folder+ '\\' + f"{cnt:03d}" + f".{to_file_type}")
        cnt = cnt + 1
    print("done")


#MoviePy Stuff
###########################################################

##Fixing time mirror
@requires_duration
@apply_to_mask
@apply_to_audio
def time_mirror(self):
    """
    Returns a clip that plays the current clip backwards.
    The clip must have its ``duration`` attribute set.
    The same effect is applied to the clip's audio and mask if any.
    """
    duration_per_frame = 1/self.fps
    return self.fl_time(lambda t: np.max(self.duration - t - duration_per_frame, 0), keep_duration=True)

def time_converter(seconds,minutes = 0,hours = 0):
    return seconds + minutes * 60 + hours * 3600
    
"""
The video export failed, possibly because the codec specified for the video (libx264) is not compatible with the given extension (webm). 
Please specify a valid 'codec' argument in write_videofile. 
This would be 'libx264' or 'mpeg4' for mp4, 'libtheora' for ogv, 'libvpx for webm.
Another possible reason is that the audio codec was not compatible with the video codec. For instance the video extensions 'ogv' and 'webm' only allow 'libvorbis' (default) as avideo codec.
"""

def cut_video(video_filepath,start_time_seconds,end_time_seconds,new_video_name_without_extension,save_folder_without_seperator = ""):
    codec_dict = {'mp4':'libx264','ogv':'libtheora','webm':'libvpx'}
    extension = video_filepath.split('.')[1]
    video = VideoFileClip(video_filepath)
    if start_time_seconds == 0 and end_time_seconds == 0:
        return 
    elif end_time_seconds <= start_time_seconds:
        return 
    
    save_videopath = ""
    if save_folder_without_seperator:
        save_videopath = f"{save_folder_without_seperator}/{new_video_name_without_extension}." + extension
    else:
        save_videopath = new_video_name_without_extension + "." + extension
    video_cut = video.subclip(start_time_seconds,end_time_seconds)
    video_cut.write_videofile(save_videopath,codec = codec_dict[extension], bitrate = "800000")
    return save_videopath
    
def to_other_video(video_filepath,new_video_name_without_extension,save_folder_without_seperator = ""):
    video = VideoFileClip(video_filepath)
    extension = input("Which file will the video be changed to \"mp4\",\"webm\" or \"ogv\"? ")
    codec_dict = {'mp4':'libx264','ogv':'libtheora','webm':'libvpx'}
    save_videopath = ""
    if save_folder_without_seperator:
        save_videopath = f"{save_folder_without_seperator}/{new_video_name_without_extension}." + extension
    else:
        save_videopath = new_video_name_without_extension + "." + extension
    video.write_videofile(save_videopath,codec = codec_dict[extension],bitrate = "800000")
    
    return save_videopath
##############################
def resize_video(video_filepath,resize_percent,new_video_name_without_extension,save_folder_without_seperator = ""):
    video = VideoFileClip(video_filepath)
    resize_percent = resize_percent/100
    extension = video_filepath.split('.')[1]
    codec_dict = {'mp4':'libx264','ogv':'libtheora','webm':'libvpx'}
    save_videopath = ""
    if save_folder_without_seperator:
        save_videopath = f"{save_folder_without_seperator}/{new_video_name_without_extension}." + extension
    else:
        save_videopath = new_video_name_without_extension + "." + extension
        
    video = video.resize(resize_percent)
    video.write_videofile(save_videopath,codec = codec_dict[extension],bitrate = "800000")
    
    return save_videopath
    
def combine_videos(array_of_videopaths,new_video_name_without_extension,save_folder_without_seperator = ""):
    videos_list = [VideoFileClip(video) for video in array_of_videopaths]
    concat = concatenate_videoclips(videos_list)
    extension = array_of_videopaths[0].split('.')[1]
    codec_dict = {'mp4':'libx264','ogv':'libtheora','webm':'libvpx'}
    save_videopath = ""
    if save_folder_without_seperator:
        save_videopath = f"{save_folder_without_seperator}/{new_video_name_without_extension}." + extension
    else:
        save_videopath = new_video_name_without_extension + "." + extension
    concat.write_videofile(save_videopath,codec = codec_dict[extension],bitrate = "850000")
    
    return save_videopath
    
def mute_video(video_filepath,new_video_name_without_extension,save_folder_without_seperator = ""):
    codec_dict = {'mp4':'libx264','ogv':'libtheora','webm':'libvpx'}
    extension = video_filepath.split('.')[1]
    video = VideoFileClip(video_filepath,audio=False)
 
    save_videopath = ""
    if save_folder_without_seperator:
        save_videopath = f"{save_folder_without_seperator}/{new_video_name_without_extension}." + extension
    else:
        save_videopath = new_video_name_without_extension + "." + extension
    
    video.write_videofile(save_videopath,codec = codec_dict[extension],bitrate = "850000")
    return save_videopath
    
def crop_video(video_filepath,start_x,start_y,width,height,new_video_name_without_extension,save_folder_without_seperator = ""):
    video = VideoFileClip(video_filepath)
    extension = video_filepath.split('.')[1]
    codec_dict = {'mp4':'libx264','ogv':'libtheora','webm':'libvpx'}
    save_videopath = ""
    if save_folder_without_seperator:
        save_videopath = f"{save_folder_without_seperator}/{new_video_name_without_extension}." + extension
    else:
        save_videopath = new_video_name_without_extension + "." + extension
    new_vid = vfx.crop(video,  x1=start_x , y1=start_y,x2=start_x + width, y2=start_y + height)
    new_vid.write_videofile(save_videopath,codec = codec_dict[extension],bitrate = "800000")
    return save_videopath



def reverse_video(video_filepath,new_video_name_without_extension,save_folder_without_seperator = ""):
    video = VideoFileClip(video_filepath)
    #video = video.set_duration(video.duration)
    new_vid = time_mirror(video)
    extension = video_filepath.split('.')[1]
    codec_dict = {'mp4':'libx264','ogv':'libtheora','webm':'libvpx'}
    save_videopath = ""
    if save_folder_without_seperator:
        save_videopath = f"{save_folder_without_seperator}/{new_video_name_without_extension}." + extension
    else:
        save_videopath = new_video_name_without_extension + "." + extension
    new_vid.write_videofile(save_videopath,codec = codec_dict[extension])
    
    return save_videopath
    
def video_to_gif(video_filepath,new_gif_name_without_extension,save_folder_without_seperator = ""):
    video = VideoFileClip(video_filepath)
    extension = video_filepath.split('.')[1]
    codec_dict = {'mp4':'libx264','ogv':'libtheora','webm':'libvpx'}
    save_videopath = ""
    if save_folder_without_seperator:
        save_videopath = f"{save_folder_without_seperator}/{new_gif_name_without_extension}." + "gif"
    else:
        save_videopath = new_gif_name_without_extension + "." + "gif"
    video.write_gif(save_videopath)
    
    return save_videopath

def gif_to_video(gif_filepath,new_video_name_without_extension,save_folder_without_seperator = ""):
    gif = VideoFileClip(gif_filepath)
    extension = input("Which file will the gif be changed to \"mp4\",\"webm\" or \"ogv\"? ")
    codec_dict = {'mp4':'libx264','ogv':'libtheora','webm':'libvpx'}
   
    save_videopath = ""
    if save_folder_without_seperator:
        save_videopath = f"{save_folder_without_seperator}/{new_video_name_without_extension}." + extension
    else:
        save_videopath = new_video_name_without_extension + "." + extension
    gif.write_videofile(save_videopath, codec = codec_dict[extension])
    
    return save_videopath





# Sample input and output file paths
#input_image_path = "path/to/your/input/image.jpg"
#output_image_path = "path/to/your/output/vector_image.svg"
# Call the function to convert the image to vectors/
#convert_to_vector(input_image_path , output_image_path)