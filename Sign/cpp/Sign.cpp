#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

void sign(vector<float> &input, vector<float> &output)
{
    for(float x: input)
    {
        if (x < 0)  output.push_back(-1.);
        if (x = 0)  output.push_back(0.);
        if (x > 0)  output.push_back(1.);
    }
}

int main()
{
    srand(1001);

    int low = -10;
    int high = 10;
    int size[] = {1,3,64,64};

    int volum = 1;
    for(int item: size)
    {
        volum *= item;
    }

    vector<float> input;
    for(int i=0; i<volum; i++)
    {
        input.push_back(rand() % high + low);
    }

    vector<float> output;
    sign(input, output);

    fstream input_ofstream("input.bin", ofstream::out | ofstream::binary);
    input_ofstream.write((char*)input.data(), input.size() * sizeof(float));

    fstream output_ofstream("output.bin", ofstream::out | ofstream::binary);
    output_ofstream.write((char*)output.data(), output.size() * sizeof(float));

    cout << "volum=" << volum<< endl;
    cout << "input.size()=" << input.size() << endl;
    cout << "output.size()=" << output.size() << endl;

    int flag = 0;
    for(auto i: input)
    {
        cout << i << endl;
        flag += 1;
        if (flag > 10) break;
    }
}