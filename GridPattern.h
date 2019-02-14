// File Name: GridPattern.h
// Written By: Christian Gruss
// Date Written: 02/14/2019
//
// This header file is responsible for placing a grid with pattern movements
// based on Artificial Intelligence onto the mobile app screen.
// Header files contain the definitions required to place the grid and movements
// of the piece on the screen.

#ifndef GRID_PATTERN_H
#define GRID_PATTERN_H

//#include relevant header file(s)

#include <string>

using namespace std;

class GridPattern
{
	public:
		GridPattern();
		~GridPattern();
		void createGrid();
		void displayPiece(int n);
		void removePiece();
		void displayGrid();
		void removeGrid();
		
	private:
		displayPiece *displayGrid;
		string displayPiece;
		int gridSize;
		int currPos;
		int gridMetrics;
		displayRectangle rectanglePos;
		displayRectangle gridPos[10];
		displayPiece grid;
		displayPiece n_back_swap;
		
};

#endif



