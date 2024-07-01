
void func1()    //цепное представление листа
{
    LinkedList1<int> list2 = new();
    bool b = true;
    while (b)
    {
        Console.WriteLine("Теперь выберите, что вы хотите сделать:\n" +
                          "1) AddLast- добавление элемента в конец списка;\n" +
                          "2) AddFirst- добавление элемента в начало списка;\n" +
                          "3) Insert- добавление элемента по индексу;\n" +
                          "4) RemoveAr- удаления элемента по индексу из списка;\n" +
                          "5) ToArray- просмотр всего списка;\n"+
                          "6) Clear- удаление всех элементов в списке:"                          
                          /*+ "7) Remove- удаления элемента из списка;\n" */);
        int x = Convert.ToInt32(Console.ReadLine());
        switch (x)
        {
            case 1:
                Console.Write("Напишите, что хотите добавить, обязательно целое число: ");
                list2.AddLast(Convert.ToInt32(Console.ReadLine()));
                break;

            case 2:
                Console.Write("Напишите, что хотите добавить, обязательно целое число: ");
                list2.AddFirst(Convert.ToInt32(Console.ReadLine()));
                break;

/*            case 7:
                Console.Write("Напишите, что хотите удалить: ");
                list2.Remove(Convert.ToInt32(Console.ReadLine()));
                break;*/

            case 3:
                Console.Write("Напишите индекс, куда хотите добавить элемент: ");
                int temp = Convert.ToInt32(Console.ReadLine());
                Console.Write("Напишите что хотите добавить, обязательно целое число: ");
                list2.Insert(temp, Convert.ToInt32(Console.ReadLine()));
                break;

            case 4:
                Console.Write("Напишите индекс элемента, который хотите удалить: ");
                list2.RemoveAt(Convert.ToInt32(Console.ReadLine()));
                break;

            case 5:
                list2.ToArray();
                break;

            case 6:
                list2.Clear();
                break;

            default: b = false; break;

        }

    }
}

void func2()    //сплошное представление листа, обычное
{
    LinkedList<int> list1 = new();
    bool b = true;
    while (b)
    {
        Console.WriteLine("Теперь выберите, что вы хотите сделать:\n" +
                          "1) Add- добавление элемента в конец списка;\n" +
                          "2) Get вывод элемента списка по индексу;\n" +
                          "3) RemoveAt- удаления элемента из списка по индексу;\n" +
                          "4) Insert- добавление элемента в список по индексу;\n" +
                          "5) ToArray- просмотр всего списка;\n" +
                          "6) ShowIndexes- просмотр всего списка и индексов;\n" +
                          "7) PrintAll- просмотр всех элементов и кол-во перемещений у онных;\n" +
                          "8) Remove- удаление всех элементов в списке:");

        int x = Convert.ToInt32(Console.ReadLine());
        switch (x)
        {
            case 1:
                Console.Write("Напишите, что хотите добавить, обязательно целое число: ");
                list1.Add(Convert.ToInt32(Console.ReadLine()));
                break;

            case 2:
                Console.Write("Напишите индекс списка, который хотите увидеть, обязательно целое число: ");
                Console.WriteLine(list1.Get(Convert.ToInt32(Console.ReadLine())));
                break;

            case 3:
                Console.Write("Напишите индекс списка, который хотите удалить, обязательно целое число: ");
                list1.RemoveAt(Convert.ToInt32(Console.ReadLine()));
                break;

            case 4:
                Console.Write("Напишите индекс списка, куда хотите вставить элемент, обязательно целое число: ");
                int temp = Convert.ToInt32(Console.ReadLine());
                Console.Write("Напишите, какое число хотите добавить, обязательно целое число: ");
                list1.Insert(temp, Convert.ToInt32(Console.ReadLine()));
                break;

            case 5:
                list1.ToArray();
                break;

            case 6:
                list1.ShowIndexes();
                break;

            case 7:
                list1.PrintAll();
                break;

            case 8:
                list1.Remove();
                break;

            default: b = false; break;

        }
    }
}

