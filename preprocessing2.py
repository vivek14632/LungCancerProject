#It's in full working code verified
# check for all doubts here https://www.kaggle.com/arnavkj95/data-science-bowl-2017/candidate-generation-and-luna16-preprocessing/notebook
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import skimage, os
from skimage.morphology import ball, disk, dilation, binary_erosion, remove_small_objects, erosion, closing, reconstruction, binary_closing
from skimage.measure import label,regionprops, perimeter
from skimage.morphology import binary_dilation, binary_opening
from skimage.filters import roberts, sobel
from skimage import measure, feature
from skimage.segmentation import clear_border
from skimage import data
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import dicom
import scipy.misc
import numpy as np
import matplotlib
import PyQt5
matplotlib.use('qt4agg')

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

# vivek: The following code is specific to linux (ls command is used)
# So i am commenting the code
#from subprocess import check_output
#print(check_output(["ls", "/media/nargis/Seagate Backup Plus Drive/Lung Cancer/sample_images"]).decode("utf8"))



#print(check_output(["ls", "../input/sample_images/"]).decode("utf8"))

# Any results you write to the current directory are saved as output.
lung = dicom.read_file('/media/nargis/Seagate Backup Plus Drive/Lung Cancer/sample_images/00cba091fa4ad62cc3200a657aeb957e/38c4ff5d36b5a6b6dc025435d62a143d.dcm')

# vivek: Following code is applicable to my system only
lung = dicom.read_file('C:/Users/ThinkPad/Documents/00cba091fa4ad62cc3200a657aeb957e/0a291d1b12b86213d813e3796f14b329.dcm')

slice = lung.pixel_array

# lung is an object in python. to get all the 
# available methods and variables in that object, use dir() function
#>>> dir(lung)
#['AcquisitionNumber', 'BitsAllocated', 'BitsStored', 'Columns', 'FrameOfReferenceUID', 'HighBit', 'ImageOrientationPatient', 'ImagePositionP
#atient', 'InstanceNumber', 'KVP', 'Modality', 'PatientBirthDate', 'PatientID', 'PatientName', 'PatientOrientation', 'PhotometricInterpretati
#on', 'PixelData', 'PixelPaddingValue', 'PixelRepresentation', 'PixelSpacing', 'PositionReferenceIndicator', 'RescaleIntercept', 'RescaleSlop
#e', 'Rows', 'SOPClassUID', 'SOPInstanceUID', 'SamplesPerPixel', 'SeriesDescription', 'SeriesInstanceUID', 'SeriesNumber', 'SliceLocation', '
#SpecificCharacterSet', 'StudyInstanceUID', 'WindowCenter', 'WindowWidth', '__contains__', '__delattr__', '__delitem__', '__dir__', '__eq__',
# '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__init__', '__init_subclass__', '__iter__', '__le__',
#'__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
#'__subclasshook__', '__weakref__', '_character_set', '_get_pixel_array', '_pixel_data_numpy', '_pretty_str', 'add', 'add_new', 'clear', 'cop
#y', 'data_element', 'decode', 'dir', 'formatted_lines', 'fromkeys', 'get', 'get_item', 'group_dataset', 'items', 'iterall', 'keys', 'pixel_a
#rray', 'pop', 'popitem', 'remove_private_tags', 'save_as', 'setdefault', 'top', 'trait_names', 'update', 'values', 'walk']
#>>>



slice[slice == -2000] = 0
plt.imshow(slice, cmap=plt.cm.gray)
plt.show()

def read_ct_scan(folder_name):
        # Read the slices from the dicom file
        slices = [dicom.read_file(folder_name + filename) for filename in os.listdir(folder_name)]

        # Sort the dicom slices in their respective order
        slices.sort(key=lambda x: int(x.InstanceNumber))

        # Get the pixel values for all the slices
        slices = np.stack([s.pixel_array for s in slices])
        slices[slices == -2000] = 0
        return slices

ct_scan = read_ct_scan('/media/nargis/Seagate Backup Plus Drive/Lung Cancer/sample_images/00cba091fa4ad62cc3200a657aeb957e/') # array of pixel_array
len(ct_scan) # total number of slices in a dicom image

def plot_ct_scan(scan):
    f, plots = plt.subplots(int(scan.shape[0] / 20) + 1, 4, figsize=(25, 25))
    for i in range(0, scan.shape[0], 5):
        plots[int(i / 20), int((i % 20) / 5)].axis('off')
        plots[int(i / 20), int((i % 20) / 5)].imshow(scan[i], cmap=plt.cm.bone)


