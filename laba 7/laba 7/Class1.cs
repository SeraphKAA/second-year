using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace laba_7
{
    class BinarySearchTree
    {
        private Node root;
        private class Node
        {
            public int value;
            public Node left;
            public Node right;

            public Node(int tvalue)
            {
                value = tvalue;
                left = null;
                right = null;
            }
        }

        public void Insert(int value)
        {
            root = Insert(root, value);
        }

        private Node Insert(Node root, int value)
        {
            if (root == null)
            {
                root = new Node(value);
            }
            else if (value < root.value)
            {
                root.left = Insert(root.left, value);
            }
            else if (value > root.value)
            {
                root.right = Insert(root.right, value);
            }
            return root;
        }

/*        public void InOrderTraversal()
        {
            InOrderTraversal(root);
        }

        private void InOrderTraversal(Node root)
        {
            if (root != null)
            {
                InOrderTraversal(root.left);
                Console.Write(root.value + " ");
                InOrderTraversal(root.right);
            }
        }*/

        public int Search(int value, bool barrier)
        {
            int count = 0;
            int prov = 999999999;
            Node current = root;
            if (barrier) 
            {
                Console.WriteLine("Напишите глубину, после которой не стоит выходить: ");
                prov = Convert.ToInt32(Console.ReadLine());
            }
            
            while (current != null && count < prov)
            {
                count++;

                if (value < current.value)
                {
                    current = current.left;
                }
                else if (value > current.value)
                {
                    current = current.right;
                }
                else
                {
                    return count;
                }
            }

            if (current == null)
            {
                return -1;
            }

            if (count == prov) 
            { 
                Console.WriteLine($"В поиске глубина достигла нашего барьера, число, которое мы искали: {value}, не было найдено");
                return -1;
            }
            return count;
        }
        public void PrintTree()
        {
            PrintTree(root, "");
        }

        private void PrintTree(Node root, string indent)
        {
            if (root == null)
                return;

            Console.WriteLine(indent + root.value);

            if (root.left != null || root.right != null)
            {
                PrintTree(root.left, indent + "    |");
                Console.WriteLine(indent + "---+");
                PrintTree(root.right, indent + "    |");
            }
        }

        public void Remove(int value)
        {
            root = Remove(root, value);
        }

        private Node Remove(Node current, int value)
        {
            if (current == null)
            {
                return null;
            }

            if (value == current.value)
            {
                if (current.left == null && current.right == null)
                {
                    return null;
                }

                if (current.left == null)
                {
                    return current.right;
                }

                if (current.right == null)
                {
                    return current.left;
                }

                int smallestValue = FindSmallestValue(current.right);
                current.value = smallestValue;
                current.right = Remove(current.right, smallestValue);
                return current;
            }

            if (value < current.value)
            {
                current.left = Remove(current.left, value);
                return current;
            }

            current.right = Remove(current.right, value);
            return current;
        }

        private int FindSmallestValue(Node root)
        {
            return root.left == null ? root.value : FindSmallestValue(root.left);
        }
    }

}
