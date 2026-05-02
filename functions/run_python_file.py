import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_path_working = os.path.abspath(working_directory)
    abs_path = os.path.normpath(os.path.join(abs_path_working, file_path))
    valid_target_file = os.path.commonpath([abs_path_working, abs_path]) == abs_path_working
    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if file_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file'
    try:
        command = ["python", abs_path]
        if args:
            command.extend(args)
        result_of_subprocess = subprocess.run(command, cwd=abs_path_working, capture_output=True, text=True, timeout=30)
        output_parts = []
        if result_of_subprocess.stdout:
            output_parts.append(f"STDOUT: {result_of_subprocess.stdout}")
        if result_of_subprocess.stderr:
            output_parts.append(f"STDERR: {result_of_subprocess.stderr}")
        if len(output_parts) < 1:
            output_parts.append("No output produced")
        if result_of_subprocess.returncode != 0:
            output_parts.append("Process exited with code X")
        return "\n".join(output_parts)
    except Exception as e:
        return f"Error: {e}"