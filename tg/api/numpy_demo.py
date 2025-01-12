from typegraph import typegraph, Policy, t, Graph
from typegraph.runtimes.wasm import WasmRuntime


@typegraph()
def np_functions(g: Graph):
    pub = Policy.public()
    #Call wasm component
    wasm = WasmRuntime.reflected("/home/cihan/metatype/metatype-np-demo/wasm-component/wasm-np.wasm")
    #wasm = WasmRuntime.reflected("/path/to/wasm/component.wasm")

    #Expose functions public
    g.expose(
        pub, # make all functions public by default
        wasm_mul = wasm.export(
            t.struct({
                    "a": t.list(t.list(t.float())),
                    "b": t.list(t.list(t.float())),
                    }),
            t.union([
                t.list(t.list(t.float())),
                t.string(),
            ]),
            name="multiply", #exported function
                            ),
        wasm_add = wasm.export(
            t.struct({
                    "a": t.list(t.list(t.float())),
                    "b": t.list(t.list(t.float())),
                    }),
            t.union([
                t.list(t.list(t.float())),
                t.string(),
            ]),
            name="add", #exported function
                            ),
        wasm_sub = wasm.export(
            t.struct({
                    "a": t.list(t.list(t.float())),
                    "b": t.list(t.list(t.float())),
                    }),
            t.union([
                t.list(t.list(t.float())),
                t.string(),
            ]),
            name="subtract", #exported function
                            ),
        wasm_transpose = wasm.export(
            t.struct({
                    "a": t.list(t.list(t.float())),
                    }),
            t.union([
                t.list(t.list(t.float())),
                t.string(),
            ]),
            name="transpose", #exported function
                            ),
        wasm_invert = wasm.export(
            t.struct({
                    "a": t.list(t.list(t.float())),
                    }),
            t.union([
                t.list(t.list(t.float())),
                t.string(),
            ]),
            name="invert", #exported function
                            ),
        wasm_determinant = wasm.export(
            t.struct({
                    "a": t.list(t.list(t.float())),
                    }),
            t.union([
                t.list(t.float()),
                t.string(),
            ]),
            name="determinant", #exported function
                            ),
        wasm_analyze = wasm.export(
            t.struct({
                    "a": t.string(),
                    }),
            t.string(),
            name="analyze", #exported function
                            ),
    )
