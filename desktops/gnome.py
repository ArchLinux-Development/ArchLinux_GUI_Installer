from typing import List, Optional
from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

class GnomeProfile(XorgProfile):
    def __init__(self):
        super().__init__('GNOME', ProfileType.DesktopEnv, description='GNOME Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "gnome",
            "gnome-shell",
            "gnome-terminal",
            "nautilus",
            "gedit",
            "evince",
            "gnome-tweaks"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Gdm
