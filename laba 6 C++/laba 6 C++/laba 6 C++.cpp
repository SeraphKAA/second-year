// laba6oopc++ 

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
#include <sstream>

using namespace std;

void zad1() {
    int c = 0;
    int l = 0;
    string line;
    ifstream fin("C:\\Users\\79045\\Desktop\\6 c txt\\cppstudio.txt");
    if (!fin) {
        cerr << "Error: Невозможно открыть файл.\n";
    }
    while (getline(fin, line))
    {
        cout << line << endl;
        c += line.length();
        l++;
    }
    fin.close();
    cout << "(text mode): " << c << endl << l << endl;

    ifstream bin_in("C:\\Users\\79045\\Desktop\\6 c txt\\cppstudio.txt", ifstream::binary);
    if (!bin_in) {
        cerr << "Error: Невозможно открыть файл.\n";
    }

    bin_in.seekg(0, bin_in.end); // перейти в конец файла
    int length = bin_in.tellg(); // получить текущую позицию (длину файла)
    bin_in.close();

    cout << "(binary mode): " << length << endl;
}

void zad2() {
    ifstream fin("C:\\Users\\79045\\Desktop\\6 c txt\\cppstudio.txt");
    ofstream russianFile("C:\\Users\\79045\\Desktop\\6 c txt\\russian.txt");
    ofstream englishFile("C:\\Users\\79045\\Desktop\\6 c txt\\english.txt");

    // Цикл посимвольного чтения и записи
    char c;
    while (fin.get(c)) {
        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) {
            // Записать английскую букву
            englishFile.put(c);
        }
        else if ((c >= 'А' && c <= 'Я') || (c >= 'а' && c <= 'я')) {
            // Записать русскую букву
            russianFile.put(c);
        }
        // Игнорировать остальные символы
    }

    // Закрыть файлы
    fin.close();
    russianFile.close();
    englishFile.close();
}

void zad3() {
    const int size = 10;
    int arr[size];
    int sum = 0;


    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 101 - 50; // заполнение массива случайными числами от -50 до 50
    }
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }

    ofstream fin("C:\\Users\\79045\\Desktop\\6 c txt\\zad3.txt");

    for (int i = 0; i < size; i++) {
        if (arr[i] > 0) {
            fin << arr[i] << " ";
            sum += arr[i];
        }
    }
    fin << endl << "Sum: " << sum;
    fin.close();
}

void zad4() {
    ifstream f1("C:\\Users\\79045\\Desktop\\6 c txt\\f1.txt");
    ofstream f2("C:\\Users\\79045\\Desktop\\6 c txt\\f2.txt");
    ofstream f3("C:\\Users\\79045\\Desktop\\6 c txt\\f3.txt");
    int num;
    while (f1 >> num) {
        cout << num << " ";
        if (num % 2 == 0) {
            f2 << oct << num << " ";
        }
        else {
            f3 << hex << num << " ";
        }
    }
    f1.close();
    f2.close();
    f3.close();
    cout << endl;
    char ch1, ch2;
    int count = 0;
    ifstream fi2("C:\\Users\\79045\\Desktop\\6 c txt\\f2.txt");
    ifstream fi3("C:\\Users\\79045\\Desktop\\6 c txt\\f3.txt");

    while (fi2.get(ch1) && fi3.get(ch2)) {
        cout << ch1 << ch2;
        count += 2;
        if (count == 10) {
            char choice;
            cout << "\nДля продолжения нажмите 'n' ";
            cin >> choice;
            if (choice != 'n') {
                break;
            }
            count = 0;
        }
    }
    fi2.close();
    fi3.close();
}

struct TeamStats {
    string name;
    string wins;
    string losses;
    string draws;
    string points;
};

void saveTableToFile(const string& filename, const vector<TeamStats>& table) {
    ofstream file(filename);
    if (file.is_open()) {
        for (const auto& team : table) {
            file << team.name << " " << team.wins << " " << team.losses << " " << team.draws << " " << team.points << endl;
        }
        file.close();
    }
    else {
        cout << "Error opening file " << filename << " for writing" << endl;
    }
}
vector<TeamStats> readTableFromFile(const string& filename) {
    vector<TeamStats> table;
    ifstream file(filename);
    if (file.is_open()) {
        string line;
        while (std::getline(file, line)) {
            istringstream iss(line);
            string name, wins, losses, draws, points;
            if (iss >> name >> wins >> losses >> draws >> points) {
                table.push_back({ name, wins, losses, draws, points });
            }
            else {
                cout << "Error reading line from file " << filename << endl;
            }
        }
        file.close();
    }
    else {
        cout << "Error opening file " << filename << " for reading" << endl;
    }
    return table;
}

