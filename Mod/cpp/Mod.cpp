#include<iostream>
#include<vector>
#include<cmath>
#include<cassert>

using namespace std;

template<typename T>
void mod(vector<T> &input0, vector<T> &input1, vector<T> &output, const int fmod_=1)
{
    assert (fmod_ == 1 || fmod_ ==0), "fmod 输入不合法";
    int size = input0.size();
    for(int i=0; i<size; i++)
    {
        if(fmod_)
        {
            output.push_back(fmod(input0[i], input1[i]));
        } 
        else
        {
            output.push_back(input0[i] - (input0[i] / input1[i]) * input1[i]);
            // output.push_back(input0[i] % input1[i]);
        } 
    }
}


int main()
{

    /*
        1、test1
    */
   vector<float> input0 = {-4.3, 7.2, 5.0, 4.3, -7.2, 8.0};
   vector<float> input1 = {2.1, -3.4, 8.0, -2.1, 3.4, 5.0};

   vector<float> output_fp;  // {-0.1,  0.4,  5. ,  0.1, -0.4,  3.}
   mod(input0, input1, output_fp, 1);
   
   cout << "\ntest1:" << endl;
   for(float item: output_fp)
   {
    cout << item << endl;
   }

   /*
        2、test2
   */
   vector<float> input00 = {-4, 7, 5, 4, -7, 8};
   vector<float> input11 = {2, -3, 8, -2, 3, 5};

   vector<float> output_float1;  // { 0,  1,  5,  0, -1,  3}
   mod(input00, input11, output_float1, 1);
   
   cout << "\ntest2:" << endl;
   for(float item: output_float1)
   {
    cout << item << endl;
   }

    /*
        3、test3
   */
   vector<int> input000 = {-4, 7, 5, 4, -7, 8};
   vector<int> input111 = {2, -3, 8, -2, 3, 5};

   vector<int> output_int;  // { 0, -2,  5,  0,  2,  3}
   mod(input000, input111, output_int, 0);

   cout << "\ntest3:" << endl;
   for(float item: output_int)
   {
    cout << item << endl;
   }

   cout << 7 % -3 << endl;
   cout << 5 % 8 << endl;
}