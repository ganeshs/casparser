import datetime
import decimal
import json
from typing import Any

from .enums import TransactionType


class CASDataEncoder(json.JSONEncoder):
    """CAS Data encoder class for json output."""

    def default(self, o: Any) -> Any:
        """Encode custom datatype to json format."""
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, datetime.date):
            return o.isoformat()
        if isinstance(o, TransactionType):
            return o.name
        return super().default(o)
