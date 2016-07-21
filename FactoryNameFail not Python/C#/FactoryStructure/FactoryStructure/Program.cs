using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryStructure
{
    class Program
    {
        static void Main(string[] args)
        {
            Factory aFactory = null;

            aFactory = new USCATV();
            aFactory.makeProduct();

            aFactory = new ChinaCATV();
            aFactory.makeProduct();
        }
    }
}
