## Deploy the Typegraph
Load the pre-compiled Wasm component using `WasmRuntime.reflected()` and expose it's export functions.

Deploy it using following command
```
meta
meta deploy -f api/numpy_demo.py --allow-dirty --create-migration --target dev --gate http://localhost:7890
```

Test it with the following queries via GraphQL:
```
query MultiplyWasm {
	wasm_mul(
    a: [[1, 2, 3], [4, 5, 6]],
    b: [[7, 8], [9, 10], [11, 12]]
  )
}

query AddWasm {
	wasm_add(
    a: [[1, 2, 3], [4, 5, 6]],
    b: [[1, 2, 3], [4, 5, 9]]
  )
}

query SubtractWasm {
  wasm_sub(
    a: [[10, 20, 30], [40, 50, 60]],
    b: [[5, 15, 25], [30, 40, 50]]
  )
}

query TransposeWasm {
  wasm_transpose(
    a: [[1, 2, 3, 4], [5, 6, 7, 8]]
  )
}

query InvertWasm {
  wasm_invert(
    a: [[4, 7], [2, 6]]
  )
}

query DeterminantWasm {
  wasm_determinant(
    a: [[4, 1], [2, 3]]
  )
}

query AnalyzeWasm {
  wasm_analyze(
    a: 
    """
Id,Name,Age,Cost,Category
1,John,25,100,Food
2,Jane,30,150,Electronics
3,Doe,35,200,Food
6,Cihan,40,99,IT
7,Teo,33,120,IT
8,Ciho,24,210,Worker
    """
  )
}
```