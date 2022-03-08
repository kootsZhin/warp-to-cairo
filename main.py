from datetime import datetime as dt

import json
import os

from src.constants import *
from src.processor import Processor

def main():
    START_TIME = dt.utcnow()

    for file in os.listdir(INPUTS_PATH):
        e = Processor(INPUTS_PATH, OUTPUTS_PATH, file)
        e.output_cairo_contract()
        e.output_cairo_abis()

    END_TIME = dt.utcnow()

    TIME_CONSUMED = END_TIME - START_TIME
    FILE_COUNT = len(os.listdir(INPUTS_PATH))

    print(f"Successfully converted {FILE_COUNT} files ({TIME_CONSUMED})")

if __name__ == "__main__":
    main()