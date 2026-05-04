import os
from config import MAX_CHARS
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_path_working = os.path.abspath(working_directory)
    abs_path = os.path.normpath(os.path.join(abs_path_working, file_path))
    parent_dir = os.path.dirname(abs_path)
    valid_target_file = os.path.commonpath([abs_path_working, abs_path]) == abs_path_working
    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    os.makedirs(parent_dir, exist_ok=True)
    try:
        with open(abs_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write/Overwrite the content specified in the content argument to the file specified by the file path argument. Then return a string describing if the call was successful and how many characters were written",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written to the file determined by the file_path argument",
            )
        },
    ),
)