## Implementing WebAssembly with Numpy in Typegraph  

This is a basic demo showcasing the implementation of Numpy functionalities in WebAssembly (Wasm) and deploying it to a Metatype Typegraph.  

Using the GraphQL UI, users can perform basic Numpy operations, including matrix:  
- Addition  
- Subtraction  
- Multiplication  
- And more  

The example has been extended to include file analysis with the following [repo](https://github.com/cihansakman/numpy-w-wasm). For this project, the Wasm component does not expect a file path, instead, it accepts CSV-like strings and analyzes them similarly using both Numpy and Regex via Metatype's GraphQL UI.

### Pipeline  

1. **Compile the Wasm Component**  
   Navigate to the `wasm-component` directory and compile the Wasm component.  

2. **Deploy the Typegraph**  
   Deploy the Typegraph by working within the `tg` directory. 