import pygame
import os

def loading(path):
    image_list = []
    size_list = []
    file_list = os.listdir(path)
    for filename in file_list:
        for s in filename:
            if s.isdigit():
                size_list.append(int(s))
        if filename.endswith(".png"):
            image = pygame.image.load(os.path.join(path, filename))
            image_list.append(image)
    x = dict(zip(image_list ,size_list))
    sorted_x = sorted(x.items(), key=lambda x:x[1])
    return sorted_x