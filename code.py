from app import *
from adafruit_hid.keycode import Keycode



AppContainer(
    Screen("Hello World", [
        Key(0,[Keycode.RETURN]),
        Key(1,Goto("press google button"))
    ]),
    Screen("press google button",[
        Key(0,[(Keycode.WINDOWS,Keycode.R),Pause(0.5),"www.google.dk", Pause(0.5),Keycode.ENTER]).with_animation(RainbowWave().loop())])
).run()

