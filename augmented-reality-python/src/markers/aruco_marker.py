# ------------------------
#   IMPORTS
# ------------------------
# Import the necessary packages
import cv2
import numpy as np
import cv2.aruco as aruco

from src.markers.marker_base import MarkerBase


# ------------------------
#   ARUCO MARKER
# ------------------------
class ArucoMarker(MarkerBase):
    def __init__(self):
        super(ArucoMarker, self).__init__()
        self.__in_image = None
        self.__json_params = None
        self.__cam_mat = None
        self.__dist_mat = None
        self.__r_vec = None
        self.__t_vec = None
        self.__aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        self.__parameters = aruco.DetectorParameters_create()
        self.__corner_points = None

    def set_json_parameters(self, params):
        self.__json_params = params

    def set_calib_parameters(self, cam_mat, dist_mat):
        self.__cam_mat = cam_mat
        self.__dist_mat = dist_mat

    def process_image(self):
        gray = cv2.cvtColor(self.__in_image, cv2.COLOR_BGR2GRAY)
        # get list of IDs and the corners belonging to each ID
        self.__corner_points, ids, rejectedImgPoints = aruco.detectMarkers(gray,
                                                                           self.__aruco_dict,
                                                                           parameters=self.__parameters)
        if np.all(ids):
            for i in range(len(ids)):
                # Estimate the pose of each marker and return the values rvet
                # and tvec-different from camera coefficients
                self.__r_vec, self.__t_vec, _ = aruco.estimatePoseSingleMarkers(self.__corner_points[i], 0.05,
                                                                                self.__cam_mat,
                                                                                self.__dist_mat)
                if self.__json_params["debug_draw"]:
                    # Draw Axis
                    aruco.drawAxis(self.__in_image, self.__cam_mat, self.__dist_mat,
                                   self.__r_vec[0], self.__t_vec[0], 0.05)
                    # Draw a square around the markers
                    aruco.drawDetectedMarkers(self.__in_image, self.__corner_points)
            cv2.putText(self.__in_image, "Id: " + str(ids), (0, 64),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    def set_input_image(self, input):
        self.__in_image = input

    def get_output_image(self):
        return self.__in_image

    def get_pose(self):
        return self.__t_vec, self.__r_vec

    def get_corners(self):
        return self.__corner_points


if __name__ == "__main__":
    marker = ArucoMarker()

