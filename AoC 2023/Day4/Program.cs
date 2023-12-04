string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day4\\input.txt";
string[] data = File.ReadAllLines(filepath);

int result = 0;
int gameNo = 0;
List<int> copies = new();
int copyResult = 0;

foreach (var line in data) {
    gameNo++;
    int count = 0;
    int currentScore = 0;
    bool alreadyFound = false;
    List<string> gameSplit = [.. line.Split("|")];

    List<string> winningNumbers = [.. gameSplit[0].Split(" ")];
    List<string> myNumbers = [.. gameSplit[1].Split(" ")];

    HashSet<int> winners = new();

    winningNumbers.RemoveRange(0, Math.Min(2, winningNumbers.Count));

    winningNumbers.RemoveAll(n => n == "");
    myNumbers.RemoveAll(n => n == "");

    foreach (string item in winningNumbers) {
        if (int.TryParse(item, out int n)) {
            winners.Add(n);
        }
    }

    int loops = 1;

    if (copies.Count > 0) {
        loops += copies[0];
        copies.RemoveAt(0);
    }

    //Console.WriteLine(string.Format("Game {0} has {1} copies", gameNo, loops - 1));

    //for (int i = 0; i < loops; i++) {
    foreach (string item in myNumbers) {
        if (int.TryParse(item, out int n) && winners.Contains(n)) {
            if (alreadyFound) {
                currentScore *= 2;
            }
            else {
                alreadyFound = true;
                currentScore = 1;
            }

            if (copies.Count > count) {
                copies[count] += loops;
            }
            else {
                copies.Add(loops);
            }

            count++;
            //Console.WriteLine(string.Format("Found a winning number: {0}", n));
        }
        //}
    }

    result += currentScore;
    copyResult += loops;
    //Console.WriteLine();
}

Console.WriteLine(result);
Console.WriteLine(copyResult);