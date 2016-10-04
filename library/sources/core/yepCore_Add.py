import peachpy.x86_64.uarch as uarch
import peachpy.x86_64.isa as isa
from peachpy.x86_64.function import Function
from peachpy.function import Argument
from peachpy.c.types import ptr
import peachpy.c.types as ctypes
from kernels.binop.binop_VV_V import binop_VV_V
from kernels.binop.binop_VS_V import binop_VS_V
from kernels.binop.binop_IVV_IV import binop_IVV_IV
from kernels.binop.binop_IVS_IV import binop_IVS_IV
from common.YepStatus import YepStatus

# =======================================================================
# =======================================================================
# ADD VECTOR TO VECTOR
# =======================================================================
# =======================================================================
arg_x = Argument(ptr(ctypes.const_Yep8s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep8s), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep8s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V8sV8s_V8s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V8sV8s_V8s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V8sV8s_V8s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V8sV8s_V8s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep8s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep8s), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep16s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V8sV8s_V16s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V8sV8s_V16s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V8sV8s_V16s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V8sV8s_V16s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep8u), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep8u), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep16u), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V8uV8u_V16u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V8uV8u_V16u:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V8uV8u_V16u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V8uV8u_V16u:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep16s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep16s), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep16s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V16sV16s_V16s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V16sV16s_V16s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V16sV16s_V16s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V16sV16s_V16s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep16s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep16s), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep32s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V16sV16s_V32s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V16sV16s_V32s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V16sV16s_V32s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V16sV16s_V32s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep16u), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep16u), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep32u), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V16uV16u_V32u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V16uV16u_V32u:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V16uV16u_V32u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V16uV16u_V32u:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep32s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep32s), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep32s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V32sV32s_V32s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V32sV32s_V32s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V32sV32s_V32s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V32sV32s_V32s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep32s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep32s), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep64s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V32sV32s_V64s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V32sV32s_V64s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V32sV32s_V64s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V32sV32s_V64s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep32u), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep32u), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep64u), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V32uV32u_V64u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V32uV32u_V64u:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V32uV32u_V64u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V32uV32u_V64u:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep64s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep64s), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep64s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V64sV64s_V64s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V64sV64s_V64s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V64sV64s_V64s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V64sV64s_V64s:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep32f), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep32f), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep32f), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V32fV32f_V32f",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V32fV32f_V32f:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V32fV32f_V32f",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V32fV32f_V32f:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep64f), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep64f), name="yPointer")
arg_z = Argument(ptr(ctypes.Yep64f), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V64fV64f_V64f",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V64fV64f_V64f:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V64fV64f_V64f",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V64fV64f_V64f:
    binop_VV_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



# =======================================================================
# =======================================================================
# ADD SCALAR TO VECTOR
# =======================================================================
# =======================================================================
arg_x = Argument(ptr(ctypes.const_Yep8s), name="xPointer")
arg_y = Argument(ctypes.Yep8s, name="y")
arg_z = Argument(ptr(ctypes.Yep8s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V8sS8s_V8s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V8sS8s_V8s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V8sS8s_V8s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V8sS8s_V8s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep8s), name="xPointer")
arg_y = Argument(ctypes.Yep8s, name="y")
arg_z = Argument(ptr(ctypes.Yep16s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V8sS8s_V16s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V8sS8s_V16s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V8sS8s_V16s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V8sS8s_V16s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep8u), name="xPointer")
arg_y = Argument(ctypes.Yep8u, name="y")
arg_z = Argument(ptr(ctypes.Yep16u), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V8uS8u_V16u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V8uS8u_V16u:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V8uS8u_V16u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V8uS8u_V16u:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep16s), name="xPointer")
arg_y = Argument(ctypes.Yep16s, name="y")
arg_z = Argument(ptr(ctypes.Yep16s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V16sS16s_V16s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V16sS16s_V16s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V16sS16s_V16s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V16sS16s_V16s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep16s), name="xPointer")
arg_y = Argument(ctypes.Yep16s, name="y")
arg_z = Argument(ptr(ctypes.Yep32s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V16sS16s_V32s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V16sS16s_V32s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V16sS16s_V32s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V16sS16s_V32s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep16u), name="xPointer")
arg_y = Argument(ctypes.Yep16u, name="y")
arg_z = Argument(ptr(ctypes.Yep32u), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V16uS16u_V32u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V16uS16u_V32u:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V16uS16u_V32u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V16uS16u_V32u:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep32s), name="xPointer")
arg_y = Argument(ctypes.Yep32s, name="y")
arg_z = Argument(ptr(ctypes.Yep32s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V32sS32s_V32s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V32sS32s_V32s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V32sS32s_V32s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V32sS32s_V32s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep32s), name="xPointer")
arg_y = Argument(ctypes.Yep32s, name="y")
arg_z = Argument(ptr(ctypes.Yep64s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V32sS32s_V64s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V32sS32s_V64s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V32sS32s_V64s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V32sS32s_V64s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep32u), name="xPointer")
arg_y = Argument(ctypes.Yep32u, name="y")
arg_z = Argument(ptr(ctypes.Yep64u), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V32uS32u_V64u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V32uS32u_V64u:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V32uS32u_V64u",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V32uS32u_V64u:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep64s), name="xPointer")
arg_y = Argument(ctypes.Yep64s, name="y")
arg_z = Argument(ptr(ctypes.Yep64s), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V64sS64s_V64s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V64sS64s_V64s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V64sS64s_V64s",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V64sS64s_V64s:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.const_Yep32f), name="xPointer")
arg_y = Argument(ctypes.Yep32f, name="y")
arg_z = Argument(ptr(ctypes.Yep32f), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V32fS32f_V32f",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V32fS32f_V32f:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V32fS32f_V32f",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V32fS32f_V32f:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")


arg_x = Argument(ptr(ctypes.const_Yep64f), name="xPointer")
arg_y = Argument(ctypes.Yep64f, name="y")
arg_z = Argument(ptr(ctypes.Yep64f), name="zPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_V64fS64f_V64f",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_V64fS64f_V64f:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "AVX2")

with Function("yepCore_Add_V64fS64f_V64f",
        (arg_x, arg_y, arg_z, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_V64fS64f_V64f:
    binop_VS_V(arg_x, arg_y, arg_z, arg_n, "add", "SSE")



# =======================================================================
# =======================================================================
# ADD VECTOR INPLACE
# =======================================================================
# =======================================================================
arg_x = Argument(ptr(ctypes.Yep8s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep8s), name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV8sV8s_IV8s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV8sV8s_IV8s:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV8sV8s_IV8s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV8sV8s_IV8s:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep16s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep16s), name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV16sV16s_IV16s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV16sV16s_IV16s:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV16sV16s_IV16s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV16sV16s_IV16s:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep32s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep32s), name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV32sV32s_IV32s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV32sV32s_IV32s:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV32sV32s_IV32s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV32sV32s_IV32s:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep64s), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep64s), name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV64sV64s_IV64s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV64sV64s_IV64s:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV64sV64s_IV64s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV64sV64s_IV64s:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep32f), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep32f), name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV32fV32f_IV32f",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV32fV32f_IV32f:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV32fV32f_IV32f",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV32fV32f_IV32f:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep64f), name="xPointer")
arg_y = Argument(ptr(ctypes.const_Yep64f), name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV64fV64f_IV64f",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV64fV64f_IV64f:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV64fV64f_IV64f",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV64fV64f_IV64f:
    binop_IVV_IV(arg_x, arg_y, arg_n, "add", "SSE")



# =======================================================================
# =======================================================================
# ADD SCALAR TO INPLACE VECTOR
# =======================================================================
# =======================================================================
arg_x = Argument(ptr(ctypes.Yep8s), name="xPointer")
arg_y = Argument(ctypes.Yep8s, name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV8sS8s_IV8s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV8sS8s_IV8s:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV8sS8s_IV8s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV8sS8s_IV8s:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep16s), name="xPointer")
arg_y = Argument(ctypes.Yep16s, name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV16sS16s_IV16s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV16sS16s_IV16s:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV16sS16s_IV16s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV16sS16s_IV16s:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep32s), name="xPointer")
arg_y = Argument(ctypes.Yep32s, name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV32sS32s_IV32s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV32sS32s_IV32s:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV32sS32s_IV32s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV32sS32s_IV32s:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep64s), name="xPointer")
arg_y = Argument(ctypes.Yep64s, name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV64sS64s_IV64s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV64sS64s_IV64s:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV64sS64s_IV64s",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV64sS64s_IV64s:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep32f), name="xPointer")
arg_y = Argument(ctypes.Yep32f, name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV32fS32f_IV32f",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV32fS32f_IV32f:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV32fS32f_IV32f",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV32fS32f_IV32f:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "SSE")



arg_x = Argument(ptr(ctypes.Yep64f), name="xPointer")
arg_y = Argument(ctypes.Yep64f, name="yPointer")
arg_n = Argument(ctypes.YepSize, name="length")

with Function("yepCore_Add_IV64fS64f_IV64f",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.haswell + isa.avx2) as yepCore_Add_IV64fS64f_IV64f:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "AVX2")

with Function("yepCore_Add_IV64fS64f_IV64f",
        (arg_x, arg_y, arg_n),
        YepStatus, target=uarch.nehalem + isa.sse2) as yepCore_Add_IV64fS64f_IV64f:
    binop_IVS_IV(arg_x, arg_y, arg_n, "add", "SSE")