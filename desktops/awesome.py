from typing import List, Optional
from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
from mock_archinstall.default_profiles.xorg import XorgProfile

class AwesomeProfile(XorgProfile):
    def __init__(self):
        super().__init__('Awesome', ProfileType.DesktopEnv, description='Awesome Window Manager')

    @property
    def packages(self) -> List[str]:
        return [
            "awesome",
            "rxvt-unicode",
            "dmenu",
            "thunar"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return None
