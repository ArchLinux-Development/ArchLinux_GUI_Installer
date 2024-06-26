from typing import List, Optional
from .profile import ProfileType, GreeterType

class XorgProfile:
    def __init__(self, name: str, profile_type: ProfileType, description: str):
        self.name = name
        self.profile_type = profile_type
        self.description = description

    @property
    def packages(self) -> List[str]:
        return []

    @property
    def default_greeter_type(self) -> Optional[GreeterType]:
        return None
