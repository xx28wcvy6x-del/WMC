import pyvista as pv
import numpy as np

# ==================================================
# 1. LATTICE SETTINGS
# ==================================================

N = 4

# ==================================================
# 2. CREATE ALL LATTICE POINTS
# ==================================================

points = np.array([
    [x, y, z]
    for x in range(N + 1)
    for y in range(N + 1)
    for z in range(N + 1)
], dtype=float)

# ==================================================
# 3. CONVERT (x, y, z) TO ARRAY INDEX
# ==================================================

def index(x, y, z):
    return x * (N + 1) * (N + 1) + y * (N + 1) + z

# ==================================================
# 4. CREATE LINES BETWEEN NEIGHBORING POINTS
# ==================================================

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

# ==================================================
# 5. CREATE LATTICE MESH
# ==================================================

lattice_mesh = pv.PolyData()

lattice_mesh.points = points
lattice_mesh.lines = lines

# ==================================================
# 6. CREATE PLOTTER
# ==================================================

plotter = pv.Plotter()

# ==================================================
# 7. DRAW LATTICE CONNECTIONS
# ==================================================

plotter.add_mesh(
    lattice_mesh,
    line_width=2
)

# ==================================================
# 8. DRAW LATTICE POINTS
# ==================================================

plotter.add_points(
    points,
    point_size=9,
    render_points_as_spheres=True
)

# ==================================================
# 9. MARK THE ORIGIN
# ==================================================

origin = np.array([
    [0.0, 0.0, 0.0]
])

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

# ==================================================
# 10. CREATE SMALL 4-POINT OBJECT
# ==================================================

# Position of the whole object
object_position = np.array([
    2.0,
    2.0,
    2.0
])

# Shape of the object relative to its own center/origin
local_points = np.array([
    [0.0, 0.0, 0.0],
    [0.35, 0.0, 0.0],
    [0.0, 0.35, 0.0],
    [0.0, 0.0, 0.35]
])

# Keep geometry local and move all actors by the same position.
object_mesh = pv.PolyData(local_points)
connections = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
object_edges = pv.PolyData(local_points)
object_edges.lines = np.array([item for a, b in connections for item in (2, a, b)])

object_actors = [
    plotter.add_points(
        object_mesh, point_size=18, render_points_as_spheres=True,
        color="orange",
    ),
    plotter.add_mesh(object_edges, line_width=4, color="orange"),
]
object_visible = False

# ==================================================
# 11. ADD / REMOVE AND MOVE THE OBJECT
# ==================================================

def update_object():
    """Translate the four dots and their connections together."""
    for actor in object_actors:
        actor.SetPosition(*object_position)
        actor.SetVisibility(object_visible)
    x, y, z = object_position
    state = "Object" if object_visible else "Object hidden"
    plotter.add_text(
        f"{state}: ({x:.2f}, {y:.2f}, {z:.2f})",
        position="upper_right", font_size=12, name="object_position_text",
    )
    plotter.render()


def toggle_object(visible):
    global object_visible
    object_visible = bool(visible)
    update_object()


def move_object(axis, value):
    object_position[axis] = float(value)
    update_object()


plotter.add_text(
    "Check the box to add the object. Drag X / Y / Z to move it.",
    position="upper_left", font_size=11,
)
plotter.add_text("Add / remove object", position=(65, 20), font_size=11)
plotter.add_checkbox_button_widget(
    toggle_object, value=False, position=(15, 15), size=35,
    color_on="orange", color_off="grey",
)

# Limit the anchor so all four dots stay within the 0..4 lattice.
for axis, title in enumerate(("X", "Y", "Z")):
    upper = float(N - local_points[:, axis].max())
    plotter.add_slider_widget(
        lambda value, axis=axis: move_object(axis, value),
        rng=(0.0, upper), value=float(object_position[axis]), title=title,
        pointa=(0.12, 0.24 - axis * 0.07),
        pointb=(0.85, 0.24 - axis * 0.07),
        interaction_event="always", fmt="%.2f",
    )

update_object()
plotter.show_axes()
plotter.show()