void func3()    //лист с курсорами
{
    CursorLinkedList list3 = new();
    bool b = true;
    while (b)
    {
        Console.WriteLine("Теперь выберите, что вы хотите сделать:\n" +
                          "1) Insert- добавление элемента по индексу;\n" +
                          "2) Add- добавление элемента в конец списка;\n" +
                          "3) Remove- удаление конкретного элемента из списка;\n" +
                          "4) ToArray- просмотр всего списка;\n" +
                          "5) DisplayMoves- просмотр всего списка и кол-во перемещений;\n" +
                          "6) Clear- удаление всех элементов в списке:");

        int x = Convert.ToInt32(Console.ReadLine());
        switch (x)
        {
            case 1:
                Console.Write("Напишите индекс списка, куда хотите вставить элемент, обязательно целое число: ");
                int temp1 = Convert.ToInt32(Console.ReadLine());
                Console.Write("Напишите, какое число хотите добавить, обязательно целое число: ");
                /*if (temp1 <= 0) list3.Add(Convert.ToInt32(Console.ReadLine()));*/
                list3.Insert(temp1, Convert.ToInt32(Console.ReadLine()));
                break;

            case 2:
                Console.Write("Напишите, какое число хотите добавить, обязательно целое число: ");
                list3.Add(Convert.ToInt32(Console.ReadLine()));
                break;
            case 3:
                Console.Write("Напишите, что хотите удалить: ");
                int temp = Convert.ToInt32(Console.ReadLine());
                list3.Remove(temp);
                break;

            case 4:
                list3.ToArray();
                break;

            case 5:
                list3.DisplayMoves();
                break;

            case 6:
                list3.Clear();
                break;

            default: b = false; break;

        }
    }

}


void main()
{
    Console.WriteLine("Выберите, с чем вы хотите работать:\n" +
                      "1) цепное представление линейного списка;\n" +
                      "2) сплошное представление линейного списка;\n" +
                      "3) сплошное представление линейного списка с курсорами:");
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
        default: Console.WriteLine("Вы что-то не то написали"); break;
    }
}


main();









/*
LinkedList<int> list1 = new();

list1.Add(12);
list1.Add(23);
list1.Add(34);
list1.Add(45);
list1.ToArray();
Console.WriteLine($"asd {list1.GetFirst()}");
list1.PopLast();
Console.WriteLine("------------------");
list1.ToArray();
Console.WriteLine("------------------");
list1.Remove();
list1.ToArray();
list1.Add(12);
list1.ToArray();
*/


/*LinkedList1<int> list2 = new();
list2.AddLast(1);
list2.AddLast(2);
list2.AddLast(3);
list2.AddLast(4);
list2.ToArray();
list2.AddFirst(111);
list2.ToArray();
list2.Clear();
list2.ToArray();
list2.AddLast(1);
list2.ToArray();
*/

/*CursorLinkedList list3 = new ();
list3.Add(3);
list3.Add(7);
list3.Add(11);
list3.ToArray();

list3.Remove(3);
list3.ToArray();
list3.Clear();ListNode
list3.ToArray ();*/

//счетчик- кол-во перемещений у элемента
//insert- во всех


public class ListNode<T>
{
    public T Data { get; set; } // данные узла
    public ListNode<T> Next { get; set; } // ссылка на следующий узел списка
    public int Count { get; set; }
    public int Moves { get; set; }

    public void Print()
    {
        Console.WriteLine($"Value: {Data} - Moves: {Moves}");
    }

    // Конструктор для создания узла списка с заданным значением данных
    public ListNode(T data)
    {
        Data = data;
        Next = null;
        Count = 0;
        Moves = 0;


    }
}

// Класс, реализующий сплошное представление линейного списка
public class LinkedList<T>
{
    private ListNode<T> head; // ссылка на первый узел списка

    // Конструктор для создания пустого списка
    public LinkedList()
    {
        head = null;
    }

    // Метод, проверяющий, является ли список пустым
    public bool IsEmpty()
    {
        return head == null;
    }

    // Метод, добавляющий новый узел с заданным значением данных в конец списка
/*    public void Add(T data)
    {
        ListNode<T> newNode = new ListNode<T>(data);
        newNode.Count = head != null ? head.Count + 1 : 1;
        if (IsEmpty())
        {
            head = newNode;
        }
        else
        {
            ListNode<T> current = head;

            while (current.Next != null)
            {
                current = current.Next;
            }

            current.Next = newNode;
        }
    }*/

    public void Add(T data)
    {
        ListNode<T> newNode = new ListNode<T>(data);
        newNode.Moves = 0; // сброс счетчика перемещений для новых элементов
        newNode.Count = head != null ? head.Count + 1 : 1;
        if (IsEmpty())
        {
            head = newNode;
        }
        else
        {
            ListNode<T> current = head;

            while (current.Next != null)
            {
                current = current.Next;
            }

            current.Next = newNode;
        }
    }


