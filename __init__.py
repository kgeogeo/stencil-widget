bl_info = {
    "name": "Stencil_Widget",
    "description": "Show a widget to control the stencil brush",
    "author": "kgeogeo",
    "version": (1, 0),
    "blender": (2, 6, 6),
    "category": "Paint"}

import bpy
from . import Stencil_Widget

def register():    
    bpy.utils.register_module(__name__)
    km_list = ['Image Paint', 'Sculpt', 'Vertex Paint']
    for i in km_list:
        km = bpy.context.window_manager.keyconfigs.default.keymaps[i]
        kmi = km.keymap_items.new("brush.stencil_widget", 'Q', 'PRESS')

def unregister():
    bpy.utils.unregister_module(__name__)
    km_list = ['Image Paint', 'Sculpt', 'Vertex Paint']
    for i in km_list:
        km = bpy.context.window_manager.keyconfigs.default.keymaps[i]
        for kmi in (kmi for kmi in km.keymap_items if kmi.idname in {"brush.stencil_widget", }):
            km.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()
