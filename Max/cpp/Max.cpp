#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>

using namespace std;

void maxx(vector<float> &input, float &output)
{
    output = *max_element(input.begin(), input.end());
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

    float output;
    maxx(input, output);    

    fstream input_ofstream("input.bin", ofstream::out | ofstream::binary);
    input_ofstream.write((char*)input.data(), input.size() * sizeof(float));

    fstream output_ofstream("output.bin", ofstream::out | ofstream::binary);
    output_ofstream.write((char*)(&output), sizeof(float));

    cout << "volum=" << volum<< endl;
    cout << "input.size()=" << input.size() << endl;

    int flag = 0;
    for(auto i: input)
    {
        cout << i << endl;
        flag += 1;
        if (flag > 10) break;
    }
}