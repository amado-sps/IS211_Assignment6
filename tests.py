#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import conversions

class ComparisonTable(unittest.TestCase):
    celsValues = [500.00, 490.00, 480.00, 470.00, 460.00]
    fahrValues = [932.00, 914.00, 896.00, 878.00, 860.00]
    kelvValues = [773.15, 763.15, 753.15, 743.15, 733.15]

    def testConversionCelsiusToKelvin(self):
        for i in range(len(self.celsValues)):
            print('Testing {} degrees Celsius to {} degrees Kelvin is correct.'.format(self.celsValues[i],
                                                                                       self.kelvValues[i]))
            result = conversions.convertCelsiusToKelvin(self.celsValues[i])
            self.assertEqual(self.kelvValues[i], round(result, 2))

    def testConversionCelsiusToFahrenheit(self):
        for i in range(len(self.celsValues)):
            print('Testing {} degrees Celsius to {} degrees Fahrenheit is correct.'.format(self.celsValues[i],
                                                                                       self.fahrValues[i]))
            result = conversions.convertCelsiusToFahrenheit(self.celsValues[i])
            self.assertEqual(self.fahrValues[i], round(result, 2))

    def testConversionFahrenheitToCelsius(self):
        for i in range(len(self.celsValues)):
            print('Testing {} degrees Fahrenheit to {} degrees Celsius is correct.'.format(self.fahrValues[i],
                                                                                       self.celsValues[i]))
            result = conversions.convertFahrenheitToCelsius(self.fahrValues[i])
            self.assertEqual(self.celsValues[i], round(result, 2))

    def testConversionFahrenheitToKelvin(self):
        for i in range(len(self.celsValues)):
            print('Testing {} degrees Fahrenheit to {} degrees Kelvin is correct.'.format(self.fahrValues[i],
                                                                                       self.kelvValues[i]))
            result = conversions.convertFahrenheitToKelvin(self.fahrValues[i])
            self.assertEqual(self.kelvValues[i], round(result, 2))

    def testConversionKelvinToCelsius(self):
        for i in range(len(self.celsValues)):
            print('Testing {} degrees Kelvin to {} degrees Celsius is correct.'.format(self.kelvValues[i],
                                                                                       self.celsValues[i]))
            result = conversions.convertKelvinToCelsius(self.kelvValues[i])
            self.assertEqual(self.celsValues[i], round(result, 2))

    def testConversionKelvintoFahrenheit(self):
        for i in range(len(self.celsValues)):
            print('Testing {} degrees Kelvin to {} degrees Fahrenheit is correct.'.format(self.kelvValues[i],
                                                                                       self.fahrValues[i]))
            result = conversions.convertKelvintoFahrenheit(self.kelvValues[i])
            self.assertEqual(self.fahrValues[i], round(result, 2))

if __name__ == '__main__':
    unittest.main()
