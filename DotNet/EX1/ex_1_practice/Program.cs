using System;

namespace ex_1_practice
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("It's Working!");
            var name = Console.ReadLine();
            var dateTime = DateTime.Now.Year;
            Console.WriteLine($"{name}, on {dateTime}");
        }
    }
}
