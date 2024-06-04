import json
import requests
from typing import List
from pydantic import BaseModel

from zango.codeassist import URL, TENANT_URL


class Child(BaseModel):
    url: str
    name: str
    icon: str | None = None


class MenuItem(BaseModel):
    url: str = ""
    icon: str | None = None
    name: str
    children: List[Child] | None = None


class Color(BaseModel):
    accent: str = "#DDE2E5"
    header: str = "#FFFFFF"
    primary: str = "#DDE2E5"
    sidebar: str = "#E1D6AE"
    secondary: str = "#E1D6AE"
    background: str = "#FFFFFF"
    typography: str = "#212429"
    headerBorder: str = "#DDE2E5"


class ConfigItem(BaseModel):
    color: Color = Color()


class Frame(BaseModel):
    role: str
    menu: List[MenuItem]
    config: ConfigItem = ConfigItem()
    login_url: str | None = None
    display_edit_profile: bool = True
    allow_change_password: bool = True
    display_change_password: bool = True

    def apply(self):
        try:
            from zango.apps.appauth.models import UserRoleModel

            user_role = UserRoleModel.objects.get(name=self.role)
            config = json.loads(self.model_dump_json())
            del config["role"]
            requests.post(
                f"{TENANT_URL}/frame/configure/orm/",
                data={
                    "user_role_id": user_role.pk,
                    "config": config,
                },
                headers={"Content-Type": "application/json"},
            )
        except Exception as e:
            print(e)
