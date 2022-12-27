def decimal_to_hex(decimal_value):
    # Convert the decimal value to its binary representation using two's compliment method
    binary_value = bin(decimal_value & 0xffff)[2:]
    
    # Add leading zeros to make the binary value 16 bits long
    binary_value = binary_value.zfill(16)
    
    # Convert the binary value to hexadecimal
    hex_value = hex(int(binary_value, 2))[2:]
    
    # Add a leading zero for single digit hex values
    if len(hex_value) == 1:
        hex_value = "0" + hex_value
    
    # Remove the "ff" prefix for negative hex values
    if hex_value[0] == "f":
        hex_value = hex_value[2:]
    
    return hex_value

# Test the function with the given decimal values
decimal_values = [0, 0, 0, 0, 6, 12, 19, 25, 31, 36, 42, 48, 53, 58, 63, 68, 72, 77, 80, 84, 87, 90, 93, 95, 97, 99, 100, 100, 101, 101, 100, 100, 99, 97, 95, 93, 90, 87, 84, 81, 77, 73, 68, 63, 59, 53, 48, 42, 37, 31, 25, 19, 13, 7, 0, -6, -12, -18, -24, -30, -36, -42, -47, -53, -58, -63, -68, -72, -76, -80, -84, -87, -90, -93, -95, -97, -98, -100, -100, -101, -101, -100, -100, -99, -97, -95, -93, -91, -88, -84, -81, -77, -73, -68, -64, -59, -54, -48, -43, -37, -31, -25, -19, -13, -7, -1, 5, 12, 18, 24, 30, 36, 41, 47, 52, 58, 63, 67, 72, 76, 80, 84, 87, 90, 93, 95, 97, 98, 100, 100, 101, 101, 101, 100, 99, 97, 95, 93, 91, 88, 85, 81, 77, 73, 69, 64, 59, 54, 49, 43, 38, 32, 26, 20, 14, 7, 0, 5, 11, 16, 21, 26, 32, 36, 41, 46, 50, 55, 59, 63, 66, 70, 73, 76, 78, 80, 82, 84, 85, 86, 87, 87, 87, 87, 86, 85, 84, 82, 81, 78, 76, 73, 70, 66, 63, 59, 55, 51, 46, 42, 37, 32, 27, 22, 16, 11, 6, 0, -5, -10, -16, -21, -26, -31, -36, -41, -46, -50, -54, -59, -62, -66, -69, -73, -75, -78, -80, -82, -84, -85, -86, -87, -87, -87, -87, -87, -86, -85, -84, -83, -81, -78, -76, -73, -70, -67, -63, -59, -55, -51, -47, -42, -37, -32, -27, -22, -17, -11, -6, -1, 5]

# Convert the decimal values to hexadecimal
hex_values = [decimal_to_hex(decimal_value) for decimal_value in decimal_values]

# Print the hex values in groups of 8, separated by a single space
for i in range(0, len(hex_values), 8):
    print(" ".join(hex_values[i:i+8]))
