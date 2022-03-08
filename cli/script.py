from datetime import datetime as dt

import click
import json
import os

from cli.utils.constants import *
from cli.utils.processor import Processor

@click.command()
def convert():
    START_TIME = dt.utcnow()

    for file in os.listdir(INPUTS_PATH):
        e = Processor(INPUTS_PATH, OUTPUTS_PATH, file)
        e.output_cairo_contract()
        e.output_cairo_abis()

    END_TIME = dt.utcnow()

    TIME_CONSUMED = END_TIME - START_TIME
    FILE_COUNT = len(os.listdir(INPUTS_PATH))

    click.echo(f"Successfully converted {FILE_COUNT} files ({TIME_CONSUMED})")

if __name__ == "__main__":
    convert()