plot_ct_scan(ct_scan)
plt.show()


def get_segmented_lungs(im, plot=False):

    '''
    This funtion segments the lungs from the given 2D slice.
    '''
    if plot == True:
        f, plots = plt.subplots(8, 1, figsize=(5, 40))
    '''
    Step 1: Convert into a binary image.
    '''
    binary = im < 604
    if plot == True:
        plots[0].axis('off')
        plots[0].imshow(binary, cmap=plt.cm.bone)
        #plt.show()
    '''
    Step 2: Remove the blobs connected to the border of the image.
    '''
    cleared = clear_border(binary)
    if plot == True:
        plots[1].axis('off')
        plots[1].imshow(cleared, cmap=plt.cm.bone)

    '''
    Step 3: Label the image.
    '''
    label_image = label(cleared)
    if plot == True:
        plots[2].axis('off')
        plots[2].imshow(label_image, cmap=plt.cm.bone)

    '''
    Step 4: Keep the labels with 2 largest areas.
    '''
    areas = [r.area for r in regionprops(label_image)]
    areas.sort()
    if len(areas) > 2:
        for region in regionprops(label_image):
            if region.area < areas[-2]:
                for coordinates in region.coords:
                       label_image[coordinates[0], coordinates[1]] = 0
    binary = label_image > 0
    if plot == True:
        plots[3].axis('off')
        plots[3].imshow(binary, cmap=plt.cm.bone)

    '''
    Step 5: Erosion operation with a disk of radius 2. This operation is
    seperate the lung nodules attached to the blood vessels.
    '''
    selem = disk(2)
    binary = binary_erosion(binary, selem)
    if plot == True:
        plots[4].axis('off')
        plots[4].imshow(binary, cmap=plt.cm.bone)

    '''
    Step 6: Closure operation with a disk of radius 10. This operation is
    to keep nodules attached to the lung wall.
    '''
    selem = disk(10)
    binary = binary_closing(binary, selem)
    if plot == True:
        plots[5].axis('off')
        plots[5].imshow(binary, cmap=plt.cm.bone)

    '''
    Step 7: Fill in the small holes inside the binary mask of lungs.
    '''
    edges = roberts(binary)
    binary = ndi.binary_fill_holes(edges)
    if plot == True:
        plots[6].axis('off')
        plots[6].imshow(binary, cmap=plt.cm.bone)

    '''
    Step 8: Superimpose the binary mask on the input image.
    '''
    get_high_vals = binary == 0
    im[get_high_vals] = 0
    if plot == True:
        plots[7].axis('off')
        plots[7].imshow(im, cmap=plt.cm.bone)
    #plt.show()
    return im

get_segmented_lungs(ct_scan[71], True)
plt.show()

def segment_lung_from_ct_scan(ct_scan):
    return np.asarray([get_segmented_lungs(slice) for slice in ct_scan])

segmented_ct_scan = segment_lung_from_ct_scan(ct_scan)
plot_ct_scan(segmented_ct_scan)

segmented_ct_scan[segmented_ct_scan < 604] = 0 # not sure if we should do this. I got everything black after I did this transformation
plot_ct_scan(segmented_ct_scan)


selem = ball(2)
binary = binary_closing(segmented_ct_scan, selem)

label_scan = label(binary)

areas = [r.area for r in regionprops(label_scan)]
areas.sort()

for r in regionprops(label_scan): # not sure if we should do this. I got everything black after I did this transformation
    max_x, max_y, max_z = 0, 0, 0
    min_x, min_y, min_z = 1000, 1000, 1000
    
    for c in r.coords:
        max_z = max(c[0], max_z)
        max_y = max(c[1], max_y)
        max_x = max(c[2], max_x)
        
        min_z = min(c[0], min_z)
        min_y = min(c[1], min_y)
        min_x = min(c[2], min_x)
    if (min_z == max_z or min_y == max_y or min_x == max_x or r.area > areas[-3]):
        for c in r.coords:
            segmented_ct_scan[c[0], c[1], c[2]] = 0
    else:
        index = (max((max_x - min_x), (max_y - min_y), (max_z - min_z))) / (min((max_x - min_x), (max_y - min_y) , (max_z - min_z)))
