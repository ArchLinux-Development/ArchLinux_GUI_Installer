from typing import List, Optional
from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

class EnlightenmentProfile(XorgProfile):
    def __init__(self):
        super().__init__('Enlightenment', ProfileType.DesktopEnv, description='Enlightenment Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "enlightenment",
            "terminology",
            "econnman"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Lightdm