vector<TeamStats> writeTable(const vector<TeamStats>& table, string& name, string& wins, string& losses, string& draws, string& points) {
    vector<TeamStats> table1;
    for (const auto& team : table) {
        if (team.name == name) {
            table1.push_back({ name, wins, losses, draws, points });
        }
        else {
            table1.push_back({ team.name, team.wins, team.losses, team.draws, team.points });
        }
    }
    return table1;
}

vector<TeamStats> writeFirstTable() {
    vector<TeamStats> table;
    int x;
    string name, wins, losses, draws, points;
    cout << "Ведите количество команд: ";
    cin >> x;
    do {
        cout << "Введите название команды: ";
        cin >> name;
        cout << "Введите количество побед: ";
        cin >> wins;
        cout << "Введите количество проигрышей: ";
        cin >> losses;
        cout << "Введите количество ничьей: ";
        cin >> draws;
        int a = stoi(wins), b = stoi(draws);
        int c = a * 3 + b;
        points = to_string(c);
        table.push_back({ name, wins, losses, draws, points });
        x -= 1;
    } while (x != 0);
    return table;
}

void zad5() {
    vector<TeamStats> table = {
        {"Team_A", "5", "3", "2", "17"},
        {"Team_B", "3", "5", "2", "11"},
        {"Team_C", "6", "1", "3", "21"},
        {"Team_D", "2", "6", "2", "8"},
    };

    // Сохранение таблицы в файл
    saveTableToFile("C:\\Users\\79045\\Desktop\\6 c txt\\table.txt", table);

    // Считывание таблицы из файла
    vector<TeamStats> tableFromFile = readTableFromFile("C:\\Users\\79045\\Desktop\\6 c txt\\table.txt");

    // Вывод таблицы на экран
    cout << "Table from file:" << endl;
    cout << "Название команды Победы Поражения Ничьи Баллы" << endl;
    for (const auto& team : tableFromFile) {
        cout << team.name << "\t\t " << team.wins << "\t" << team.losses << "\t  " << team.draws << "\t" << team.points << endl;
    }
}

void printTable(const vector<TeamStats>& table) {
    cout << "Название команды Победы Поражения Ничьи Баллы" << endl;
    for (const auto& team : table) {
        cout << team.name << "\t\t " << team.wins << "\t" << team.losses << "\t  " << team.draws << "\t" << team.points << endl;
    }
}

void asd() {
    cout << "Заполняем изначальную таблицу" << endl;
    vector<TeamStats> table = writeFirstTable();
    printTable(table);
    int choice, a, b, c;
    string name, wins, losses, draws, points;
    vector<TeamStats> tableFromFile;
    vector<TeamStats> table1;
    do {

        cout << "Выберите доступное действие:" << endl;
        cout << "1. Сохранить таблицу в файл" << endl;
        cout << "2. Прочитать таблицу из файла" << endl;
        cout << "3. Изменить таблицу" << endl;
        cout << "0. Выход" << endl;
        cout << "Выбор: ";
        cin >> choice;

        // Проверка на правильность ввода
        if (cin.fail()) { //если в потоке произошла ошибка то выполняется дальше
            cin.clear(); //восстанавливаетм поток ввода
            cin.ignore(32767, '\n'); // удаляет все символы в потоке ввода до символа новой строки
            cout << "Ошибка ввода, попробуйте еще раз." << endl;
            continue;
        }

        // Выбор действия
        switch (choice) {
        case 0:
            cout << "Выход из программы." << endl;
            break;
        case 1:
            saveTableToFile("C:\\Users\\79045\\Desktop\\6 c txt\\table.txt", table);
            system("pause");
            system("cls");
            break;
        case 2:
            tableFromFile = readTableFromFile("C:\\Users\\79045\\Desktop\\6 c txt\\table.txt");
            printTable(tableFromFile);
            system("pause");
            system("cls");
            break;
        case 3:
            cout << "Введите название команды: ";
            cin >> name;
            cout << "Введите количество побед: ";
            cin >> wins;
            cout << "Введите количество проигрышей: ";
            cin >> losses;
            cout << "Введите количество ничьей: ";
            cin >> draws;
            a = stoi(wins);
            b = stoi(draws);
            c = a * 3 + b;
            points = to_string(c);
            table = writeTable(table, name, wins, losses, draws, points);
            printTable(table);
            system("pause");
            system("cls");
            break;
        default:
            cout << "Неверный выбор, попробуйте еще раз." << endl;
            break;
        }

        cout << endl;
    } while (choice != 0);
}



int main()
{
    setlocale(LC_ALL, "rus");
    //zad1();
    //zad2();
    //zad3();
    //zad4();
    //zad5();
    asd();
}