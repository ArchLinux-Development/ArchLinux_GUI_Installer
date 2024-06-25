from typing import List, Optional
from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

class LxqtProfile(XorgProfile):
    def __init__(self):
        super().__init__('LXQt', ProfileType.DesktopEnv, description='LXQt Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "lxqt",
            "qterminal",
            "pcmanfm-qt",
            "featherpad",
            "lximage-qt"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Sddm
