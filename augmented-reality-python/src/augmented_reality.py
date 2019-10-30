# ------------------------
#   IMPORTS
# ------------------------
# Import the necessary packages
from src.json_parser import JsonReader
from src.camera_calibration import CameraCalibration
from src.threaded_webcam import WebCamVideoStream
from src.markers.aruco_marker import ArucoMarker
from src.markers.natural_feature_marker import NaturalFeatureMarker
import cv2


# ------------------------
#   Augmented Reality
# ------------------------
class AugmentedReality:
    """
        Class used to initialize the input source, find the marker and place the object using the obtained position
        of the marker
    """
    def __init__(self):
        """
        Initialize the various class required to run the augmented reality service.
        """
        self.__json_reader = JsonReader()
        self.__camera_calib = CameraCalibration()
        self.__camera = WebCamVideoStream().start()
        self.__marker_obj = None

    def set_service_parameter_json(self, path):
        """
        Set the JSON file path and read the required value
        :param path: Path to the configuration JSON file
        :return: None
        """
        self.__json_reader.read_from_file(path)
        calib_path = self.__json_reader.get_value("calibration_path")
        self.__camera_calib.get_calibration_from_file(calib_path)
        marker_type = self.__json_reader.get_value("marker_type")
        self.set_marker(marker_type)

    def set_marker(self, type):
        """
        Create a marker object depending on the json input
        :param type: Marker type string
        :return: None
        """
        marker_params = self.__json_reader.get_value("marker_params")
        if type == "aruco":
            self.__marker_obj = ArucoMarker()
        if type == "nft":
            self.__marker_obj = NaturalFeatureMarker()
        self.__marker_obj.set_json_parameters(marker_params)
        self.__marker_obj.set_calib_parameters(self.__camera_calib.get_camera_mat(), self.__camera_calib.get_dist_mat())

    def process_image(self, frame):
        """
        Function used to run the process of each frame and then sets the pose.
        :param frame: Current frame to be processed
        :return: None
        """
        self.__marker_obj.set_input_image(frame)
        self.__marker_obj.process_image()
        self.__marker_obj.get_pose()

    def run_service(self):
        """
        Take the frame from the source, processes the frame and shows it.
        :return:
        """
        if not self.__camera.isOpened():
            raise IOError("Cannot open webcam!")
        while True:
            frame = self.__camera.read()
            self.process_image(frame)
            output = self.get_output()
            cv2.imshow('AR', output)
            c = cv2.waitKey(30)
            if c == 27:
                self.__camera.stop()
                break

    def get_output(self):
        """
        Return the image with the debug markings.
        :return: Output image from the service.
        """
        return self.__marker_obj.get_output_image()
