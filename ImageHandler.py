import scipy.misc as misc
import os
import shutil

def downsampling(file_dir, save_dir, scale, arg=""):
    '''
    Downsample images in file_dir and save them
    :param file_dir: directory to downsample images
    :param save_dir: directory to save result images
    :param scale: downsample scale ex) 2
    :param arg: argument to add to file name
    :return:
    '''
    if not os.path.exists(save_dir + "/x{}".format(scale)):
        os.mkdir(save_dir + "x{}".format(scale))
    file_list = os.listdir(file_dir)
    for file in file_list:
        print(file)
        image = misc.imread(file_dir + file)
        converted_image = misc.imresize(image, size=100 // scale, interp='bicubic')
        # print(converted_image)
        misc.imsave(save_dir + "x{}/{}{}x{}.png".format(scale, file[:-4], arg, scale), converted_image)
    return

def upsampling(file_dir, save_dir, scale):
    '''
    Upsample images in file_dir and save them
    These files is used to compare RCAN result
    :param file_dir: directory to upsample images
    :param save_dir: directory to save result images
    :param scale: upsample scale ex) 4
    :return:
    '''
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    file_list = os.listdir(file_dir + "x{}/".format(int(1/scale)))
    for file in file_list:
        print(file)
        image = misc.imread(file_dir + "x{}/".format(int(1/scale)) + file)
        converted_image = misc.imresize(image, size=(968, 968), interp='bicubic')
        misc.imsave(save_dir + "{}x{}.png".format(file[:4], int(1/scale)), converted_image)
    return

def centerCropping(image, image_size):
    '''
    crop the center of image into image_size
    :param image: cropped image
    :param image_size: cropped image size
    :return: cropped_image
    '''
    y, x = image.shape
    start_x = x//2 - image_size//2
    start_y = y//2 - image_size//2
    return image[start_y:start_y+image_size, start_x:start_x+image_size]

def prepareTestData(origin_dir, HR_dir, LR_dir, scale):
    '''
    copy downsampled image and original image in origin_dir to HR_dir and LR_dir for test
    :param origin_dir: original directory of images
    :param HR_dir: directory to copy original images
    :param LR_dir: directory to copy downsampled images
    :param scale: downsample scale
    :return:
    '''
    file_list = os.listdir(origin_dir)
    for file in file_list:
        print(file)
        image = misc.imread(origin_dir+file)
        shutil.copy(origin_dir+file, HR_dir + "x{}/{}_HR_x{}.png".format(scale, file[:-4], scale))
        converted_image = misc.imresize(image, size=100 // scale, interp='bicubic')
        misc.imsave(LR_dir + "x{}/{}_LRBI_x{}.png".format(scale, file[:-4], scale), converted_image)
    return

def copyImage(origin_dir, destination, scale = 2):
    '''
    copy images in origin_dir
    :param origin_dir: original directory of images
    :param desination: destination to move of images
    :param scale: destination directory of scale
    :return:
    '''
    file_list = os.listdir(origin_dir)
    for file in file_list:
        print(file)
        image = misc.imread(origin_dir + file)
        shutil.copy(origin_dir + file, destination + "x{}/{}_LRBI_x{}.png".format(scale, file[:-4], scale))
    return