#include <iostream>
#include <Windows.h>
#include "sgfplib.h"

#pragma comment(lib, "SGFPLib.lib")  // Link the SDK lib

int main() {
    ISGFPDev* sgfplib = nullptr;

    long result = CreateSGFPMObject(&sgfplib);
    std::cout << "CreateSGFPMObject: " << result << std::endl;

    if (!sgfplib) {
        std::cerr << "Failed to create SGFPLib object." << std::endl;
        return 1;
    }

    result = sgfplib->Init(SG_DEV_AUTO);
    std::cout << "SGFPM_Init: " << result << std::endl;

    result = sgfplib->OpenDevice(0);
    std::cout << "SGFPM_OpenDevice: " << result << std::endl;

    int width = 0, height = 0;
    sgfplib->GetImageSize(&width, &height);
    int imageSize = width * height;

    std::cout << "Image size: " << width << " x " << height << std::endl;

    BYTE* imageBuffer = new BYTE[imageSize];

    std::cout << "Place your finger and press Enter..." << std::endl;
    std::cin.get();

    result = sgfplib->GetImage(imageBuffer);
    std::cout << "SGFPM_GetImage: " << result << std::endl;

    FILE* fp = fopen("fingerprint.raw", "wb");
    fwrite(imageBuffer, 1, imageSize, fp);
    fclose(fp);

    std::cout << "Fingerprint saved as fingerprint.raw" << std::endl;

    delete[] imageBuffer;
    sgfplib->CloseDevice();
    sgfplib->Destroy();

    return 0;
}
