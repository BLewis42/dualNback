// File Name: displayMyResults.h
// Written By: Christian Gruss
// Date Written: 02/14/2019
//
// This file is a header file for displaying the results of the user.
// Header files contain definitions required to run the display of results.

#ifndef DISPLAY_MY_RESULTS_H
#define DISPLAY_MY_RESULTS_H

#include <string>
//#include relevant header file(s)

using namespace std;

class displayMyResults
{
	public:
		displayMyResults();
		~displayMyResults();
		void displayPiece(piece_t piece_identifier);
		void removeDisplayPiece(int position);
		
	private:
		ResponseResults* display_Piece[10];
		string n_displayPiecesContainer[10];
		PieceRectangle positionOfPiece[10];
		DisplayPiece* displayPiece;
		piece_t determinePiece[10];	
		
}

#endif



