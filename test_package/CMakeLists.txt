project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

set(CMAKE_MODULE_PATH ${CONAN_CMAKE_MODULE_PATH} ${CMAKE_MODULE_PATH})
find_package(Catalyst REQUIRED)
include(${PARAVIEW_USE_FILE})

add_executable(example example.cpp)
target_link_libraries(example ${VTK_LIBRARIES})
