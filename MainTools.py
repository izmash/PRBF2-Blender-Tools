import bpy

"""Blender addon information"""
bl_info = {
    "name": "PRBF2 Tools",
    "author": "Izmash",
    "version": (0, 1),
    "location": "3D Viewport > Sidebar > PRBF2 Tools",
    "description": "Set of usefull tools to speed up making model for Project Reality BF2 modification",
}


"""Function that removes all uv maps"""
def remove_uv_layers():
    for obj in bpy.context.selected_objects: #for every selected object
        for uv in obj.data.uv_layers: #for every uv map that object have
            obj.data.uv_layers.remove(obj.data.uv_layers[0]) #remove first uv map (like in heap)
            print("UV layer removed!")


"""Function that add new set of proper uvs"""
uv_prefix = 'UVChannel_' #Literal for uv map prefix
def add_new_uv_set():
    for obj in bpy.context.selected_objects: #For every selected object
        for i in range (1, 6): #For 5 times
            temp_sufix = str(i) #Make i string
            obj.data.uv_layers.new(name = uv_prefix + temp_sufix, do_init = True) #Add new uv map with proper name
            print("UV Layer added!")


"""Operator for deleting old and creating new set of uv maps"""
class set_up_uv_layout(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.set_up_uv_layout"
    bl_label = "Set up object uv layout"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        remove_uv_layers()
        add_new_uv_set()
        return {'FINISHED'}
   


"""Main panel class for miscellaneous PRBF2 Tools"""
class pt_prbf2_tools(bpy.types.Panel):  

    #Naming
    bl_idname = "OBJECT_PT_PRBF2_Tools" #Indentyfier name
    bl_label = "PRBF2 Tools" #Panel label
    
    #Panel position
    bl_space_type = 'VIEW_3D' #VIEW_3D spacetype (3D Viewport where meshes are)
    bl_region_type = 'UI' #UI region type (Sidebar)
    bl_category = 'PRBF2 Tools' #New category for this panel

    #Additional options
    bl_description = "Set of usefull tools to speed up making model for Project Reality BF2 modification"
    
    @classmethod
    #Default class methods
    def poll(cls, context):
        return (context.object is not None)
        
    def draw(self, context):
        layout = self.layout
        
        layout.label(text="UV Tools")

        row = self.layout.row()
        row.operator(set_up_uv_layout.bl_idname, text = set_up_uv_layout.bl_label)


#Register and unregister classes
def register():
    bpy.utils.register_class(pt_prbf2_tools)
    bpy.utils.register_class(set_up_uv_layout)
    
def unregister():
    bpy.utils.unregister_class(pt_prbf2_tools)
    bpy.utils.unregister_class(set_up_uv_layout)

if __name__ == "__main__":
    register()