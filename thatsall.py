import cv2
import moviepy.editor as mp
import numpy as np 
text = "That's all folks !! LinkedIn : thekartikeyamishra"
font_scale = 1
font_thickness = 2
font_face = cv2.FONT_HERSHEY_SIMPLEX

video_width = 1280
video_height = 720
fps = 24

background_image = np.zeros((video_height, video_width, 3), dtype="uint8")
background_image[:] = (255, 255, 255)  

def animate_text(frame, i):
  text_size, _ = cv2.getTextSize(text, font_face, font_scale, font_thickness)
  text_x = int((video_width - text_size[0]) / 2)
  text_y = int((video_height + text_size[1]) / 2)
  new_scale = font_scale * (1 + i / fps)  # Increase scale over time
  cv2.putText(frame, text, (text_x, text_y), font_face, new_scale, (0, 0, 255), font_thickness)

# Generate video frames
frames = []
for i in range(fps * 2):  # Create 2 seconds of video
  frame = background_image.copy()
  animate_text(frame, i)
  frames.append(frame)

clip = mp.ImageSequenceClip(frames, fps=fps)

clip.write_videofile("fancy_text.mp4")

print("Video generation complete!")
