class arithemetry:

	def __init__(self, length, width):
		self.length = length
		self.width = width


	def doSum(self, length, width):
		return 2 * (self.length + self.width )

	def doArea(self, length, width):
		return (self.length * self.width )

class Rectangle(arithemetry):

	def __init__(self, length, width):
		super().__init__(length, width)
		self.length = length
		self.width = width


	def doSum(self,length,width):
		print("Hello world")


rectangle = Rectangle(2, 4)

print(rectangle.doSum(rectangle.length,rectangle.width))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


df = pd.read_csv("kenyanclassics.csv")

print(df.head())
