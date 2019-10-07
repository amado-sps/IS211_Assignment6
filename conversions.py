#!/usr/bin/env python
# -*- coding: utf-8 -*-

#[K] = [°C] + 273.15
def convertCelsiusToKelvin(celsius):
     kelvin = celsius + 273.15
     return float(kelvin)

#[°F] = [°C] × ​9⁄5 + 32
def convertCelsiusToFahrenheit(celsius):
     fahrenheit = (celsius * 9) / 5 + 32
     return float(fahrenheit)

#[°C] = ([°F] − 32) × ​5⁄9
def convertFahrenheitToCelsius(fahrenheit):
     celsius = ((fahrenheit - 32) * 5) / 9
     return float(celsius)

#[K] = ([°F] + 459.67) × ​5⁄9
def convertFahrenheitToKelvin(fahrenheit):
     kelvin = (fahrenheit + 459.67) * 5/9
     return float(kelvin)

#[°C] = [K] − 273.15
def convertKelvinToCelsius(kelvin):
     celsius = (kelvin - 273.15)
     return float(celsius)

#[°F] = [K] × ​9⁄5 − 459.67
def convertKelvintoFahrenheit(kelvin):
     fahrenheit = (kelvin * 9/5) - 459.67
     return float(fahrenheit)