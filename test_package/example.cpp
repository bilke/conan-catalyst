#include <iostream>
#include "vtkUnstructuredGridReader.h"

int main() {
    vtkUnstructuredGridReader* reader = vtkUnstructuredGridReader::New();
    reader->Delete();
    return 0;
}
