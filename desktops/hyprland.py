from typing import List, Optional
from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
from mock_archinstall.default_profiles.xorg import XorgProfile

class HyprlandProfile(XorgProfile):
    def __init__(self):
        super().__init__('Hyprland', ProfileType.DesktopEnv, description='Hyprland Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "hyprland",
            "waybar",
            "alacritty",
            "thunar",
            "wofi"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return None
