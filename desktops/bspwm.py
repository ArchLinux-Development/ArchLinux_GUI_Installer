from typing import List, Optional
from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

class BspwmProfile(XorgProfile):
    def __init__(self):
        super().__init__('Bspwm', ProfileType.DesktopEnv, description='Bspwm Window Manager')

    @property
    def packages(self) -> List[str]:
        return [
            "bspwm",
            "sxhkd",
            "rxvt-unicode",
            "dmenu",
            "thunar"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return None
