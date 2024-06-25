from typing import List, Optional
from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

class I3Profile(XorgProfile):
    def __init__(self):
        super().__init__('i3', ProfileType.DesktopEnv, description='i3 Window Manager')

    @property
    def packages(self) -> List[str]:
        return [
            "i3-wm",
            "i3status",
            "i3lock",
            "dmenu",
            "xfce4-terminal",
            "thunar"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return None
