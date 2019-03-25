import responder
import os

from typing import (
    Any,
    Dict,
    Tuple
)

ALLOW_ORIGINS = (
    '*',
) 

def get_cors_params () -> Dict[Any, Any]:
    cors_params: Dict[Any, Any] = responder.statics.DEFAULT_CORS_PARAMS.copy()
    cors_params['allow_origins'] = ALLOW_ORIGINS

    return cors_params