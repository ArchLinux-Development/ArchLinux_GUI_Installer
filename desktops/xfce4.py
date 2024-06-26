from typing import List, Optional
from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
from mock_archinstall.default_profiles.xorg import XorgProfile

class XfceProfile(XorgProfile):
    def __init__(self):
        super().__init__('XFCE', ProfileType.DesktopEnv, description='XFCE Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "xfce4",
            "xfce4-goodies",
            "xfce4-terminal",
            "thunar",
            "mousepad",
            "ristretto"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Lightdm
