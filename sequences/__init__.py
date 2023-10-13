from importlib import import_module
from pathlib import Path
from typing import Dict, TypeVar, Generic
from utils import constants
from uuid import uuid4
import os

SequenceVar = TypeVar("SequenceVar")


class SequenceBase(Generic[SequenceVar]):
    """
    Base class for all console sequences, including automatic registry for sequence classes.
    """

    ## Internal functions for the sequence registry

    _REGISTRY: Dict[str, SequenceVar] = {}

    def __init_subclass__(cls, registry_key, **kwargs):
        super().__init_subclass__(**kwargs)
        if registry_key:
            cls._REGISTRY[registry_key] = cls
            cls.seq_name = registry_key

    seq_name = "INVALID"
    parameters: Dict = {}

    def __init__(self):
        pass

    @classmethod
    def get_sequence(cls, registry_key):
        return cls._REGISTRY[registry_key]

    @classmethod
    def installed_sequences(cls):
        return list(cls._REGISTRY.keys())

    ## Sequence API functions

    def get_name(self) -> str:
        """
        Returns the internal name of the sequence.
        """
        return self.seq_name

    @classmethod
    def get_readable_name(self) -> str:
        """
        Returns a human-readable name of the sequence.
        """
        return "INVALID"

    def set_parameters(self, parameters) -> bool:
        """
        Reads the sequence parameters from a JSON dictionary.
        """
        return True

    def get_settings(self) -> dict:
        """
        Returns the current sequence parameters as JSON dict.
        """
        return {}

    def setup_ui(self, widget) -> bool:
        """
        Creates the user interface of the sequence.
        """
        return True

    def write_parameters_to_ui(self, widget) -> bool:
        """
        Write the internal settings to the UI, which lives inside the widget.
        """
        return True

    def read_parameters_from_ui(self) -> bool:
        """
        Reads the settings from the UI into the sequence.
        """
        return True

    def calculate_sequence(self) -> bool:
        """
        Calculates the sequence instructions.
        """
        return True

    def is_adjustment_sequence(self) -> bool:
        """
        Returns True if the sequence is an adjustment sequence.
        """
        if self.seq_name.startswith("adj_"):
            return True
        return False


class PulseqSequence(SequenceBase[SequenceVar], registry_key=""):
    def store_seq_file(self, file_name: str = "", seq=None) -> str:
        """
        Store the seq file in the randomly generated folder
        """
        # TODO: Folders should not be created by the sequence. Needs to be moved to framework code.

        dirname_seq = str(uuid4())
        if (os.path.isdir(constants.DATA_PATH_ACQ)) is False:
            os.mkdir("/opt/mri4all/data")
            os.mkdir("/opt/mri4all/data")
        os.mkdir(os.path.join(constants.DATA_PATH_ACQ, dirname_seq))
        path_to_save = os.path.join(constants.DATA_PATH_ACQ, dirname_seq, file_name)
        seq.write(os.path.join(path_to_save))

        return path_to_save


# Automatically import all sequence classes existing in the /sequences directory.
# Sequence classes must provide only one Python file in the sequences directory,
# and it must be named the same as the class name. Helper files must be placed in a
# subdirectory to the sequence directory

for f in Path(__file__).parent.glob("*.py"):
    module_name = f.stem
    if (not module_name.startswith("_")) and (module_name not in globals()):
        import_module(f".{module_name}", __package__)
    del f, module_name
del import_module, Path
