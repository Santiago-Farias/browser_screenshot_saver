import os

new_patch = '.\chupala'
if not os.path.exists(new_patch):
    print("No existe, creando.")
    os.makedirs(new_patch)
else:
    print("Ya existe bobi")