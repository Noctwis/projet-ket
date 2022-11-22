import base64
from io import BytesIO
from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image
from src import cityscapes
import segmentation_models as sm
from segmentation_models import Unet


sm.set_framework('tf.keras')

sm.framework()

# same idea for dice and jaccard metrics
def dice_metric(y_true, y_pred):
    smooth = 1.
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    score = (2. * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)
    return score

def dice_loss(y_true, y_pred):
    loss = 1 - dice_metric(y_true, y_pred)
    return loss




BACKBONE = 'resnet34'
model_resnet = Unet(BACKBONE, encoder_weights='imagenet', classes=8,activation='softmax')
model_resnet.compile('Adam', loss=dice_loss, metrics=[dice_metric])

# Loads the weights
model_resnet.load_weights('model.hdf5')


#model.make_predict_function()          # Necessary

    
    
    
def get_images(
   
    
    dataset_path="C:/Users/jketk/Desktop/p8data",
    image_id=None,
):
    
    
    
    

    resize = 256
    img_size = (resize, resize)

    leftImg8bit_path = Path(dataset_path, "leftImg8bit")
    gtFine_path = Path(dataset_path, "gtFine")

    image_id = str(image_id)
    input_img_paths = []
    labels_img_paths = []
    if image_id:
        input_img_paths = sorted(
            Path(leftImg8bit_path).glob(f"**/*{image_id}*_leftImg8bit.png")
        )
        labels_img_paths = sorted(
            Path(gtFine_path).glob(f"**/*{image_id}*_color.png")
        )

    if len(input_img_paths) == 0 or len(labels_img_paths) == 0:
        input_img_paths = sorted(
            Path(leftImg8bit_path, "val").glob("**/*_leftImg8bit.png")
        )
        labels_img_paths = sorted(
            Path(gtFine_path, "val").glob("**/*_color.png")
        )

    rand_idx = np.random.randint(0, len(input_img_paths))

    with open(input_img_paths[rand_idx], "rb") as f:
        original_img = base64.b64encode(f.read())
        original_img_str = original_img.decode("utf-8")

        input_img = Image.open(
            BytesIO(base64.b64decode(original_img))
        ).resize(img_size)
        categories_img = Image.fromarray(
            cityscapes.cityscapes_category_ids_to_category_colors(
                np.squeeze(
                    np.argmax(
                       model_resnet.predict(np.expand_dims(input_img, 0)), axis=-1
                    )
                )
            )
        )

        buffered = BytesIO()
        categories_img.save(buffered, format="PNG")
        categories_img_str = base64.b64encode(buffered.getvalue()).decode(
            "utf-8"
        )
        

    with open(labels_img_paths[rand_idx], "rb") as f:
        labels_img_read = f.read()
        labels_img = base64.b64encode(labels_img_read)
        labels_img_str = labels_img.decode("utf-8")

    return original_img_str, labels_img_str,categories_img_str