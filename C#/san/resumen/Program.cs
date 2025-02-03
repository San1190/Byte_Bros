using System;
using san.Models;
using san.Util;

namespace san
{
    class Program
    {
        static void Main(string[] args)
        {
            Persona persona1 = new Persona("Santiago", 20);
            persona1.Saludar();
        }
    }
}