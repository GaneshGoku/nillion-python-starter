from nada_dsl import *

def nada_main():
    # Define the party involved in the computation
    party1 = Party(name="Party1")
    
    # Define secret integer inputs for the party
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    my_int3 = SecretInteger(Input(name="my_int3", party=party1))

    # Perform the computation - calculating the average of three secret integers
    # Sum the three secret integers
    sum_of_ints = my_int1 + my_int2 + my_int3
    
    # Define the count of numbers being averaged
    count = SecretInteger(3)
    
    # Calculate the average using integer division
    average = sum_of_ints // count  # Integer division to get the average

    # Define the output of the computation
    output = Output(average, "average_result", party1)
    
    # Return the output as a list (potentially allowing for multiple outputs in the future)
    return [output]

# Run the nada_main function
nada_main()
