#include<iostream>
#include<vector>
#include<cmath>
#include<fstream>

using namespace std;

#define PI acos(-1)


void linspace(int end, vector<float> &output, int dtype=1)
{
    int start = 0;
    int step = 1;
    for(int i=0; i<end; i++)
    {   
        if(dtype)
        {
            output.push_back((float)start);
            start += step;
        }
    }
}

void hann(int &size, vector<float> &output, const int output_datatype=1, bool periodic=true)
{   
    vector<float> linspace_data;
    linspace(size, linspace_data, output_datatype);

    float a0 = 0.5f, a1 = 0.5f;
    if (output_datatype==1)
    {
        if (periodic)  // periodic window
        {
            for(int i=0; i<size;i++)
            {
                output.push_back(a0 - a1 * cos(2 * PI * linspace_data[i] / size));
            }
        }
        else  // symmetric window
        {
            for(int i=0; i<size;i++)
            {
                output.push_back(a0 - a1 * cos(2 * PI * linspace_data[i] / (size - 1)));
            }
        }
    }
}

int main()
{
    int size = 10;

    // 1、symmetric window
    vector<float> output0;
    hann(size, output0, 1, 0);

    fstream input_ofstream("input0.bin", ofstream::out | ofstream::binary);
    input_ofstream.write((char*)(&size), sizeof(int));

    fstream output_ofstream("output0.bin", ofstream::out | ofstream::binary);
    output_ofstream.write((char*)output0.data(), output0.size() * sizeof(float));


    //2、periodic window
    vector<float> output1;
    hann(size, output1, 1, 1);

    fstream input_ofstream1("input1.bin", ofstream::out | ofstream::binary);
    input_ofstream1.write((char*)(&size), sizeof(int));

    fstream output_ofstream1("output1.bin", ofstream::out | ofstream::binary);
    output_ofstream1.write((char*)output1.data(), output1.size() * sizeof(float));

}