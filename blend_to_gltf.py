import sys
import bpy

argv = sys.argv
argv = argv[argv.index("--") + 1:]
output = argv[0]

bpy.ops.export_scene.gltf(export_format='GLTF_EMBEDDED', ui_tab='GENERAL', export_copyright='', export_texcoords=True, export_normals=True, export_tangents=False, export_materials=True, export_colors=True, export_cameras=False, export_selected=False, export_extras=False, export_yup=True, export_apply=False, export_animations=False, export_frame_range=False, export_frame_step=1, export_move_keyframes=False, export_force_sampling=False, export_current_frame=False, export_skins=False, export_bake_skins=False, export_all_influences=False, export_morph=False, export_morph_normal=False, export_morph_tangent=False, export_lights=False, export_texture_transform=False, export_displacement=False, will_save_settings=False, filepath=output, check_existing=False, filter_glob='*.glb;*.gltf')