# inferir novas imagens ou vídeos com o modelo treinado

import torch
from yolov5 import detect

def run_detection(weights_path, source='dataset/test/images', img_size=640, conf_thres=0.25):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    detect.run(weights=weights_path, 
               source=source, 
               imgsz=img_size, 
               conf_thres=conf_thres,
               device=device)

if __name__ == "__main__":
    weights_path = 'runs/train/exp/weights/best.pt'  # Peso do modelo treinado
    run_detection(weights_path)
