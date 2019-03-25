import responder
import uvicorn
import typing
import os

api = responder.API()

@api.route("/{greeting}")
async def greet_world(req, resp, *, greeting):
    resp.text = f"{greeting}, world!"

if __name__ == '__main__':
    debug = os.getenv('DEBUG')
    if debug:
        port: typing.Optional[int] = int(typing.cast(int, os.getenv('PORT'))) or 8000
        print('-'*80 + '\nDebug is enabled\nHot reloading enabled\n' + '-'*80)
        uvicorn.run('api:api', host="0.0.0.0", port=port, reload=True)
    else:
        api.run()
