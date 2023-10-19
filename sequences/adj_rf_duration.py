from pathlib import Path

import numpy as np
import time

import external.seq.adjustments_acq.config as cfg
import external.seq.adjustments_acq.scripts as scr  # pylint: disable=import-error
from external.seq.adjustments_acq.calibration import rf_duration_cal

import common.logger as logger

from sequences import PulseqSequence  # type: ignore
from sequences.rf_se import pypulseq_rfse  # type: ignore


log = logger.get_logger()


class AdjRFDuration(PulseqSequence, registry_key=Path(__file__).stem):
    @classmethod
    def get_readable_name(self) -> str:
        return "Adjust RF Duration"

    def calculate_sequence(self) -> bool:
        points = 25  # number of steps, to be added as a parameter
        rf_min_duration, rf_max_duration = 50e-6, 300e-6  # in seconds
        rf_duration_vals = np.linspace(
            rf_min_duration, rf_max_duration, num=points, endpoint=True
        )

        # Calculating sequence for different RF pulse durations
        for i in range(points):
            self.seq_file_path = (
                self.get_working_folder()
                + "/seq/rf_duration_calib_"
                + str(i + 1)
                + ".seq"
            )
            log.info("Calculating sequence " + self.get_name())
            pypulseq_rfse(
                inputs={},
                check_timing=True,
                output_file=self.seq_file_path,
                rf_duration=rf_duration_vals[i],
            )
            log.info("Done calculating sequence " + self.get_name())
            self.calculated = True

        return True

    def run_sequence(self) -> bool:
        log.info("Running RF calibration sequences ")

        points = 25  # number of steps, to be added as a parameter
        tr_spacing = 2  # [us] Time between repetitions

        # Make sure the TR units are right (in case someone puts in us rather than s)
        if tr_spacing >= 30:
            print(
                'TR spacing is over 30 seconds! Set "force_tr" to True if this isn\'t a mistake. '
            )
            return -1

        # Run sequences for different RF pulse duration
        print("Running RF duration calibration sequences")
        rxd_list = []
        for i in range(points):
            seq_file = (
                self.get_working_folder()
                + "/seq/rf_duration_calib_"
                + str(i + 1)
                + ".seq"
            )
            rxd, rx_t = scr.run_pulseq(
                seq_file,
                rf_center=cfg.LARMOR_FREQ,
                tx_t=1,
                grad_t=10,
                tx_warmup=100,
                shim_x=cfg.SHIM_X,
                shim_y=cfg.SHIM_Y,
                shim_z=cfg.SHIM_Z,
                rf_max=cfg.RF_MAX,
                grad_cal=False,
                save_np=True,
                save_mat=False,
                save_msgs=False,
                gui_test=False,
            )
            rxd_list.append(rxd)
            time.sleep(tr_spacing)

            # Print progress
            if (i + 1) % 5 == 0:
                print(f"Finished point {i + 1}/{points}...")

        # Identify the RF duration corresponding to the maximal echo amplitude
        rf_duration_cal(rdx_list=rxd_list, points=points)

        log.info("Done RF calibration sequences ")
        return True
