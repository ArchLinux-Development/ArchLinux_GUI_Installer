from typing import List, Optional
from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

class PlasmaProfile(XorgProfile):
    def __init__(self):
        super().__init__('KDE Plasma', ProfileType.DesktopEnv, description='KDE Plasma Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "plasma-meta",
            "konsole",
            "kwrite",
            "dolphin",
            "ark",
            "plasma-workspace",
            "egl-wayland"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Sddm
