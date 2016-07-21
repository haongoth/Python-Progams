#pragma once

#include<iostream>

class Factory abstract
{
public:
	virtual void makeProduct() = 0;
};

class USFactory : Factory
{
public:
	virtual void makeProduct() override
	{
		std::cout << "These products make in US";
	}
};

class NonUSFactory : Factory
{
public:
	virtual void makeProduct() override
	{
		std::cout << "These products make in China";
	}
};

class Satcom : USFactory
{
public:
	virtual void makeProduct() override
	{
		std::cout << "These products make inThese products make by Satcom department in US";
	}
};

class CATV : USFactory 
{
public:
	virtual void makeProduct() override
	{
		std::cout << "These products make inThese products make by CATV department in US";
	}
};

class Satcom : NonUSFactory
{
public:
	virtual void makeProduct() override
	{
		std::cout << "These products make inThese products make by Satcom department in Thailand";
	}
};

class CATV : NonUSFactory
{
public:
	virtual void makeProduct() override
	{
		std::cout << "These products make inThese products make by CATV department in China";
	}
};