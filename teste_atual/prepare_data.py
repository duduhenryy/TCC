#Este script ajuda a organizar seu dataset e converter as anotações no formato adequado para o YOLOv5

import os
import shutil
import random

def prepare_dataset(dataset_path, train_ratio=0.8):
    images_path = os.path.join(dataset_path, 'images')
    labels_path = os.path.join(dataset_path, 'labels')

    images = os.listdir(images_path)
    random.shuffle(images)

    train_size = int(len(images) * train_ratio)
    
    train_images = images[:train_size]
    val_images = images[train_size:]

    # Criar diretórios
    train_image_dir = os.path.join(dataset_path, 'train', 'images')
    train_label_dir = os.path.join(dataset_path, 'train', 'labels')
    val_image_dir = os.path.join(dataset_path, 'val', 'images')
    val_label_dir = os.path.join(dataset_path, 'val', 'labels')
    
    os.makedirs(train_image_dir, exist_ok=True)
    os.makedirs(train_label_dir, exist_ok=True)
    os.makedirs(val_image_dir, exist_ok=True)
    os.makedirs(val_label_dir, exist_ok=True)
    
    for image in train_images:
        image_path = os.path.join(images_path, image)
        label_path = os.path.join(labels_path, image.replace('.jpg', '.txt'))
        
        shutil.copy(image_path, train_image_dir)
        shutil.copy(label_path, train_label_dir)

    for image in val_images:
        image_path = os.path.join(images_path, image)
        label_path = os.path.join(labels_path, image.replace('.jpg', '.txt'))
        
        shutil.copy(image_path, val_image_dir)
        shutil.copy(label_path, val_label_dir)

    print(f'Dataset preparado! {train_size} imagens para treino e {len(images) - train_size} para validação.')

if __name__ == "__main__":
    dataset_path = 'dataset'
    prepare_dataset(dataset_path)
