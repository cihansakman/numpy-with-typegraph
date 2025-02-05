import numpy as np
import wasm_np
#from wasm_np import exports
from wasm_np.types import Err
from typing import Union
from utils import *

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

    #Take a string like csv like input and print-out an
    #analysis of it.
    def analyze(sef, a: str) -> str:
        try:
            data = load_data(a)
            result = ""
        
            # General info about the dataset
            column_names = data.dtype.names
            num_rows = len(data)
            num_columns = len(column_names)
            result += (f"\n=== General Outline of Provided Data ===")
            result += (f"\nNumber of rows: {num_rows}")
            result += (f"\nNumber of columns: {num_columns}")
            result += (f"\nColumn names: {', '.join(column_names)}\n")
        
            report = analyze_data(data)
        
            result += ("\n\n=== Analysis Report ===")
            for col, analysis in report.items():
                result += f"\n\nColumn: {col}"
                for key, value in analysis.items():
                    result += f"\n\t{key}: {value}"
            
            return result
        
        except Exception as e:
            return f"Error during Analyze operation {e}"



