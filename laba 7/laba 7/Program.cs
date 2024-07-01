using laba_7;
using System;

void main() 
{
    BinarySearchTree tree = new BinarySearchTree();
    bool b = true;
    while (b)
    {
        Console.WriteLine("У вас есть биннарное дерево, выберите метод:\n" +
            "1) PrintTree - метод для Просмотра биннарного дерева;\n" +
            "2) Insert - Метод для добавление элемента в биннарное дерево относительно значений;\n" +
            "3) Remove - Метод для удаления элемента из дерева;\n" +
            "4) Search - метод для поиска элемента в биннарном дереве;\n" +
            "0) выход из цикла:");
        int variable = Convert.ToInt32(Console.ReadLine());

        switch (variable)
        {
            case 1:
                tree.PrintTree();
                break;
            
            case 2:
                Console.WriteLine("Введите что хотите добавить: ");
                tree.Insert(Convert.ToInt32(Console.ReadLine()));
                break;

            case 3:
                Console.WriteLine("Введите элемент,который хотите удалить: ");
                tree.Remove(Convert.ToInt32(Console.ReadLine()));
                break;

            case 4:
                Console.WriteLine("Напишите, какой элемент хотите найти: ");
                int poisk = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("чтобы осуществить поиск, вам также нужно выбрать 0 или 1 для того, чтобы выбрать поиск без барьера или поиск с барьером: ");
                int temp = Convert.ToInt32(Console.ReadLine()); int oper;
                
                if (temp == 0)
                {
                    oper = tree.Search(poisk, false);
                    if (oper != -1)
                    {
                        Console.WriteLine("Число операций сравнения в поиске с барьером: " + oper + $", для элемента {poisk}");
                    }
                    else Console.WriteLine("Не нашло элемент или достигли ограничения в глубину");
                    
                }
                
                else if (temp == 1)
                {
                    oper = tree.Search(poisk, true);

                    if (oper != -1)
                    {
                        Console.WriteLine("Число операций сравнения в поиске с барьером: " + oper + $", для элемента {poisk}");
                    }
                    else Console.WriteLine("Не нашло элемент или достигли ограничения в глубину");

                }
                else Console.WriteLine("Вы написали не 1 и не 0...");
                break;


            case 0:
            default:
                b = false;
                break;
        
        }
    }

}

main();


/*
BinarySearchTree tree = new();
tree.Insert(50);
tree.Insert(1);
tree.Insert(52);
tree.Insert(33);
tree.Insert(35);
tree.Insert(51);
tree.Insert(53);

//                          { m,
//           { ml                        { mr, 
//l,mmlml, r}, {l,mmlmr, r}}, {l,mmrml, r}, {l,mmrmr, r}} }

tree.PrintTree(); Console.WriteLine('\n');

tree.Remove(1);
tree.PrintTree(); Console.WriteLine('\n');

int number_tree = 53;
int countWithoutBarrier = tree.Search(number_tree, false); // поиск без барьера
if (countWithoutBarrier != -1) 
{
    Console.WriteLine("Число операций сравнения в поиске без барьера: " + countWithoutBarrier + $", для элемента {number_tree}");
}

int countWithBarrier = tree.Search(number_tree, true); // поиск c барьером

if (countWithBarrier != -1)
{
    Console.WriteLine("Число операций сравнения в поиске с барьером: " + countWithBarrier + $", для элемента {number_tree}");
}
else Console.WriteLine("Не нашло элемент или достигли ограничения в глубину");*/
