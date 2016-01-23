import json
import os

TABLE_HEADER = "YEP_USE_DISPATCH_TABLE_SECTION const FunctionDescriptor<YepStatus (YEPABI*)(const %s *YEP_RESTRICT, " \
        "const %s *YEP_RESTRICT, %s *YEP_RESTRICT, YepSize)> _dispatchTable_%s[] = {"
IMPLEMENTATION_DESCRIPTION = "YEP_DESCRIBE_FUNCTION_IMPLEMENTATION(_%s, %s, %s, %s, %s, \"asm\", YEP_NULL_POINTER, YEP_NULL_POINTER)"
filename = "Dispatch_Tables.cpp"

x86_64_SIMD_EXTENSIONS = {
    "Nehalem"       : ["YepX86SimdFeatureSSE", "YepX86SimdFeatureSSE2"],
    "SandyBridge"   : ["YepX86SimdFeatureAVX"],
    "Haswell"       : ["YepX86SimdFeatureAVX2", "YepX86SimdFeatureAVX"]
}

x86_64_SYSTEM_FEATURES = {
    ("Nehalem", "Microsoft")        : ["YepX86SystemFeatureXMM"],
    ("SandyBridge", "Microsoft")    : ["YepX86SystemFeatureYMM"],
    ("Haswell", "Microsoft")        : ["YepX86SystemFeatureYMM"],
    ("Nehalem", "SysV")             : ["YepX86SystemFeatureXMM"],
    ("SandyBridge", "SysV")         : ["YepX86SystemFeatureYMM"],
    ("Haswell", "SysV")             : ["YepX86SystemFeatureYMM"]
}

def write_table_header(func_metadata):
    """
    Writes the dispatch table header to the output file
    :param func_metadata JSON metadata generated by PeachPy during compilation
    """
    arg_type_input = filter(lambda arg: arg["name"] == "xPointer", func_metadata["arguments"])[0]["type"]
    arg_type_output = filter(lambda arg: arg["name"] == "zPointer", func_metadata["arguments"])[0]["type"]
    func_name = func_metadata["name"]
    with open(filename, "a") as f:
        f.write(TABLE_HEADER % (arg_type_input, arg_type_input, arg_type_output, func_name))
        f.write('\n')

def write_microsoft_abi(func_metadata):
    target_arch = func_metadata["uarch"]
    isa_extensions = "YepIsaFeaturesDefault"
    simd_extensions = x86_64_SIMD_EXTENSIONS[target_arch]
    system_extensions = x86_64_SYSTEM_FEATURES[(target_arch, "Microsoft")]
    yep_target_arch = "YepCpuMicroarchitecture" + target_arch
    with open(filename, "a") as f:
        f.write(IMPLEMENTATION_DESCRIPTION % (func_metadata["name"], isa_extensions, \
            ' | '.join(simd_extensions), ' | '.join(system_extensions), yep_target_arch))
        f.write('\n')

def write_systemv_abi(func_metadata):
    target_arch = func_metadata["uarch"]
    isa_extensions = "YepIsaFeaturesDefault"
    simd_extensions = x86_64_SIMD_EXTENSIONS[target_arch]
    system_extensions = x86_64_SYSTEM_FEATURES[(target_arch, "SysV")]
    yep_target_arch = "YepCpuMicroarchitecture" + target_arch
    with open(filename, "a") as f:
        f.write(IMPLEMENTATION_DESCRIPTION % (func_metadata["name"], isa_extensions, \
                ' | '.join(simd_extensions), ' | '.join(system_extensions), yep_target_arch))
        f.write('\n')

if __name__ == "__main__":
    build_dir = "library/build/x86_64-osx"
    json_files = filter(lambda f: f.endswith(".json"), os.listdir(build_dir))
    decoder = json.JSONDecoder()
    for json_file in json_files:
        metadata = decoder.decode(' '.join(open(os.path.join(build_dir, json_file), "r").readlines()))
        for func_data in metadata:
            write_table_header(func_data)
            print func_data["name"]
            print func_data["uarch"]
            if func_data["abi"] == "ms":
                write_microsoft_abi(func_data)
            if func_data["abi"] == "SystemV x86-64 ABI":
                write_systemv_abi(func_data)
