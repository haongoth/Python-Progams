// FactoryStruct.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Factory.h"


int main()
{
	
	 Factory aFactory = new USCATV();
	
	aFactory.makeProduct();
    return 0;
}

