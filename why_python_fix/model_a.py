from typing import Optional
from pydantic import BaseModel


class ModelA(BaseModel):
    a: Optional["ModelA"]
    b: Optional["ModelB"]

    @classmethod
    def from_dict(cls, obj: dict) -> "ModelA":
        return ModelA.parse_obj(
            {
                "a": ModelA.from_dict(obj.get("a")) if obj.get("a") else None,
                "b": ModelB.from_dict(obj.get("b")) if obj.get("b") else None,
            }
        )


from model_b import ModelB

ModelA.update_forward_refs()
