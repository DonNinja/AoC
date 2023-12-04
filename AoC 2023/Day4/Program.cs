string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day4\\input.txt";
string[] data = File.ReadAllLines(filepath);

int result = 0;

foreach (var line in data) {
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

    foreach (string item in myNumbers) {
        if (int.TryParse(item, out int n) && winners.Contains(n)) {
            if (alreadyFound) {
                currentScore *= 2;
            }
            else {
                alreadyFound = true;
                currentScore = 1;
            }


            //Console.WriteLine(string.Format("Found a winning number: {0}", n));
        }
    }

    result += currentScore;
    //Console.WriteLine();
}

Console.WriteLine(result);