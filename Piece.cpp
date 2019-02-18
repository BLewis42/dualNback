/*
 * Piece.cpp
 *
 *  Created on: Feb 18, 2019
 *      Author: macintosh
 */

#include "Piece.h"

Piece::Piece() 
{
	// Left intentionally blank...
}

Piece::~Piece() 
{
	// Left intentionally blank...
}

void Piece::builtPiece(int N)
{
	NValue = N;
	
	TrainData_image.init(N);
	TrainData_image.generateGridMarkers();
	TrainData_image.setMask();
	TrainData_image.makeDistractors();
	TrainData_image.makeRandomFill();
}

Pot_t Piece::getAIVal(int pos)
{
	Pot_t pot_values;
	pot_values.imageDest = TrainData_image.getGridVal(pos);
	return pot_values;
}

Grid_t Piece::getPotMarker(int pos)
{
	Grid_t grid_values;
	grid_piece.imageYesNo = TrainData_image.getGridPos(pos);
	return grid_values;
}


