import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], 
                                            quote['top_bid']['price'], 
                                            quote['top_ask']['price'], 
                                            (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], 
                                            quote['top_bid']['price'], 
                                            quote['top_ask']['price'], 
                                            (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    prices = [[121.2, 121.68],
              [120.48, 117.87]]
    for arr in prices:
       self.assertEqual(getRatio(arr[0], arr[1]), arr[0]/arr[1])

  def test_getRatio_handlePriceAZero(self):
    prices = [[0, 120.48],
              [0, 117.87]]
    for arr in prices:
        self.assertEqual(getRatio(arr[0], arr[1]), arr[0]/arr[1])

  def test_getRatio_handlePriceBZero(self):
    prices = [[120.48, 0],
              [117.87, 0],
              [0, 0]]
    for arr in prices:
        self.assertEqual(getRatio(arr[0], arr[1]), None)

if __name__ == '__main__':
    unittest.main()
