import os
import sys

# setting path
sys.path.append("../")
sys.path.append("/opt/mri4all/console/external/")

import common.logger as logger
import common.runtime as rt
import common.helper as helper

rt.set_service_name("tests")
log = logger.get_logger()

from sequences import SequenceBase


def run_sequence_test(sequence_name: str) -> bool:
    log.info(f"Testing sequence {sequence_name}...")

    temp_folder = "/tmp/" + helper.generate_uid()
    log.info(f"Using temporary folder: {temp_folder}")

    try:
        os.mkdir(temp_folder)
    except:
        log.error(f"Could not create temporary folder {temp_folder}.")
        return False

    sequence_instance = SequenceBase.get_sequence(sequence_name)()
    # Get the default parameters from the sequence as an example
    default_parameters = sequence_instance.get_default_parameters()
    # Configure the sequence with the default parameters. Normally, the parameters would come from the JSON file.
    sequence_instance.set_parameters(default_parameters)
    sequence_instance.set_working_folder(temp_folder)
    sequence_instance.calculate_sequence()
    sequence_instance.run_sequence()

    return True


def run_tests() -> bool:
    log.info("Running tests for sequences...")
    log.info("")
    run_sequence_test("rf_se")
    return True


if __name__ == "__main__":
    run_tests()
