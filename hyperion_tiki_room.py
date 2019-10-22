import numpy as np
import time, socket, os, pygame

# Other effects in..
# /usr/share/hyperion/effects
os.system("hyperion-remote --effect 'UDP listener'")

UDP_IP = "192.168.1.169" #"127.0.0.1" #localhost or ip of device (192.168.1.169)
UDP_PORT = 2391
MESSAGE = "Sending data using UDP to Lightpack!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#3,4,5,2,1,6,7,8,9,10

# INITIALIZE PYGAME MUSIC
pygame.mixer.init()
# pygame.mixer.music.load("two_track_stereo_Jose.mp3")
pygame.mixer.music.load("tiki_room_audio_short.mp3")

# assign the location for birds
Michael = [0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Jose = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,0,0,0,0,0,0,0,0]
Pierre = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255]
Fritz = [0,0,0,0,0,0,0,0,0,0,0,0,255,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
clear = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
roof_white = [0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0]
middle_green = [0,0,0,0,0,0,0,0,0,255,150,255,0,0,0,0,0,0,0,0,0,0,0,0,255,150,255,0,0,0]
bottom_red = [0,0,0,0,0,0, 0,0,0,0,0,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,0,0]
top_blue = [0,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,0,0,0,0,0,0]
rlist = [255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255]

# rlist = [0,0,255,
#             0,0,0,
#             0,0,0,
#             0,0,0,
#             0,0,0,
#             0,0,0,
#             0,0,0,
#             0,0,255,
#             0,0,0,
#             0,0,0]

def sing(bird, time_df):
   sock.sendto(bytes(bird), (UDP_IP, 2391))
   time.sleep(time_df)

def whistle(time_df):
    t_end = time.time() + time_df - 0.2
    while time.time() < t_end:
      for k in range(0,10):
         sing(roof_white, 0.1)
         sing(clear, 0.1)

def alltogether(time_df):
   rList = 255*np.random.rand(10,3)
   t_end = time.time() + time_df
   while time.time() < t_end:
      rList = 255*np.random.rand(10,3)
      sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
      sock.sendto(bytes(rList), (UDP_IP, 2391))
      time.sleep(0.25)

def swing(time_df):
   t_end = time.time() + time_df - 0.65
   while time.time() < t_end:
      sing(roof_white, .15)
      sing(middle_green, .15)

def finale():
   sing(bottom_red, 0.25)
   sing(middle_green, 0.32)
   sing(top_blue, 0.31)
   sing(roof_white, 0.9)

# START PLAYING BACKGROUND MUSIC
pygame.mixer.music.play()

# while pygame.mixer.music.get_busy():
   # BEGIN SINGING SEQUENCE
sing(clear, 0.5)
sing(Jose, 14.2)
sing(Michael, 8.5)
sing(Pierre, 10.2)
sing(Fritz, 13.8)
sing(Michael, 3.9)

whistle(2.1)

sing(Jose, 3.3)

alltogether(5.1)

sing(Jose, 0.8)
sing(Pierre, 2.1)

alltogether(2.8)

sing(Jose, 9.8) # Welcome to our tropical hideaway

alltogether(6) # ALLTOGETHER!

sing(Jose, 1.3)
sing(Pierre, 1.3)

alltogether(2.8)

sing(Michael, 4) # I sing so beautifully, I should sing solo
sing(Jose, 2.4)
sing(Pierre, 4.8)
sing(Fritz, 8.6)
sing(Jose, 6.5)
sing(Pierre, 2.7) # because of their claws?
sing(Jose, 1.1)
sing(Pierre, 7)

swing(5)

sing(Jose, 10.7)
alltogether(5.2)
sing(Jose, 1.4)
sing(Pierre, 1.4)

alltogether(2.6)

sing(Michael, 10.7)

alltogether(5.2)

sing(Jose, 1.4)
sing(Pierre, 1.4)

alltogether(2.7)

sing(Jose, 10.7) # All my magnificent produc-ti-on is yet to come

# recalculate the timings
alltogether(5.1)
sing(Michael, 0.6)
alltogether(4.7)
sing(Michael, 1)
alltogether(9.8) #

finale()

sing(Michael, 2.8)
sing(Jose, 1.5)
sing(Pierre, 3.9)
sing(Jose, 4)
sing(clear, 1)


#Turn off all LEDs
#hyperion-remote --clear
