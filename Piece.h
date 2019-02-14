// File Name: Piece.h
// Written By: Christian Gruss
// Date Written: 02/14/2019
//
// This header file contains the definitions for the piece on the grid.

#ifndef PIECE_H
#define PIECE_H

#include <vector>
// include addl header

typedef struct
{
	int audioPot;
	int imagePot;
}
Pot_t;

typedef struct
{
	pot_piece_audioYesNo;
	pot_piece_imageYesNo;
}
Pot_t;

class Piece
{
	public:
		Piece();
		~Piece();
		void builtPiece(int N);
		Pot_t getAIVal(int pos);
		pot_t getPotMarker(int pos);
		
	private:
		TrainData n_TrainData_audio;
		TrainData n_TrainData_image;
		int n_Numerical;
};

#endif



// File Name: Piece.h
// Written By: Christian Gruss
// Date Written: 02/14/2019
//
// This header file contains the definitions for the piece on the grid.

#ifndef PIECE_H
#define PIECE_H

#include <vector>
// include addl header

typedef struct
{
	int audioPot;
	int imagePot;
}
Pot_t;

typedef struct
{
	pot_piece_audioYesNo;
	pot_piece_imageYesNo;
}
Pot_t;

class Piece
{
	public:
		Piece();
		~Piece();
		void builtPiece(int N);
		Pot_t getAIVal(int pos);
		pot_t getPotMarker(int pos);
		
	private:
		TrainData n_TrainData_audio;
		TrainData n_TrainData_image;
		int n_Numerical;
};

#endif



