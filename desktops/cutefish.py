from typing import List, Optional
from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
from mock_archinstall.default_profiles.xorg import XorgProfile

class CutefishProfile(XorgProfile):
    def __init__(self):
        super().__init__('Cutefish', ProfileType.DesktopEnv, description='Cutefish Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "cutefish-core",
            "cutefish-qt-plugins",
            "cutefish-settings"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Lightdm
