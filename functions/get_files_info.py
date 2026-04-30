import os


def get_files_info(working_directory, directory="."): # accept a dir (working_dir), return a string(contents of directory)
    
    abspath_working = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abspath_working, directory))
    valid_target_dir = os.path.commonpath([abspath_working, target_dir]) == abspath_working
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        items_within = []
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            item_size = os.path.getsize(item_path)
            item_dir = os.path.isdir(item_path)
            items_within.append(f"- {item}: file_size={item_size} bytes, is_dir={item_dir}")
        return "\n".join(items_within)
    except Exception as e:
        return f"Error: {e}"

        
        

    
