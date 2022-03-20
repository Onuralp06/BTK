import os
try:
    os.mkdir("elma")
except FileExistsError:
    print("Açmaya calıştığınız klasör mevcuttur. Lütfen farklı klasör adı yazınız!")
