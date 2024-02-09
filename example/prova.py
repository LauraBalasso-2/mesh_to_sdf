from mesh_to_sdf import scale_to_unit_sphere, create_from_scans, create_from_mesh
import trimesh
import open3d as o3d
import numpy as np
import os

os.environ['PYOPENGL_PLATFORM'] = 'egl'
import sys

sys.path.append('/home/laura/source/mesh2sdf/')
from npz_to_vtu import save_vtu

mesh = trimesh.load(
    '/home/fausto/Desktop/DrivaerMimic/AngelaCars/Results_lhs_2inputs/body00000/DrivAER_DEFORMED_noWheels.stl')
mesh = scale_to_unit_sphere(mesh)

# mesh.export('/home/laura/rescaled_body00000_2.stl')

if isinstance(mesh, trimesh.Scene):
    mesh = mesh.dump().sum()
if not isinstance(mesh, trimesh.Trimesh):
    raise TypeError("The mesh parameter must be a trimesh mesh.")

# points = mesh.sample(10000000, return_index=False)
# reconstruction_ply = '/home/laura/exclude_backup/pycharm_projects_deployment/MeshSDF/experiments/drivaer/2_var_no_wheel/third_run/Reconstructions/body00000.ply'

# pcd = o3d.io.read_point_cloud(reconstruction_ply)  # Read the point cloud

# Convert open3d format to numpy array
# Here, you have the point cloud in numpy format. 


# point_cloud = np.asarray(pcd.points)
# translation_matrix = np.ones_like(point_cloud)
# point_cloud = point_cloud - translation_matrix

spc = create_from_mesh(mesh)
n_surface_points = spc.points.shape[0]
query_points, sdf = spc.sample_sdf_near_surface(use_centers=True)
# sdf = spc.get_sdf(point_cloud)

save_dir = '/home/laura/exclude_backup/drivaer/2_var_no_wheel/sdf_samples_from_mesh_centers/vtu'

data = {}
data['sdf'] = np.ascontiguousarray(-sdf)
data['x'] = np.ascontiguousarray(query_points[:, 0])
data['y'] = np.ascontiguousarray(query_points[:, 1])
data['z'] = np.ascontiguousarray(query_points[:, 2])

file_name = os.path.join(save_dir, 'body00000')

save_vtu(file_name, data)
