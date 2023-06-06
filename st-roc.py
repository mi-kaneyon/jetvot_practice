import subprocess

def get_gpu_name():
    process = subprocess.Popen(['lspci'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    lines = out.decode().split('\n')
    for line in lines:
        if 'VGA compatible controller' in line and 'AMD' in line:
            return line.split(': ')[-1]
    return "Unknown GPU"

def get_gpu_info():
    process = subprocess.Popen(['rocm-smi'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode()

print("GPU Name: ", get_gpu_name())
print(get_gpu_info())
