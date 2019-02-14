// File Name: ClassOfStrings.h
// Written By: Christian Gruss
// Date Written: 02/14/2019
//
// This header file contains the definitions required to prove a String class.
// Header files contain definitions required to provide String capabilities
// such as StringBuilder in Java, to port to C++ programming language.

#ifndef CLASS_OF_STRINGS_H
#define CLASS_OF_STRINGS_H

enum displayMe_t
{
	emptyBox = 1 << 0,
	gridMe = 1 << 1,
	gridBox = 1 << 2
};

typedef struct
{
	int firstPos;
	int secondPos;
} placement_t;

typedef struct
{
	int gridBoxDesign;
	int colorMyGridRed;
	int colorMyGridGreen;
	int colorMyGridBlue;
	int gridRed;
	int gridGreen;
	int gridBlue;
	gridset_t Grid;
} boxDisplay_t;

#endif



