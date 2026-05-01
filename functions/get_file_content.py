import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path): # errors if not a file or a file within working_dir, otherwise return string(file)
    abs_path_working = os.path.abspath(working_directory)
    abs_path = os.path.normpath(os.path.join(abs_path_working, file_path))
    valid_target_file = os.path.commonpath([abs_path_working, abs_path]) == abs_path_working
    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_path, "r") as fp:
            file_content = fp.read(MAX_CHARS)
            if fp.read(1):
                file_content +=  f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content
    except Exception as e:
        return f"Error: {e}"