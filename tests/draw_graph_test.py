#Oussama Konate, Thomas Delépine, groupe 8
import sys
sys.path.append('../') # allows us to fetch files from the project root
import math
import unittest
from modules.draw_graph import *

class pointtest(unittest.TestCase):
  def test_point(self):
    p1 = point(1, 2)
    p2 = point(5, 5)
    self.assertEqual(p1, p1.copy())
    self.assertIsNot(p1, p1.copy())
    self.assertEqual(p1 + p2, point(6, 7))
    self.assertEqual(p2 - p1, point(4, 3))
    self.assertEqual(2*p1, point(2, 4))

  def test_draw(self):
    width = WIDTH
    height = HEIGHT
    image = Image.new("RGB", (width, height), 'white')
    draw = ImageDraw.Draw(image)
    n1 = node(1, 'i', [], [])
    n2 = node(2, 'j', [], [])
    g = open_digraph([1,2], [1,2], [n1, n2])
    node_pos = {}
    node_pos[1] = point(100, 100)
    node_pos[2] = point(200, 200)
    draw.graph(g, node_pos, [], [],'manual')
    
    image.save("test.jpg")
  
class test_display(unittest.TestCase):
  def test_layout(self):
    n0 = node(0, 'i', [], [1])
    n1 = node(1, 'j', [0], [])
    n2 = node(2, 'j', [2, 3], [2,3])
    n3 = node(3, 'j', [2], [2])
    g1 = open_digraph([0, 1], [1], [n0, n1])
    x = random_layout(g1)

if __name__ == '__main__': # the following code is called only when
  random.seed(datetime.now())
  unittest.main() 