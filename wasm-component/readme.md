# Custom Numpy build with componentize-py

## NumPy and Regex for target wasm32_unknown_wasi
The `componentize-py` team has developed custom Numpy and Regex builds that targets `wasm32-unknown-wasi`, allowing it to run within any WASI-supported WebAssembly runtime. Additionally, other native Python libraries compatible with `wasm32-wasi` can be found in this [repository](https://github.com/dicej/wasi-wheels/), which includes custom builds of popular libraries.

### Get the wasi compiled pakcages from wasi-wheels or built them yourself
```
curl -OL https://github.com/dicej/wasi-wheels/releases/download/latest/numpy-wasi.tar.gz
curl -OL https://github.com/dicej/wasi-wheels/releases/download/latest/regex-wasi.tar.gz
tar xf numpy-wasi.tar.gz
tar xf regex-wasi.tar.gz
```

## Compile it to Wasm component

By default, componentize-py includes the `wasi:cli` world. To handle this, use the `--stub-wasi` flag to provide dummy implementations for these worlds during compilation:

```
componentize-py -d wit/ -w wasm-np componentize --stub-wasi app -o wasm-np.wasm
```
