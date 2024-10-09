#treinar o modelo YOLOv5 no dataset.

import os
import torch
from yolov5 import train

# Função para treinar o modelo
def train_model(data_yaml, epochs=100, batch_size=16, img_size=640):
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
