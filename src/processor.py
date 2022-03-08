import json

class Processor:
    def __init__(self, inputs_path, outputs_path, file_name):
        self.INPUTS_PATH = f"{inputs_path}/{file_name}"
        self.OUTPUT_PATH = outputs_path

        self.FILE_NAME = file_name.split(".")[0]

        self.CONTRACTS_OUTPUTS_PATH = f"{self.OUTPUT_PATH}/{self.FILE_NAME}.cairo"
        self.ABIS_OUTPUTS_PATH = f"{self.OUTPUT_PATH}/abis/{self.FILE_NAME}.json"

        self._open_input_json()
    
    def _open_input_json(self):
        f = open(self.INPUTS_PATH)
        self.INPUTS_JSON = json.load(f)
        f.close()

    def output_cairo_contract(self):
        contract = self.INPUTS_JSON["cairo_code"]
        outputs = open(self.CONTRACTS_OUTPUTS_PATH, "w")
        outputs.write(contract)
        outputs.close()

    def output_cairo_abis(self):
        abi = json.dumps(self.INPUTS_JSON["sol_abi"])
        outputs = open(self.ABIS_OUTPUTS_PATH, "w")
        outputs.write(abi)
        outputs.close()