import arcade
import time

testNoise = arcade.sound.load_sound(".\\CoconutMall.mp3")
arcade.play_sound(testNoise)

while testNoise:
    time.sleep(1)