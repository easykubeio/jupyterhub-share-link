from traitlets.config import get_config
import sys


c = get_config()
c.JupyterHub.services = [
    {
        'name': 'share-link',
        'admin': True,
        'url': 'http://127.0.0.1:21211',
        'command': [sys.executable, '-m', 'jupyterhub_share_link.run', 'asdfasdfasd'],
    }
]

c.JupyterHub.allow_named_servers = True
c.Spawner.cmd = ['jupyter-labhub']

c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'


c.Spawner.default_url = '/lab'

# HACK? Workaround. See jupyterhub.handlers.base "don't own".
c.JupyterHub.admin_access = True
