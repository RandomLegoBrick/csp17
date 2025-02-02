"""
Matthew Anderson 2/1/2025
"""

hourly_pay = float(input('Hourly pay: '))
regular_hours_worked = float(input('Regular hours worked: ')) 
overtime_hours_worked = float(input('Overtime hours worked: ')) 

## read as a percentage from 0-100, eg 3.3 is 3.3% and therefore converted to 0.033 for calculations
federal_tax_rate = float(input('Federal tax withholds percentage: '))
state_tax_rate = float(input('State tax withholds percentage: '))

overtime_multiplier = 1.5 ## assume the overtime hourly pay rate is 1.5 times of the regular hourly pay rate

gross_pay = (regular_hours_worked * hourly_pay) + (overtime_hours_worked * hourly_pay * overtime_multiplier)

federal_tax = gross_pay * (federal_tax_rate / 100)

state_tax = gross_pay * (state_tax_rate / 100)

net_pay = gross_pay + (-federal_tax) + (-state_tax)

print("\n----- Monthly Pay Overview -----")

print(f'Gross Pay: ${gross_pay:.2f}')
print(f'    Federal tax: ${federal_tax:.2f} (Rate: {federal_tax_rate}%)')
print(f'    State tax: ${state_tax:.2f} (Rate: {state_tax_rate}%)')

print(f'\nNet Pay: ${net_pay:.2f}')