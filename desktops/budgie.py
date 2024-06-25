from typing import List, Optional
from archinstall.default_profiles.profile import ProfileType, GreeterType
from archinstall.default_profiles.xorg import XorgProfile

class BudgieProfile(XorgProfile):
    def __init__(self):
        super().__init__('Budgie', ProfileType.DesktopEnv, description='Budgie Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "budgie-desktop",
            "tilix",
            "nautilus",
            "gedit",
            "evince"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Gdm
