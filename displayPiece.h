// File Name: displayPiece.h
// Written By: Christian Gruss
// Date Written: 02/14/2019
//
// This is the header file required for displaying the piece for the results.
// Header files contain definitions required for the display of the results and shape.

#ifndef DISPLAY_PIECE_H
#define DISPLAY_PIECE_H

enum piece_t
{
	left_rectangle,
	right_rectangle,
	left_marker,
	right_marker,
	left_hex,
	right_hex,
	null_piece
};

class displayPiece
{
	public:
		displayPiece();
		~displayPiece();
		void displayPieceTrue();
		void displayPieceFalse();
		
	private:
		displayPiece *n_replaceMe;
		displayPiece *n_piece;
		displayPiece *n_displayPiece;
		piece_t displayPieceIdentifier;
		string displayPieceName;
		displayPiece positionPiece;
		bool createdPiece;
			
};

#endif


