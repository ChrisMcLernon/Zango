from pydantic import BaseModel
import requests
import json
import os
from typing import List

from .base_fields import FieldBase

from zango.codeassist import URL


class FormField(FieldBase):
    pass


class FormMeta(BaseModel):
    model: str
    title: str
    order: List[str]


class Form(BaseModel):
    name: str
    fields: List[FormField]
    meta: FormMeta

    def apply(self, tenant, module):
        resp = requests.post(
            f"{URL}/generate-form",
            json=json.loads(self.model_dump_json()),
        )
        with open(os.path.join("workspaces", tenant, module, "forms.py"), "a+") as f:
            f.write(resp.json()["content"])
            f.write("\n\n")