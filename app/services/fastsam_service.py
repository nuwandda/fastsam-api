import sys
sys.path.append('app/services')
from app.services.fastsam import FastSAM, FastSAMPrompt
from PIL import Image
from io import BytesIO
import numpy as np
import uuid
import base64
from app.utils import file_operations
from app.utils.logging import logger
import requests
import torch
import cv2


class FastSAMService:
    def __init__(self, weights='app/services/weights/FastSAM.pt', device='cpu', better_quality=True):
        self.device = device
        self.model = FastSAM(weights)
        self.better_quality = better_quality
        
        
    def determine_resize_resolution(self, image_pil):
        width, height = image_pil.size    
        aspect_ratio = width / height
        orientation = ''
        if aspect_ratio > 1:
            orientation = 'horizontal'
        elif aspect_ratio < 1:
            orientation = 'vertical'
        else:
            orientation = 'square'
        
        if orientation=='square':
            resize_width=512
            resize_height=512
        elif orientation=='vertical':
            resize_width=512
            resize_height=768
        elif orientation=='horizontal':
            resize_width=768
            resize_height=512        

        if resize_width==512 and resize_height==512:
            resize_size_width=256
            resize_size_height=256
        elif resize_width==512 and resize_height==768:
            resize_size_width=256
            resize_size_height=384        
        elif resize_width==768 and resize_height==512:
            resize_size_width=384
            resize_size_height=256
            
        return (resize_size_width, resize_size_height)


    def process(self, request_data):
        # Create a temporary directory
        logger.info('Reading and saving the input image...')
        temp_id = str(uuid.uuid4())
        temp_path = '/tmp/{}'.format(temp_id)
        file_operations.create_temp(temp_path)
        
        # Read the image from url
        image_content_path = requests.get(request_data.image_path)
        image_content = Image.open(BytesIO(image_content_path.content))

        # Save the image to the temporary directory
        init_image = image_content.convert('RGB')
        init_image.save(temp_path + '/input_image.png')
        logger.info('Input image is saved.')
        
        # Core FastSAM processing logic
        logger.info('Generating masks...')
        everything_results = self.model(temp_path + '/input_image.png', device=self.device, retina_masks=True, imgsz=1024, conf=0.4, iou=0.9)
        prompt_process = FastSAMPrompt(temp_path + '/input_image.png', everything_results, device=self.device)
        logger.info('Generated.')
        
        logger.info('Preparing annotations...')
        annotations = prompt_process.everything_prompt()
        if isinstance(annotations[0], dict):
            annotations = [annotation['segmentation'] for annotation in annotations]
        logger.info('Annotations are ready.')
            
        if self.better_quality:
            logger.info('Improving mask quality...')
            if isinstance(annotations[0], torch.Tensor):
                annotations = np.array(annotations.cpu())
            for i, mask in enumerate(annotations):
                mask = cv2.morphologyEx(mask.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
                annotations[i] = cv2.morphologyEx(mask.astype(np.uint8), cv2.MORPH_OPEN, np.ones((8, 8), np.uint8))
            logger.info('Mask quality improved.')
        
        logger.info('Resizing masks...')
        result_array = []
        resize_size = self.determine_resize_resolution(init_image)
        for mask in annotations:
            loaded_data = mask
            resized_image = cv2.resize(np.asarray(loaded_data).astype(np.uint8) * 255, resize_size)
            result_array.append(resized_image.tolist())
        logger.info('Masks resized.')
        
        return result_array
