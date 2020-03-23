import unittest

from LinkedList import LinkedList


class TestSum(unittest.TestCase):
    def test_init(self):
        """
        Test initialization
        """
        obj = LinkedList()

        self.assertEqual(obj.count, 0)
        self.assertEqual(obj.head, None)
        self.assertEqual(obj.tail, None)

    def test_append_to_tail(self):
        """
        Test append to end of linkedl ist
        """
        obj = LinkedList()
        obj.append(2)
        obj.append(3)
        self.assertEqual(obj.count, 2)
        self.assertEqual(obj.head.data, 2)
        self.assertEqual(obj.head.next.data, 3)

    def test_insert(self):
        """
        Test append to end of linkedl ist
        """
        obj = LinkedList()
        obj.append(2)
        obj.append(3)
        obj.insert(5,1)
        self.assertEqual(obj.count, 3)
        self.assertEqual(obj.head.data, 2)
        self.assertEqual(obj.head.next.data, 5)
        self.assertEqual(obj.head.next.next.data, 3)


if __name__ == '__main__':
    unittest.main()