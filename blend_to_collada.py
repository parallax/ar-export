import sys
import bpy

argv = sys.argv
argv = argv[argv.index("--") + 1:]
output = argv[0]

bpy.ops.wm.collada_export(filepath=output, check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', prop_bc_export_ui_section='main', apply_modifiers=True, export_mesh_type=0, export_mesh_type_selection='view', selected=False, include_children=False, include_armatures=False, include_shapekeys=False, deform_bones_only=False, include_animations=True, include_all_actions=True, export_animation_type_selection='sample', sampling_rate=1, keep_smooth_curves=False, keep_keyframes=False, active_uv_only=False, use_texture_copies=True, triangulate=True, use_object_instantiation=True, use_blender_profile=True, sort_by_name=False, export_transformation_type=0, export_transformation_type_selection='matrix', open_sim=False, limit_precision=False, keep_bind_info=False)