from invoke import task
from pelican.server import ComplexHTTPRequestHandler
import os
import shutil
import sys
import socketserver

# Local path configuration (can be absolute or relative to fabfile)
DEPLOY_PATH = 'public'

# Port for `serve`
PORT = 8000

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)
@task
def build(c):
    """Build local version of site"""
    # TODO Download pelican-themes if needed
    # TODO Download Flex theme if needed
    c.run('pelican -s pelicanconf.py')

@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run('pelican -d -s pelicanconf.py')

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run('pelican -r -s pelicanconf.py')

@task
def serve(c):
    """Serve site at http://localhost:8000/"""
    os.chdir(DEPLOY_PATH)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)

@task
def preview(c):
    """Build production version of site"""
    c.run('pelican -s publishconf.py')
