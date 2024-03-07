#!/bin/bash

# Check if the user has provided the required arguments
if [ $# -ne 3 ]; then
    echo "Usage: $0 <num_of_numbers> <lower_bound> <upper_bound>"
    exit 1
fi

# Extract user inputs
num_of_numbers=$1
lower_bound=$2
upper_bound=$3

# Validate the range
if [ "$lower_bound" -ge "$upper_bound" ]; then
    echo "Error: Upper bound must be greater than lower bound"
    exit 1
fi

# Generate and display random numbers
for (( i=0; i<num_of_numbers; i++ )); do
    # Generate a random integer
    random=$(( RANDOM ))
    # Scale the random integer to fit within the desired range
    scaled=$(( random % (upper_bound - lower_bound + 1) + lower_bound ))
    echo "Random number $(( i + 1 )): $scaled"
done
