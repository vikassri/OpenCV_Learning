import cv2
import numpy as np

# function to convert the images to match the channel


def stackImages(img_list=[], stack_type=0):

    # Create the empty list to store images
    list_of_img = []
    # Iterate the images
    for img in img_list:
        # check if the image is color or not , color will have (row, column, channel) where as gray dont have channel

        if len(img.shape) < 3:
            # transform the image to color level
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

        # add to list
        list_of_img.append(img)

    # check if we need to stack horizontal or vertical, by default is horizontal
    if stack_type == 0:
        imgStack = np.hstack(tuple(list_of_img))
    else:
        imgStack = np.vstack(tuple(list_of_img))

    # show the images
    cv2.imshow("Stacked Image", imgStack)

    # show the image for 5 seconds, 0 means undefinite
    cv2.waitKey(10000)

    # destroy all the image windows
    cv2.destroyAllWindows()


def stackImages(x_list=[], y_list=[]):
    # Create the empty list to store images
    list_of_x_img = []
    # Iterate the images
    for img in x_list:
        # check if the image is color or not , color will have (row, column, channel) where as gray dont have channel

        if len(img.shape) < 3:
            # transform the image to color level
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

        # add to list
        list_of_x_img.append(img)

    list_of_y_img = []
    for img in y_list:
        # check if the image is color or not , color will have (row, column, channel) where as gray dont have channel

        if len(img.shape) < 3:
            # transform the image to color level
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

        # add to list
        list_of_y_img.append(img)

    # check if we need to stack horizontal or vertical, by default is horizontal
    imgStack_x = np.hstack(tuple(list_of_x_img))
    imgStack_y = np.hstack(tuple(list_of_y_img))

    imgStack = np.vstack((imgStack_x, imgStack_y))

    # show the images
    cv2.imshow("Stacked Image", imgStack)

    # show the image for 5 seconds, 0 means undefinite
    cv2.waitKey(10000)

    # destroy all the image windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # read the images
    img = cv2.imread('Resources/small_bird.jpg')
    img2 = cv2.imread('Resources/small_bird.jpg', 0)
    img3 = cv2.imread('Resources/small_bird.jpg', -1)

    # Call the function
    stackImages([img, img2, img3])
