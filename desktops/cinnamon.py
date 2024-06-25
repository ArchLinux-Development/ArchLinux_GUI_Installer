from typing import List, Optional
from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

class CinnamonProfile(XorgProfile):
    def __init__(self):
        super().__init__('Cinnamon', ProfileType.DesktopEnv, description='Cinnamon Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "cinnamon",
            "gnome-terminal",
            "nemo",
            "gedit",
            "evince"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Lightdm
