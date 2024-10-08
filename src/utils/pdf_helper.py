import io
import fitz
import os
import PIL.Image
import numpy as np

def extract_images_util(pdf: fitz.Document, page: int, imgDir: str = 'data/files/cv/image', prefix_file_name = 'empty'):
    imageList = pdf[page].get_images()
    os.makedirs(imgDir, exist_ok=True)
    paths = []

    if imageList:
        for idx, img in enumerate(imageList, start=1):
            data = pdf.extract_image(img[0])
            with PIL.Image.open(io.BytesIO(data.get('image'))) as image:
                image_shape = np.array(image).shape
                h, w = image_shape[0], image_shape[1]
                if max(h, w) / min(h, w) >= 20:
                    continue
                path = f'{imgDir}/{prefix_file_name}-{page}-{idx}.{data.get("ext")}'
                paths.append(path)
                image.save(path, mode='wb')

    return paths

def extract_images(path: str):
    prefix_file_name = path.split("/")[-1].split(".")[0]
    pdf = fitz.open(path)

    paths = []
    for page in range(pdf.page_count):
        paths += extract_images_util(pdf, page, imgDir = 'data/files/cv/image', prefix_file_name = prefix_file_name)

    return paths