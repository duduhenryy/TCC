import os
import torch
from yolov5 import train

# Função para filtrar as classes durante o treinamento
def filter_labels(annotation_dir, allowed_classes):
    for root, dirs, files in os.walk(annotation_dir):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                # Filtra as anotações para manter apenas as classes permitidas
                filtered_lines = [line for line in lines if int(line.split()[0]) in allowed_classes]

                # Sobrescreve o arquivo com as anotações filtradas
                with open(file_path, 'w') as file:
                    file.writelines(filtered_lines)

# Função para treinar o modelo
def train_model(data_yaml, epochs=100, batch_size=16, img_size=640):
    # Filtrar as classes antes do treinamento
    train_annotations = 'C:/Users/Edu/Desktop/Edu/estudos/tcc/dataset/labels/10'
    val_annotations = 'C:/Users/Edu/Desktop/Edu/estudos/tcc/dataset/labels/12'

    # Classes permitidas: 1 e 2 (Setting e Waiting)
    allowed_classes = [1, 2]
    
    print("Filtrando as classes antes do treinamento...")
    filter_labels(train_annotations, allowed_classes)
    filter_labels(val_annotations, allowed_classes)

    # Verificar se a GPU está disponível
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # Chamando o treinamento do YOLOv5
    train.run(data=data_yaml,
              imgsz=img_size,
              batch_size=batch_size,
              epochs=epochs,
              device=device)

if __name__ == "__main__":
    # Localização do arquivo data.yaml
    data_yaml = 'dataset/data.yaml'

    # Treinar o modelo
    train_model(data_yaml)
