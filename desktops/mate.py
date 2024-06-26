from typing import List, Optional
from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
from mock_archinstall.default_profiles.xorg import XorgProfile

class MateProfile(XorgProfile):
    def __init__(self):
        super().__init__('MATE', ProfileType.DesktopEnv, description='MATE Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "mate",
            "mate-extra",
            "mate-terminal",
            "caja",
            "pluma",
            "atril"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Lightdm
