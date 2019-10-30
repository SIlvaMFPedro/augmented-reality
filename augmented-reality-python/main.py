# ------------------------
#   IMPORTS
# ------------------------
# Import the necessary packages
from src.augmented_reality import AugmentedReality

if __name__ == '__main__':
    # Start the AR service
    ar_service = AugmentedReality()

    ar_service.set_service_parameter_json("data/aruco-params.json")
    # ar_service.set_service_parameter_json("data/nft-params.json")

    ar_service.run_service()
    ar_service.get_output()