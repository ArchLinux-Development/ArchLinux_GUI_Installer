from typing import List, Optional
from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
from mock_archinstall.default_profiles.xorg import XorgProfile

class QtileProfile(XorgProfile):
    def __init__(self):
        super().__init__('Qtile', ProfileType.DesktopEnv, description='Qtile Window Manager')

    @property
    def packages(self) -> List[str]:
        return [
            "qtile",
            "alacritty",
            "dmenu",
            "thunar"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return None
