using System;

namespace Main
{
    class Program
    {
        static void Main(String[] args)
        {
            int money = 1000 - int.Parse(Console.ReadLine());
            int maxChange = 500;

            bool isTen = false; 
            int result = 0;

            while (maxChange > 0)
            {
                int cnt = money / maxChange;
                money = money % maxChange;
                result = result + cnt;

                if (isTen) {
                    maxChange = maxChange / 2;
                } else {
                    maxChange = maxChange / 5;
                }
                isTen = !isTen;
            }

            Console.WriteLine(result);
        }
    }
}