import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

def normalize_image(image, bounds, size):
    image = clip_image(image, bounds)
    image = resize_image(image, size)
    return image

def normalize_label(label, bounds, size):
    label = clip_label(label, bounds)
    label = resize_label(label, bounds[1] - bounds[0], size)
    return label

def bounding_box(center, size, fx):
    bounding_box = np.array([[0, 0, 0], [1, 1, 1]], dtype='float')
    bounding_box -= 0.5
    bounding_box *= size
    bounding_box[..., :-1] *= fx / center[..., -1]
    bounding_box += center

    return bounding_box

def resize_image(image, new_size):
    image *= new_size[-1]

    new_size = np.array(new_size, dtype=int)
    image = scipy.misc.imresize(image.squeeze(), new_size[-2::-1], 'bilinear', mode='F')

    return image[..., None]

def resize_label(label, old_size, new_size):
    label *= new_size / old_size
    return label

def clip_image(image, bounding_box):
    bounding_box = np.array(bounding_box)

    image = np.clip(image, *bounding_box[..., -1]).astype(float)
    image -= (bounding_box[1, -1] + bounding_box[0, -1]) / 2
    image = image / (bounding_box[1, -1] - bounding_box[0, -1])

    bounding_box = bounding_box.astype(int)

    padding = np.array([-bounding_box[0, :-1], bounding_box[1, :-1] - image.shape[::-1]]).clip(0)
    bounding_box[..., :-1] += padding[0]

    image = np.pad(image, padding.T[::-1], 'edge')
    image = image[slice(*bounding_box[:, 1]), slice(*bounding_box[:, 0])]

    return image

def clip_label(label, bounding_box):
    label -= bounding_box[0]
    label[:, -1] += (bounding_box[1, -1] - bounding_box[0, -1]) / 2
    return label

def uvd_to_xyz(uvd):
    normalized_x = uvd[..., 0] / 640 - 0.5
    normalized_y = 0.5 - uvd[..., 1] / 480
    
    xyz = np.zeros(uvd.shape)
    xyz[..., 2] = uvd[..., 2]
    xyz[..., 0] = normalized_x * xyz[..., 2] * 1.08836710
    xyz[..., 1] = normalized_y * xyz[..., 2] * 0.817612648
    
    return xyz
