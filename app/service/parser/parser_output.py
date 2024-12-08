from argparse import Namespace

from pydantic import BaseModel, ConfigDict


class ParserOutput(BaseModel):
    namespace: Namespace

    model_config = ConfigDict(arbitrary_types_allowed=True)
