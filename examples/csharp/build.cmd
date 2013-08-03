set CSC=csc
set CSCFLAGS=/nologo /optimize+ /target:exe /unsafe /reference:%YEPROOT%\binaries\clr-2.0\yeppp-clr.dll
set CP=copy
set CPFLAGS=/Y
set RM=del
set RMFLAGS=/f /s /q
set MKDIR=mkdir
set MKDIRFLAGS=

%RM% %RMFLAGS% "binaries" >NUL 2>NUL
%MKDIR% %MKDIRFLAGS% "binaries" >NUL 2>NUL

%CSC% %CSCFLAGS% /out:binaries/Polynomial.exe sources\Polynomial.cs

%CSC% %CSCFLAGS% /out:binaries/PolynomialF.exe sources\PolynomialF.cs

%CSC% %CSCFLAGS% /out:binaries/CpuCycles.exe sources\CpuCycles.cs

%CSC% %CSCFLAGS% /out:binaries/CpuInfo.exe sources\CpuInfo.cs

%CSC% %CSCFLAGS% /out:binaries/Entropy.exe sources\Entropy.cs

%CSC% %CSCFLAGS% /out:binaries/SystemTimer.exe sources\SystemTimer.cs

%CP% %CPFLAGS% %YEPROOT%\binaries\clr-2.0\yeppp-clr.dll binaries\yeppp-clr.dll >NUL 2>NUL