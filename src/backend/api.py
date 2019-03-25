import responder
import uvicorn
import typing
import sys
import os

from typing import (
    cast,
    Any,
    Dict,
    Tuple,
    Optional,
)

from helpers.cors import get_cors_params

api = responder.API(
    cors=True,
    cors_params=get_cors_params()
)

@api.route("/{greeting}")
async def greet_world(req, resp, *, greeting):
    resp.text = f"{greeting}, world!"

@api.route("/api/ping")
async def pong(req, resp):
    response = {
        'running': 'Responder HTTP Service Framework',
        'version': responder.__version__.__version__,
        'python': sys.version
    }
    resp.media = response

if __name__ == '__main__':
    debug = os.getenv('DEBUG')
    if debug:
        port: Optional[int] = int(cast(int, os.getenv('PORT'))) or 8000
        print('-'*80 + '\nWarning: Debug is enabled\nCode Hot Reload enabled\n' + '-'*80)
        uvicorn.run('api:api', host="0.0.0.0", port=port, reload=True)
    else:
        api.run()