    // Метод, удаляющий первый узел списка

    public void RemoveAt(int index)
    {
        if (index < 0 || head == null)
            throw new IndexOutOfRangeException();

        ListNode<T> prev = null;
        ListNode<T> current = head;
        while (index > 0 && current != null)
        {
            prev = current;
            current = current.Next;
            index--;
        }

        if (current == null)
            throw new IndexOutOfRangeException();

        if (prev == null)
        {
            head = current.Next;
        }
        else
        {
            prev.Next = current.Next;
        }

        current = null;

        // увеличение счетчика перемещений для остальных элементов списка
        ListNode<T> temp = head;
        while (temp != null)
        {
            if (prev != null && prev.Equals(temp))
            {
                // предыдущий узел был удален - увеличиваем его перемещение на количество перемещений текущего узла
                prev.Moves += current.Moves;
                break;
            }
            else if (current != null && current.Equals(temp))
            {
                // текущий узел был удален - ничего не делаем
            }
            else
            {
                temp.Moves++;
            }
            temp = temp.Next;
        }
    }
/*    public void RemoveAt(int index)
    {
        if (index < 0 || head == null)
            throw new IndexOutOfRangeException();

        if (index == 0)
        {
            head = head.Next;
            return;
        }

        ListNode<T> prev = head;
        ListNode<T> current = head.Next;

        while (index > 1)
        {
            prev = current;
            current = current.Next;
            index--;
        }

        prev.Next = current.Next;
        current = null;
    }*/

    // Метод, возвращающий значение узла списка по индексу
    public T Get(int index)
    {
        if (index < 0 || head == null)
            throw new IndexOutOfRangeException();

        ListNode<T> current = head;
        while (index > 0)
        {
            current = current.Next;
            index--;
        }

        return current.Data;
    }
    // Метод, добавляющий новый узел с заданным значением данных в начало списка
    public void AddFirst(T data)
    {
        ListNode<T> newNode = new ListNode<T>(data);
        newNode.Count = head != null ? head.Count + 1 : 1;

        if (IsEmpty())
        {
            head = newNode;
        }
        else
        {
            newNode.Next = head;
            head = newNode;
        }
    }

    public void Insert(int index, T data)
    {
        if (index < 0)
            throw new IndexOutOfRangeException();

        if (index == 0)
        {
            this.AddFirst(data);
            return;
        }

        ListNode<T> prev = head;
        ListNode<T> current = head.Next;
        while (index > 1 && current != null)
        {
            prev = current;
            current = current.Next;
            index--;
        }

        ListNode<T> newNode = new ListNode<T>(data);
        prev.Next = newNode;
        newNode.Next = current;

        // увеличение счетчика перемещений для остальных элементов списка
        ListNode<T> temp = current;
        while (temp != null)
        {
            temp.Moves++;
            temp = temp.Next;
        }
    }

/*
    public void Insert(int index, T data)
    {
        if (index < 0)
            throw new IndexOutOfRangeException();

        if (index == 0)
        {
            this.AddFirst(data);
            return;
        }

        ListNode<T> prev = head;
        ListNode<T> current = head.Next;
        while (index > 1 && current != null)
        {
            prev = current;
            current = current.Next;
            index--;
        }

        ListNode<T> newNode = new ListNode<T>(data);
        prev.Next = newNode;
        newNode.Next = current;
    }
*/


    // Метод, возвращающий все значения узлов списка в виде массива
    public T[] ToArray()
    {
        ListNode<T> current = head;
        int count = 0;

        while (current != null)
        {
            count++;
            current = current.Next;

        }

        T[] array = new T[count];

        current = head;

        for (int i = 0; i < count; i++)
        {
            array[i] = current.Data;
            Console.Write($"{array[i]} ");
            current = current.Next;
        }
        Console.WriteLine();
        return array;
    }
    public void ShowIndexes()
    {
        ListNode<T> current = head;
        int index = 0;
        while (current != null)
        {
            Console.WriteLine($"Index: {index} - Value: {current.Data}");
            current = current.Next;
            index++;
        }
    }
    public void PrintAll()
    {
        ListNode<T> current = head;
        while (current != null)
        {
            current.Print();
            current = current.Next;
        }
    }

    public void Remove()
    {
        head.Count = 0;
        head = null;
    }
}



class Node1
{
    public int value;
    public int next;
    public int movesCount;

    public Node1(int value, int next)
    {
        this.value = value;
        this.next = next;
        this.movesCount = 0;
    }
}

