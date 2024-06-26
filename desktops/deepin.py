from typing import List, Optional
from mock_archinstall.default_profiles.profile import ProfileType, GreeterType
from mock_archinstall.default_profiles.xorg import XorgProfile

class DeepinProfile(XorgProfile):
    def __init__(self):
        super().__init__('Deepin', ProfileType.DesktopEnv, description='Deepin Desktop Environment')

    @property
    def packages(self) -> List[str]:
        return [
            "deepin",
            "deepin-terminal",
            "deepin-file-manager",
            "deepin-text-editor",
            "deepin-image-viewer"
        ]

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return GreeterType.Lightdm
