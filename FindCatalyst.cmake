set(ParaView_DIR ${CONAN_CATALYST_ROOT})
include(${CONAN_CATALYST_ROOT}/lib/cmake/paraview-5.4/ParaViewConfig.cmake)

mark_as_advanced(
	ParaView_DIR
)