class CursorLinkedList
{
    private Node1[] nodes;
    private int size;
    private int head;
    private int free;

    public CursorLinkedList()
    {
        nodes = new Node1[50];
        size = 0;
        head = -1;
        free = 0;

        for (int i = 0; i < nodes.Length; i++)
        {
            nodes[i] = new Node1(0, i + 1);
        }

        nodes[nodes.Length - 1] = new Node1(0, -1);
    }

    public void Add(int value)
    {
        if (free == -1)
        {
            int newCapacity = nodes.Length * 2;
            Node1[] newNodes = new Node1[newCapacity];

            for (int i = 0; i < nodes.Length; i++)
            {
                newNodes[i] = nodes[i];
            }

            for (int i = nodes.Length; i < newCapacity; i++)
            {
                newNodes[i] = new Node1(0, i + 1);
            }

            newNodes[newCapacity - 1].next = -1;
            free = nodes.Length;
            nodes = newNodes;
        }

        nodes[free].value = value;

        int previous = -1;
        int current = head;

        while (current != -1 && nodes[current].value < value)
        {
            previous = current;
            current = nodes[current].next;
        }

        if (previous == -1)
        {
            nodes[free].next = head;
            head = free;
        }
        else
        {
            nodes[previous].next = free;
            nodes[free].next = current;
        }

        // увеличиваем счетчик перемещений для всех узлов, которые были перемещены
        int traverser = current;
        while (traverser != -1)
        {
            nodes[traverser].movesCount++;
            traverser = nodes[traverser].next;
        }

        free = nodes[free].next;
        size++;
    }

    public void Insert(int index, int value)
    {
        if (free == -1)
        {
            // Увеличиваем размер массива узлов при необходимости
            int newCapacity = nodes.Length * 2;
            Node1[] newNodes = new Node1[newCapacity];

            for (int i = 0; i < nodes.Length; i++)
            {
                newNodes[i] = nodes[i];
            }

            for (int i = nodes.Length; i < newCapacity; i++)
            {
                newNodes[i] = new Node1(0, i + 1);
            }

            newNodes[newCapacity - 1].next = -1;
            free = nodes.Length;
            nodes = newNodes;
        }

        int previous = -1;
        int current = head;

        while (current != -1 && nodes[current].value < value)
        {
            previous = current;
            current = nodes[current].next;
        }

        nodes[free].value = value;
        nodes[free].movesCount = 0;

        if (previous == -1)
        {
            nodes[free].next = head;
            head = free;
        }
        else
        {
            nodes[previous].next = free;
            nodes[free].next = current;
        }

        // Увеличиваем значения movesCount у всех следующих узлов на 1
        Console.WriteLine("previous");
        int traverser = nodes[previous].next;
        while (traverser != -1)
        {
            nodes[traverser].movesCount++;
            traverser = nodes[traverser].next;
            Console.WriteLine(nodes[traverser].movesCount);
        }

        free = nodes[free].next;
        size++;

        // Если новый узел вставлен перед заданным индексом, увеличиваем значение movesCount у всех следующих узлов на 1
        Console.WriteLine("current");
        if (current == index)
        {
            while (current != -1)
            {
                nodes[current].movesCount++;
                current = nodes[current].next;
                Console.WriteLine(nodes[current].movesCount);
            }
        }
    }

    public void Remove(int value)
    {
        if (head == -1)
        {
            return;
        }

        int previous = -1;
        int current = head;

        while (current != -1 && nodes[current].value != value)
        {
            previous = current;
            current = nodes[current].next;
        }

        if (current == -1)
        {
            return;
        }

        // увеличиваем счетчик перемещений для всех узлов, которые были перемещены
        int traverser = nodes[current].next;
        while (traverser != -1)
        {
            nodes[traverser].movesCount++;
            traverser = nodes[traverser].next;
        }

        if (previous == -1)
        {
            head = nodes[current].next;
        }
        else
        {
            nodes[previous].next = nodes[current].next;
        }

        nodes[current].value = 0;
        nodes[current].next = free;
        free = current;
        size--;
    }



    public void ToArray()
    {
        int current = head;

        while (current != -1)
        {
            Console.Write(nodes[current].value + " ");
            current = nodes[current].next;
        }

        Console.WriteLine();
    }
    public void Clear()
    {
        size = 0;
        head = -1;
        free = 0;

        for (int i = 0; i < nodes.Length; i++)
        {
            nodes[i] = new Node1(0, i + 1);
        }

        nodes[nodes.Length - 1] = new Node1(0, -1);
    }

