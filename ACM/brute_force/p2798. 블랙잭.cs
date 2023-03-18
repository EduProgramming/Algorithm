using System;

namespace Main
{
    class Program
    {
        static void Main(String[] args)
        {
            int[] info = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int N = info[0];
            int M = info[1];

            int[] CARDS = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

            int maxV = 0;
            for (int i=0; i < N-2; i++)
            {
                for (int j=i+1; j < N-1; j++)
                {
                    for (int k=j+1; k < N; k++)
                    {
                        int sumV = CARDS[i] + CARDS[j] + CARDS[k];
                        if (sumV > M) continue;
                        else if (sumV > maxV) maxV = sumV;
                    }
                }
            }

            Console.WriteLine(maxV);
        }
    }
}