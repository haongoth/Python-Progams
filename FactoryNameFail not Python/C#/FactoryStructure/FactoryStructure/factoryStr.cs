using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryStructure
{
    abstract class Factory
    { public abstract void makeProduct(); }

    class USFactory : Factory
    {
        public override void makeProduct()
        { Console.WriteLine("These products make in US"); }
    }

    class USSatcom : USFactory
    {
        public override void makeProduct()
        { Console.WriteLine("These products make by Satcom in US"); }
    }

    class USCATV : USFactory
    {
        public override void makeProduct()
        { Console.WriteLine("These products make by CATV in US"); }
    }

    class NonUSFactory : Factory
    {
        public override void makeProduct()
        { Console.WriteLine("These products make in China"); }
    }

    class ThailandSatcom : NonUSFactory
    {
        public override void makeProduct()
        { Console.WriteLine("These products make by Satcom in Thailand"); }
    }

    class ChinaCATV : NonUSFactory
    {
        public override void makeProduct()
        { Console.WriteLine("These products make by CATV in China"); }
    }

}
