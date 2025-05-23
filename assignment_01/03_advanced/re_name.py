import os

directory = r"C:\Users\Selltricks\Desktop\project\simple-calculator\node_modules\assignment-4\assignment_01\03_advanced"
old_prefix = 'old_prefix_'
new_prefix = 'new_prefix_'

for filename in os.listdir(directory):
    if filename.startswith(old_prefix) and filename.endswith('.py'):
        old_file = os.path.join(directory, filename)
        new_filename = filename.replace(old_prefix, new_prefix, 1)
        new_file = os.path.join(directory, new_filename)
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')
