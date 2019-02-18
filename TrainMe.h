// File Name: TrainMe.h
// Written By: Christian Gruss
// Date Written: 04/18/2019
//
// This header file is responsible for selection of targeting stimuli during the
// N-Back test. It is the training set for the N-Back test stimuli. This header
// file contains information for visual target stimuli.


#ifndef TRAIN_ME_H
#define TRAIN_ME_H


#include <vector>


enum stimuli_visual_t
{
	VALID_TARGET,
	NON_VALID_TARGET
};


#define NUMERICAL_STIMULI_AMOUNT 50

using namespace std;


class TrainMe
{
	public:
		TrainMe();
		~TrainMe();
		void initialStimuli(int N);
		void selectGridPosForStimuli(int numberOfBlocks);
		void duplicateMyGridPos(const TrainMe& trainMyObject);
		void createGridVals();
		void createTransitions();
		void createGridMarkersRandomized();
		int getValForGrid(int pos);
		stimuli_grid_t getGridPos(int pos);
	
	private:
		vector<int> TrainMe;
		vector<stimuli_grid_t> GridMarkers; 
		vector<int> vacantGridMarkers;
		vector<int> vacantGrids;
		vector<int> occupiedGridMarkers;
		int NBackVal;
		void createFirstStimuli();
		void createSecondStimuli();
		void randomizeMe();
		void inhibitGrid(int pos);
		void anyConstraints(int pos);
		void clearGrid();
		void clearGridMarker(int n);
		void clearCurrGridMarker(int n, vector<int>& vacantMarkers);
		int randomizeGrid(int minimumVal, int maximumVal);
};

#endif



