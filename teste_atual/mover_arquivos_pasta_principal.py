import os
import shutil

# Caminho para a pasta onde estão as subpastas com as imagens
main_folder = 'C:/Users/Edu/Desktop/Edu/estudos/tcc/dataset/images/11'

# Percorrer todas as subpastas dentro da pasta principal
for root, dirs, files in os.walk(main_folder):
    for file in files:
        # Verificar se o arquivo é uma imagem (você pode ajustar as extensões conforme necessário)
        if file.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            # Caminho completo da imagem
            file_path = os.path.join(root, file)
            
            # Caminho de destino (pasta principal)
            destination = os.path.join(main_folder, file)
            
            # Mover a imagem para a pasta principal
            shutil.move(file_path, destination)

print("Imagens movidas com sucesso!")
