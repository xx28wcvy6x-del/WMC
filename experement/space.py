import pyvista as pv
import numpy as np

# -----------------------------------
# Size of the lattice
# -----------------------------------

N = 4

# -----------------------------------
# Create all points
# -----------------------------------

points = np.array([
    [x, y, z]
    for x in range(N + 1)
    for y in range(N + 1)
    for z in range(N + 1)
], dtype=float)

# -----------------------------------
# Convert (x, y, z) to point index
# -----------------------------------

def index(x, y, z):
    return x * (N + 1) * (N + 1) + y * (N + 1) + z

# -----------------------------------
# Create connections between
# neighboring points
# -----------------------------------

lines = []

for x in range(N + 1):
    for y in range(N + 1):
        for z in range(N + 1):

            current = index(x, y, z)

            # Neighbor in x-direction
            if x < N:
                neighbor = index(x + 1, y, z)
                lines.extend([2, current, neighbor])

            # Neighbor in y-direction
            if y < N:
                neighbor = index(x, y + 1, z)
                lines.extend([2, current, neighbor])

            # Neighbor in z-direction
            if z < N:
                neighbor = index(x, y, z + 1)
                lines.extend([2, current, neighbor])

lines = np.array(lines)

# -----------------------------------
# Create one mesh containing
# all the lines
# -----------------------------------

mesh = pv.PolyData()
mesh.points = points
mesh.lines = lines

# -----------------------------------
# Create the plot
# -----------------------------------

plotter = pv.Plotter()

# Draw connections
plotter.add_mesh(
    mesh,
    line_width=2
)

# Draw points
plotter.add_points(
    points,
    point_size=10,
    render_points_as_spheres=True
)

# -----------------------------------
# Highlight the origin
# -----------------------------------

origin = np.array([[0.0, 0.0, 0.0]])

plotter.add_points(
    origin,
    point_size=20,
    render_points_as_spheres=True
)

plotter.add_point_labels(
    origin,
    ["O = (0,0,0)"],
    font_size=14
)

# -----------------------------------
# Highlight some example points
# -----------------------------------

special_points = np.array([
    [1.0, 1.0, 1.0],
    [4.0, 4.0, 4.0]
])

plotter.add_points(
    special_points,
    point_size=18,
    render_points_as_spheres=True
)

plotter.add_point_labels(
    special_points,
    [
        "P = (1,1,1)",
        "Q = (4,4,4)"
    ],
    font_size=14
)

# -----------------------------------
# Show orientation axes
# -----------------------------------

plotter.show_axes()

# -----------------------------------
# Open interactive 3D window
# -----------------------------------

plotter.show()