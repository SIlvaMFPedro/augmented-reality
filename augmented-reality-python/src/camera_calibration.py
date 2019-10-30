# ------------------------
#   IMPORTS
# ------------------------
# Import the necessary packages
import cv2


# ------------------------
#   Camera Calibration
# ------------------------
class CameraCalibration:
    """
        Class used to read calibration matrix from calibration.yaml file
    """
    def __init__(self):
        self.__camera_matrix = None
        self.__dist_matrix = None

    def calibrate_camera(self, path):
        """
        Code to calibrate the camera given a list of images for calibration
        :param path: path to calibration images
        :return: None
        """
        pass

    def get_calibration_from_file(self, path):
        """
        Extract the calibration values from the path
        :param path: path to calibration file
        :return: None
        """
        # read file storage
        cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)
        # specify the type of data to retrieve otherwise get a FileNode object back instead of a matrix
        self.__camera_matrix = cv_file.getNode("camera_matrix").mat()
        self.__dist_matrix = cv_file.getNode("dist_coeff").mat()
        print("Camera Matrix: ", self.__camera_matrix.tolist())
        print("Dist Matrix: ", self.__dist_matrix.tolist())
        cv_file.release()

    def get_camera_mat(self):
        """
        Return the camera matrix
        :return: returns the camera matrix
        """
        return self.__camera_matrix

    def get_dist_mat(self):
        """
        Return the distortion matrix
        :return: returns the distortion matrix
        """
        return self.__dist_matrix