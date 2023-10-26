"""
| This file defines paths for reuse across all functions related to:
1. Virtual Scanner
2. Pypulseq
3. Flocra-pulseq
4. marcos-client
"""

from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.parent   # This is at the level of MRI4ALL
RELATIVE_PATH = ROOT_PATH.relative_to('/opt/mri4all')
#### ---------------------------
# Acq service paths go here
DATA_PATH_ACQ = RELATIVE_PATH/'data' / 'acq'

# Recon service paths go here
DATA_PATH_RECON = ROOT_PATH/'data' / 'recon'


# # coms_ui
# COMS_PATH = ROOT_PATH / 'virtual-scanner' / 'coms'
# COMS_UI_PATH = COMS_PATH / 'coms_ui'
# COMS_UI_STATIC_USER_UPLOAD_PATH = ROOT_PATH / 'coms' / 'coms_ui' / 'static' / 'user_uploads'
# # COMS_UI_STATIC_ANALYZE_PATH = Path('static') / 'ana'
# COMS_UI_STATIC_ANALYZE_PATH = ROOT_PATH / 'coms' / 'coms_ui' / 'static' / 'ana'
# # COMS_UI_STATIC_ACQUIRE_PATH = Path('static') / 'acq'
# COMS_UI_STATIC_ACQUIRE_PATH = ROOT_PATH / 'coms' / 'coms_ui' / 'static' / 'acq'
# COMS_UI_STATIC_ACQUIRE_PATH = ROOT_PATH / 'coms' / 'coms_ui' / 'static' / 'acq'

# # COMS_UI_STATIC_RF_PATH = Path('static') / 'RF'
# COMS_UI_STATIC_RF_PATH = ROOT_PATH / 'virtual-scanner'/ 'coms' / 'coms_ui' / 'static' / 'RF'
# COMS_UI_STATIC_RFTX_PATH = COMS_UI_STATIC_RF_PATH / 'tx'
# COMS_UI_STATIC_RFRX_PATH = COMS_UI_STATIC_RF_PATH / 'rx'
# # COMS_UI_STATIC_RFRX_PATH = Path('static') / 'Rx' / 'outputs'

# # COMS_UI_STATIC_RECON_PATH = Path('static') / 'recon'
# COMS_UI_STATIC_RECON_PATH = ROOT_PATH /'virtual-scanner'/ 'coms' / 'coms_ui' / 'static' / 'recon'
# COMS_UI_STATIC_RX_OUTPUT_PATH = COMS_PATH / 'coms_ui' / 'static' / 'RF' / 'Rx' / 'outputs'
# COMS_UI_STATIC_RX_INPUT_PATH = COMS_PATH / 'coms_ui' / 'static' / 'RF' / 'Rx' / 'inputs'
# COMS_UI_SIM_OUTPUT_PATH = COMS_PATH / 'coms_ui' / 'static' / 'acq' / 'outputs'

# # server
# SERVER_PATH = ROOT_PATH / 'virtual-scanner'/'server'

# # server.ana

# # server.quant_analysis
# SERVER_ANALYZE_PATH = SERVER_PATH / 'ana'

# # server.recon
# RECON_PATH = ROOT_PATH /'virtual-scanner'/ 'server' / 'recon'
# RECON_ASSETS_PATH = RECON_PATH / 'drunck' / 'assets'

# # server.registration

# # server.rf
# RF_SAR_STATIC_IMG_PATH = COMS_UI_PATH / 'static' / 'RF' / 'tx' / 'SAR/'
# RF_SAR_PATH = SERVER_PATH / 'rf' / 'tx' / 'SAR_calc'

# # server.rx
# RX_PATH = SERVER_PATH / 'RF' / 'rx'

# # server.simulation
# SERVER_SIM_BLOCH_PATH = SERVER_PATH / 'simulation' / 'bloch'
# SERVER_SIM_OUTPUT_PATH = SERVER_PATH / 'simulation' / 'outputs'
# SERVER_SIM_BLOCH_PY2JEMRIS_PATH = SERVER_PATH / 'simulation' / 'py2jemris'

# # scanner control paths
# SCANNER_CONTROL = SERVER_PATH/'scanner_control'
# SCANNER_CONTROL_LOG = SCANNER_CONTROL/'log'
# SCANNER_CONTROL_SEQ = SCANNER_CONTROL/'seq'
# SCANNER_CONTROL_SEQ = SCANNER_CONTROL/'seq'
# SCANNER_CONTROL_ACQ_SEQ_FILES = SCANNER_CONTROL_SEQ/'acq_seq_files'
# SCANNER_CONTROL_CAL_SEQ_FILES = SCANNER_CONTROL_SEQ/'cal_seq_files'

# MGH_PATH = './mgh'