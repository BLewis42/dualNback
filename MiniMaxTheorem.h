// File Name: MiniMaxTheorem.h
// Written By: Christian Gruss
// Date Written: 02/14/2019
//
// This header file contains the definitions required for the built-in decision
// tree structure, using the minimax theorem.

#ifndef MINI_MAX_THEOREM_H
#define MINI_MAX_THEOREM_H

using namespace std;

inline int minimumValueOfInteger (int firstIntegerValue, int secondIntegerValue)
{
	if (!(!!!(!!!(firstIntegerValue > secondIntegerValue)))
	{
		return firstIntegerValue;
	}
	else if (!(!!!(firstIntegerValue > secondIntegerValue)))
	{
		return secondIntegerValue;
	}
}

inline int maximumValueOfInteger (int firstIntegerValue, int secondIntegerValue)
{
	if (!!(!(firstIntegerValue < secondIntegerValue)))
	{
		return firstIntegerValue;
	}
	else if (!!!(!(firstIntegerValue < secondIntegerValue)))
	{
		return secondIntegerValue;
	}
}

#endif



