using System;
using System.Collections;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;


void func1()    //цепное представление стека
{
    Stack<int> stack = new ();
    bool b = true;
    while (b)
    {
        Console.WriteLine("Теперь выберите, что вы хотите сделать:\n" +
                          "1) Push- добавление элемента в стек;\n" +
                          "2) Pop- удаления элемента из стека;\n" +
                          "3) Peek- просмотр вершины стека:");
        int x = Convert.ToInt32(Console.ReadLine());
        switch (x)
        {
            case 1:
                Console.Write("Напишите, что хотите добавить, обязательно целое число: ");
                stack.Push(Convert.ToInt32(Console.ReadLine()));
                break;

            case 2: Console.WriteLine($"Был удален элемент {stack.Pop()}"); break;

            case 3: stack.Peek(); break;

            default: b = false; break;

        }

    }
}
void func2()    //сплошное представление стека
{
    Stack1 stack = new ();
    bool b = true;
    while (b)
    {
        Console.WriteLine("Теперь выберите, что вы хотите сделать:\n" +
                          "1) Push- добавление элемента в стек;\n" +
                          "2) Pop- удаления элемента из стека;\n" +
                          "3) Peek- просмотр вершины стека;\n" +
                          "4) See- просмотр всего стека:");
        int x = Convert.ToInt32(Console.ReadLine());
        switch (x)
        {
            case 1:
/*                
                Console.Write("Напишите тип переменной, которую хотите добавить: ");
                string temp = Console.ReadLine();
                if (temp == "int")
*/

                Console.Write("Напишите, что хотите добавить: ");
                stack.Push(Console.ReadLine());
                break;

            case 2: Console.WriteLine($"Был удален элемент {stack.Pop()}"); break;

            case 3: stack.Peek(); break;

            case 4: stack.See(); break;

            default: b = false; break;

        }

    }


}
void func3()    //цепное представление очереди
{
    Queue<int> queue = new ();
    bool b = true;
    while (b)
    {
        Console.WriteLine("Теперь выберите, что вы хотите сделать:\n" +
                          "1) Append- добавление элемента в очередь;\n" +
                          "2) Pop- удаления элемента из очереди;\n" +
                          "3) CheckHead- просмотр головы очереди;\n" +
                          "4) CheckTail- просмотр хвоста очереди:");
        int x = Convert.ToInt32(Console.ReadLine());
        switch (x)
        {
            case 1:
                Console.Write("Напишите, что хотите добавить, обязательно целое число: ");
                queue.Append(Convert.ToInt32(Console.ReadLine()));
                break;

            case 2: Console.WriteLine($"Был удален элемент {queue.Pop()}"); break;

            case 3: queue.CheckHead(); break;

            case 4: queue.CheckTail(); break;

            default: b = false; break;

        }

    }

}
void func4()    //сплошное представление очереди
{
    Queue1<int> queue = new (100);
    bool b = true;
    while (b)
    {
        Console.WriteLine("Теперь выберите, что вы хотите сделать:\n" +
                          "1) Append- добавление элемента в очередь;\n" +
                          "2) Pop- удаления элемента из очереди;\n" +
                          "3) Peek- просмотр головы очереди;\n" +
                          "4) Check- просмотр хвоста очереди\n" +
                          "5) See- просмотри всей очереди:");
        int x = Convert.ToInt32(Console.ReadLine());
        switch (x)
        {
            case 1:
                Console.Write("Напишите, что хотите добавить, обязательно целое число: ");
                queue.Append(Convert.ToInt32(Console.ReadLine()));
                break;

            case 2: Console.WriteLine($"Был удален элемент {queue.Pop()}"); break;

            case 3: queue.Peek(); break;

            case 4: queue.Check(); break;

            case 5: queue.See(); break;

            default: b = false; break;

        }

    }

}


void main()
{
    Console.WriteLine("Выберите, с чем вы хотите работать:\n" +
                      "1) цепное представление стека;\n" +
                      "2) сплошное представление стека;\n" +
                      "3) цепное представление очереди;\n" +
                      "4) сплошное представление очереди:");
    int x = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine(x);
    switch (x)
    {
        case 1:
            func1(); break;
        case 2:
            func2(); break;
        case 3:
            func3(); break;
        case 4:
            func4(); break;
        default: Console.WriteLine("Вы что-то не то написали"); break;
    }
}


main();


/*Stack asd1 = new ();
asd1.Push(11);
asd1.Push(21);
asd1.Push(311);
asd1.Peek();
asd1.Pop();
asd1.Push(123123);
asd1.Peek();
asd1.Pop();
asd1.Peek();
asd1.Pop();
asd1.Peek();*/





/*
Stack1 asd = new ();
asd.Push(11);
asd.Push(21);
asd.Push(311);
asd.See();
asd.Pop();
asd.See();
Console.WriteLine(asd.Peek());
asd.See();

*/
Queue1<int> aaaa = new (100);
/*aaaa.Append(10);
aaaa.Peek();
aaaa.Append(20);
aaaa.Peek();
aaaa.Append(30);
aaaa.Peek();
aaaa.Append(40);
aaaa.Peek();
aaaa.Append(50);
aaaa.Peek();
aaaa.Pop();
aaaa.Peek();
aaaa.See();*/



/*
Queue<int> queue = new ();
queue.Append (1);
queue.Append (2);
queue.Append (3);
queue.Append (4);
queue.CheckHead();
queue.CheckTail();
*/