    public void DisplayMoves()
    {
        Console.WriteLine("Moves:");
        int current = head;

        while (current != -1)
        {
            Console.WriteLine($"Value = {nodes[current].value}, moved {nodes[current].movesCount} times.");
            current = nodes[current].next;
        }
    }
}


public class LinkedListNode<T>
{
    public T Value { get; set; }
    public LinkedListNode<T> Next { get; set; }
    public int Moves { get; set; }
}

public class LinkedList1<T>
{
    public LinkedListNode<T> Head { get; set; }
    public int Count { get; set; }

    public void AddFirst(T value)
    {
        var node = new LinkedListNode<T>
        {
            Value = value,
            Next = Head,
            Moves = 0
        };
        Head = node;
        Count++;

        var current = Head.Next;
        while (current != null)
        {
            current.Moves++;
            current = current.Next;
        }
    }

    public void AddLast(T value)
    {
        if (Head == null)
        {
            AddFirst(value);
            return;
        }

        var node = new LinkedListNode<T>
        {
            Value = value,
            Moves = 0
        };
        var current = Head;

        while (current.Next != null)
        {
            //current.Moves++; // increment moves counter for current node
            current = current.Next;
        }

        current.Next = node;
        Count++;
    }


    public void Remove(T value)
    {
        if (Head == null)
        {
            return;
        }

        if (EqualityComparer<T>.Default.Equals(Head.Value, value))
        {
            Head = Head.Next;
            Count--;
            return;
        }

        var current = Head;
        while (current.Next != null)
        {
            if (EqualityComparer<T>.Default.Equals(current.Next.Value, value))
            {
                current.Next = current.Next.Next;
                Count--;
                return;
            }
            current = current.Next;
        }
    }

    public void Clear()
    {
        Head = null;
        Count = 0;
    }



    public void Insert(int index, T value)
    {
        if (index < 0 || index > Count)
        {
            throw new ArgumentOutOfRangeException("Index is out of range.");
        }

        if (index == 0)
        {
            AddFirst(value);
            return;
        }

        if (index == Count)
        {
            AddLast(value);
            return;
        }

        var node = new LinkedListNode<T>
        {
            Value = value,
            Moves = 0
        };
        var current = Head;
        LinkedListNode<T> previous = null;

        for (int i = 0; i < index; i++)
        {
            current.Moves++; // increment moves counter for current node
            previous = current;
            current = current.Next;
        }

        node.Moves = current.Moves; // set moves count for new node to the count of the node that it's replacing
        previous.Next = node;
        node.Next = current;
        Count++;

        while (current != null)
        {
            current.Moves++; // increment moves counter for following nodes
            current = current.Next;
        }
    }

    public void RemoveAt(int index)
    {
        if (index < 0 || index >= Count)
        {
            throw new ArgumentOutOfRangeException("Index is out of range.");
        }

        if (index == 0)
        {
            Head = Head.Next;
            Count--;

            var cur = Head;
            while (cur != null)
            {
                cur.Moves++;
                cur = cur.Next;
            }

            return;
        }

        var current = Head;
        LinkedListNode<T> previous = null;

        for (int i = 0; i < index; i++)
        {
            previous = current;
            current = current.Next;
        }

        previous.Next = current.Next;
        Count--;

        while (current.Next != null)
        {
            current.Next.Moves++;
            current = current.Next;
        }
    }

    public bool Contains(T value)
    {
        var current = Head;
        while (current != null)
        {
            if (EqualityComparer<T>.Default.Equals(current.Value, value))
            {
                return true;
            }
            current = current.Next;
        }
        return false;
    }

    public void ToArray()
    {
        LinkedListNode<T> current = Head;
        int count = 0;

        while (current != null)
        {
            count++;
            current = current.Next;
        }

        T[] array = new T[count];

        current = Head;

        for (int i = 0; i < count; i++)
        {
            array[i] = current.Value;
            Console.WriteLine($"{i}) value = {array[i]} moved {current.Moves} times.");
            current = current.Next;
        }
        Console.WriteLine();
    }
}
/*    public void MoveToFront(T value)
    {
        if (Head == null || EqualityComparer<T>.Default.Equals(Head.Value, value))
        {
            return;
        }

        var previous = Head;
        var current = Head.Next;
        while (current != null)
        {
            if (EqualityComparer<T>.Default.Equals(current.Value, value))
            {
                previous.Next = current.Next;
                current.Next = Head;
                Head = current;
                Head.Moves++;
                return;
            }
            previous = current;
            current = current.Next;
        }
    }*/

