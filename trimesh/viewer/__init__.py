"""
viewer
-------------

View meshes and scenes via pyglet or inline HTML.
"""


def _cloture(exc):
    """
    Return a function which will accept any arguments
    but raise the exception when called.

    Parameters
    ------------
    exc : Exception
      Will be raised later

    Returns
    -------------
    failed : function
      When called will raise `exc`
    """
    # scoping will save exception
    def failed(*args, **kwargs):
        raise exc
    return failed


# try importing windowed which will fail
# if we can't create an openGL context
try:
    from .windowed import (SceneViewer,
                           render_scene)
except BaseException as E:
    # if windowed failed to import only raise
    # the exception if someone tries to use them
    SceneViewer = _cloture(E)
    render_scene = _cloture(E)


# this is only standard library imports
from .notebook import (in_notebook,
                       scene_to_notebook,
                       scene_to_html)

# explicitly list imports in __all__
# as otherwise flake8 gets mad
__all__ = [SceneViewer,
           render_scene,
           in_notebook,
           scene_to_notebook,
           scene_to_html]
