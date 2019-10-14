from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


def add_z_down(p):
    return p[0], p[1], 0


def add_z_up(p):
    return p[0], p[1], 4


def add_z_mid(p):
    return p[0], p[1], 0


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


def create_arrow(a, b, **kwargs):
    return Arrow3D([a[0], b[0]], [a[1], b[1]], [a[2], b[2]], **kwargs)
