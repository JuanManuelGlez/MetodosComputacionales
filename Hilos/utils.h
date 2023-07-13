// =================================================================
//
// File: utils.h
// Author: Pedro Perez
// Description: This file contains the implementation of the
//				functions used to take the time and perform the
//				speed up calculation; as well as functions for
//				initializing integer arrays.
//
// Copyright (c) 2020 by Tecnologico de Monterrey.
// All Rights Reserved. May be reproduced for any non-commercial
// purpose.
//
// =================================================================

#ifndef UTILS_H
#define UTILS_H

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>

#define N 			10
#define DISPLAY		50
#define TOP_VALUE	10000

// =================================================================
// Initializes an array with random values between 1 and TOP_VALUE.
//
// @param array, an array of integer numbers.
// @param size, the amount of numbers.
// =================================================================
void random_array(int *array, int size) {
	int i;

	srand(time(0));
	for (i = 0; i < size; i++) {
		array[i] = (rand() % TOP_VALUE) + 1;
	}
}

// =================================================================
// Initializes a vector with random values between 1 and TOP_VALUE.
//
// @param v, an vector of integer numbers.
// =================================================================
void random_vector(std::vector<int> &v) {
	srand(time(0));
	for (int i = 0; i < v.size(); i++) {
		v[i] = (rand() % TOP_VALUE) + 1;
	}
}

// =================================================================
// Initializes an array with consecutive values of 1 and TOP_VALUE
// across all locations.
//
// @param array, an array of integer numbers.
// @param size, the amount of numbers.
// =================================================================
void fill_array(int *array, int size) {
	int i;

	srand(time(0));
	for (i = 0; i < size; i++) {
		array[i] = (i % TOP_VALUE) + 1;
	}
}

// =================================================================
// Initializes a vector with consecutive values of 1 and TOP_VALUE
// across all locations.
//
// @param v, a vector of integer numbers.
// =================================================================
void fill_vector(std::vector<int> &v) {
	srand(time(0));
	for (int i = 0; i < v.size(); i++) {
		v[i] = (i % TOP_VALUE) + 1;
	}
}


// =================================================================
// Displays the first N locations in the array.
//
// @param array, an array of integer numbers.
// @param size, the amount of numbers.
// =================================================================
void display_array(const char *text, int *array) {
	int i;

	printf("%s = [%4i", text, array[0]);
	for (i = 1; i < DISPLAY; i++) {
		printf(",%4i", array[i]);
	}
	printf(", ... ,]\n");
}

// =================================================================
// Displays the first N locations in the vector.
//
// @param text, a text to be displayed.
// @param v, a vector of integer numbers.
// =================================================================
void display_vector(const char *text, const std::vector<int> &v) {
	int i;

	printf("%s = [%4i", text, v[0]);
	for (i = 1; i < DISPLAY; i++) {
		printf(",%4i", v[i]);
	}
	printf(", ... ,]\n");
}
#endif
