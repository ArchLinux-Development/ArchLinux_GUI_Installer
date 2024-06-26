from enum import Enum

class ProfileType(Enum):
    DesktopEnv = "Desktop Environment"

class GreeterType(Enum):
    Sddm = "SDDM"
    Lightdm = "LightDM"
    Gdm = "GDM"