/*public class LinkedListNode<T>
{
    public T Value { get; set; }
    public LinkedListNode<T> Next { get; set; }
    public int Moves { get; set; }
}

public class LinkedList1<T>
{
    public LinkedListNode<T> Head { get; set; }
    public int Count { get; set; }

    public void AddFirst(T value)
    {
        var node = new LinkedListNode<T> { Value = value, Next = Head };
        Head = node;
        Count++;
    }

    public void AddLast(T value)
    {
        if (Head == null)
        {
            AddFirst(value);
            return;
        }

        var node = new LinkedListNode<T> { Value = value };
        var current = Head;
        while (current.Next != null)
        {
            current = current.Next;
        }
        current.Next = node;
        Count++;
    }

    public void Remove(T value)
    {
        if (Head == null)
        {
            return;
        }

        if (EqualityComparer<T>.Default.Equals(Head.Value, value))
        {
            Head = Head.Next;
            Count--;
            return;
        }

        var current = Head;
        while (current.Next != null)
        {
            if (EqualityComparer<T>.Default.Equals(current.Next.Value, value))
            {
                current.Next = current.Next.Next;
                Count--;
                return;
            }
            current = current.Next;
        }
    }

    public void Clear()
    {
        Head = null;
        Count = 0;
    }

    public bool Contains(T value)
    {
        var current = Head;
        while (current != null)
        {
            if (EqualityComparer<T>.Default.Equals(current.Value, value))
            {
                return true;
            }
            current = current.Next;
        }
        return false;
    }

    public void ToArray()
    {
        LinkedListNode<T> current = Head;
        int count = 0;

        while (current != null)
        {
            count++;
            current = current.Next;

        }

        T[] array = new T[count];

        current = Head;

        for (int i = 0; i < count; i++)
        {
            array[i] = current.Value;
            Console.Write($"{array[i]} ");
            current = current.Next;
        }
        Console.WriteLine();
    }

}*/

/*
public class ListNode<T>
{
    public T Data { get; set; } // данные узла
    public ListNode<T> Next { get; set; } // ссылка на следующий узел списка
    public int Count { get; set; }

    // Конструктор для создания узла списка с заданным значением данных
    public ListNode(T data)
    {
        Data = data;
        Next = null;
        Count = 0;
    }
}

// Класс, реализующий сплошное представление линейного списка

public class LinkedList<T>
{
    private ListNode<T> head; // ссылка на первый узел списка

    // Конструктор для создания пустого списка
    public LinkedList()
    {
        head = null;
    }

    // Метод, проверяющий, является ли список пустым
    public bool IsEmpty()
    {
        return head == null;
    }

    // Метод, добавляющий новый узел с заданным значением данных в конец списка
    public void Add(T data)
    {
        ListNode<T> newNode = new ListNode<T>(data);
        head.Count++;
        if (IsEmpty())
        {
            head = newNode;
        }
        else
        {
            ListNode<T> current = head;

            while (current.Next != null)
            {
                current = current.Next;
            }

            current.Next = newNode;
        }
    }

    // Метод, удаляющий первый узел списка
    public void PopFirst()
    {
        head.Count--;
        if (!IsEmpty())
        {
            head = head.Next;
        }
    }
    public void PopLast()
    {
        if (IsEmpty()) return; // если список пустой, то нечего удалять
        if (head.Next == null) // если в списке всего один элемент
        {
            head = null; // удаляем его
            return;
        }

        ListNode<T> current = head;
        while (current.Next.Next != null)
        {
            current = current.Next; // ищем предпоследний элемент
        }

        current.Next = null; // удаляем последний элемент
    }


    // Метод, возвращающий значение первого узла списка
    public T GetFirst()
    {
        if (!IsEmpty())
        {
            return head.Data;
        }

        return default(T);
    }

    // Метод, возвращающий все значения узлов списка в виде массива
    public T[] ToArray()
    {
        ListNode<T> current = head;
        int count = 0;

        while (current != null)
        {
            count++;
            current = current.Next;

        }

        T[] array = new T[count];

        current = head;

        for (int i = 0; i < count; i++)
        {
            array[i] = current.Data;
            Console.Write($"{array[i]} ");
            current = current.Next;
        }
        Console.WriteLine();
        return array;
    }

    public void Remove()
    {
        head.Count = 0;
        head = null;
    }
}*/