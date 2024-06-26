from typing import List, Optional
from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
from mock_archinstall.default_profiles.xorg import XorgProfile

class SwayProfile(XorgProfile):
    def __init__(self):
        super().__init__('Sway', ProfileType.DesktopEnv, description='Sway Window Manager')

    @property
    def packages(self) -> List[str]:
        return [
            "sway",
            "alacritty",
            "thunar",
            "wofi"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return None
