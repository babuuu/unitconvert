'''
A python module for converting celsius to fahrenheit
'''
def celsius_to_fahrenheit(c_temp):
    '''
    CONVERTS CELSIUS TEMPERATURES TO FAHRENHEIT TEMPERATURES
    
    Parameters:
    -----------
    c_temp: float
        A temperature in celsius
    Returns:
    --------
    float
    '''
    
    return((c_temp*9/5)+32)

def fahrenheit_to_celsius(f_temp):
    '''
    CONVERTS FAHRENHEIT TEMPERATURES TO CELSIUS TEMPERATURES
    
    Parameters:
    -----------
    f_temp: float
        A temperature in fahrenheit
    Returns:
    --------
    float
    '''    
    return((f_temp-32)*5/9)