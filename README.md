 <h1>QAP4_Pyhton</h1>

# One Stop Insurance Company Policy Calculator

## Description
This program is designed for One Stop Insurance Company to enter and calculate new insurance policies. It handles customer information input, policy details, and generates a summary receipt.

## Author
Walid Jerjawi

## Date
July 16, 2024 - July 20, 2024

## Usage
1. Run the script using Python:
2. Follow the prompts to enter customer and policy information.
3. The program will calculate the policy details and display a summary.
4. Policy information will be saved to `Policy.dat`.

## File Structure
- `QAP4.py`: Main Python script
- `Const.dat`: Contains constant values used in calculations
- `Policy.dat`: Stores policy information for each customer

## Configuration
The program uses `Const.dat` for configuration. This file contains:
- Policy number
- Basic premium
- Additional car discount rate
- Liability coverage cost
- Glass coverage cost
- Loaner car coverage cost
- HST rate
- Monthly payment fee

Ensure this file is present and correctly formatted before running the program.

## Features
- Customer information input
- Multiple insurance options (liability, glass coverage, loaner car)
- Payment method selection
- Claim history recording
- Policy calculation and summary display
- Data persistence in `Policy.dat`

## Contributing
Contributions to improve the program are welcome. Please fork the repository and submit a pull request with your changes.