Queue<int> asd = new ();


public class Queue1<T>
{
    private T[] _data;
    private int _front;
    private int _rear;

    public Queue1(int size)
    {
        _data = new T[size];
        _front = -1;
        _rear = -1;
    }

    public bool IsEmpty() {return _front == -1;}
    public bool IsFull() {return ((_rear + 1) % _data.Length) == _front;}

    public void Append(T item)
    {
        if (IsFull()) throw new Exception("Очередь переполнена");
        else
        {
            if (_front == -1)
            {
                _front = 0;
            }
            _rear = (_rear + 1) % _data.Length;
            _data[_rear] = item;
        }
    }

    public T Pop()
    {
        T item;
        if (IsEmpty()) throw new Exception("Очередь пуста");
        else
        {
            item = _data[_front];
            if (_front == _rear)
            {
                _front = -1;
                _rear = -1;
            }
            else
            {
                _front = (_front + 1) % _data.Length;
            }
        }
        return item;
    }

    public void Peek() {
        Console.WriteLine(_data[_rear]);
    }
    public void Check()
    {
        if (IsEmpty())
            throw new InvalidOperationException("Очередь пуста");
        Console.WriteLine(_data[_front]);
    }
    public void See() 
    {
        for (int i = 0; i <= _rear; i++) 
        {
            Console.WriteLine($"{i} элемент- это {_data[i]}");
        }
    }
}


public class QueueNode<T>
{
    public T Value { get; private set; }
    public QueueNode<T> Next { get; set; }

    public QueueNode(T value)
    {
        Value = value;
    }
}

public class Queue<T>
{
    private QueueNode<T> _head;
    private QueueNode<T> _tail;
    private int _count;

    public int Count { get { return _count; } }
    public bool IsEmpty { get { return _count == 0; } }

    public void Append(T item)
    {
        if (IsEmpty)
        {
            _head = _tail = new QueueNode<T>(item);
        }
        else
        {
            _tail.Next = new QueueNode<T>(item);
            _tail = _tail.Next;
        }

        _count++;
    }

    public T Pop()
    {
        if (IsEmpty)
            throw new InvalidOperationException("Очередь пуста");

        T value = _head.Value;
        _head = _head.Next;

        if (_head == null)
            _tail = null;

        _count--;

        return value;
    }

    public void CheckHead()
    {
        if (IsEmpty)
            throw new InvalidOperationException("Очередь пуста");

        Console.WriteLine(_head.Value);
    }
    public void CheckTail()
    {
        if (IsEmpty)
            throw new InvalidOperationException("Очередь пуста");

        Console.WriteLine(_tail.Value);
    }
}


public class Stack
{
    private Node top;   // верхний узел стека

    private class Node
    {
        public object value;   // хранимое значение
        public Node next;      // ссылка на следующий узел
    }
    public bool IsEmpty() { return top == null; }

    // добавление элемента на вершину стека
    public void Push(object value)
    {
        Node newNode = new Node();
        newNode.value = value;
        newNode.next = top;
        top = newNode;
    }

    // удаление элемента с вершины стека и возврат его значения
    public object Pop()
    {
        if (top == null)
            throw new InvalidOperationException("Стек пуст");
        object value = top.value;
        top = top.next;
        return value;
    }

    public void Peek() { Console.WriteLine(top.value); }
}






public class Stack1
{
    private const int MaxSize = 100;
    private object[] _items = new object[MaxSize];
    private int _currentIndex = -1;
    public Stack1()
    {
    }
    public void Push(object element)
    {
        if (_currentIndex >= MaxSize - 1)
        {
            throw new InvalidOperationException("Стек переполнен");
        }
        _currentIndex++;
        _items[_currentIndex] = element;
    }

    public void PushCollInt(List<int> collection)
    {
        if (_currentIndex >= MaxSize - 1)
        {
            throw new InvalidOperationException("Стек переполнен");
        }

        foreach (int i in collection)
        {
            _currentIndex++;
            _items[_currentIndex] = i;
        }
    }

    public void PushCollBoolean(List<bool> collection)
    {
        if (_currentIndex >= MaxSize - 1)
        {
            throw new InvalidOperationException("Стек переполнен");
        }

        foreach (bool i in collection)
        {
            _currentIndex++;
            _items[_currentIndex] = i;
        }
    }

    public void PushCollString(List<string> collection)
    {
        if (_currentIndex >= MaxSize - 1)
        {
            throw new InvalidOperationException("Стек переполнен");
        }

        foreach (string i in collection)
        {
            _currentIndex++;
            _items[_currentIndex] = i;
        }
    }
    public object Pop()
    {
        if (IsEmpty())
        {
            throw new InvalidOperationException("Стек пуст");
        }
        object element = _items[_currentIndex];
        _items[_currentIndex] = null;
        _currentIndex--;
        return element;
    }

    public object See()
    {
        for (int i = 0; i <= _currentIndex; i++)
        {
            Console.WriteLine($"{i} элемент- это {_items[i]}");

        }
        return _items[_currentIndex];
    }
    public void Peek()
    {
        if (IsEmpty())
        {
            throw new InvalidOperationException("Стек пуст");
        }
        Console.WriteLine(_items[_currentIndex]);
    }
    public bool IsEmpty()
    {
        if (_currentIndex < 0) return true;
        else return false;
    }
}