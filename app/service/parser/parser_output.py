from argparse import Namespace

from pydantic import BaseModel, ConfigDict


class ParserOutput(BaseModel):
    namespace: Namespace
    help_message: str

    model_config = ConfigDict(arbitrary_types_allowed=True)
