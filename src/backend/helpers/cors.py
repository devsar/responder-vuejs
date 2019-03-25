import responder
import os

from typing import (
    Any,
    Dict,
    Tuple
)

ALLOW_ORIGINS: Tuple[str] = (
    'localhost:%s' % os.getenv('PORT') or '8000',
) 

def get_cors_params () -> Dict[Any, Any]:
    allow_origins: Tuple[str] = ('localhost:%s' % os.getenv('PORT') or '8000',)
    cors_params: Dict[Any, Any] = responder.statics.DEFAULT_CORS_PARAMS.copy()
    cors_params.update({'allow_origins': allow_origins})
    return cors_params