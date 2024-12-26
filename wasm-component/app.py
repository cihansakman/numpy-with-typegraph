import numpy as np
import wasm_np
#from wasm_np import exports
from wasm_np.types import Err
from typing import Union

class WasmNp(wasm_np.WasmNp):
    def multiply(self, a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        try:
            return np.matmul(a, b).tolist()  # type: ignore

        except Exception as e:
            return f"Error during Numpy operations: {e}"        

    def add(self, a: list[list[float]], b: list[list[float]]) -> Union[list[list[float]], str]:
        try:
            return (np.array(a) + np.array(b)).tolist()
        except Exception as e:
            return f"Error during Numpy operation"
    def subtract(self, a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
        try:
            return (np.array(a) - np.array(b)).tolist()
        except Exception as e:
            return f"Error during Numpy operation {e}"
    def transpose(self, a: list[list[float]]) -> list[list[float]]:
        try:
            return np.transpose(a).tolist()
        except Exception as e:
            return f"Error during Numpy operation {e}"
    def invert(self, a: list[list[float]]) -> list[list[float]]:
        try:
            return np.linalg.inv(a).tolist()
        except Exception as e:
            return f"Error during Numpy operation {e}"

    def determinant(self, a: list[list[float]]) -> float:
        try:
            return float(np.linalg.det(a))
        except Exception as e:
            return f"Error during Numpy operation {e}"





