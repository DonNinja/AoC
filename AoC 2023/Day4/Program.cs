string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day4\\input.txt";
string[] data = File.ReadAllLines(filepath);


int result = 0;
int gameNo = 0;

// Amount of copies for each of the future cards
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

    // Remove first 2 items, they'll always be "Game" "n:" where n is the game number
    winningNumbers.RemoveRange(0, Math.Min(2, winningNumbers.Count));

    // Removes all empty instances in the lists
    winningNumbers.RemoveAll(n => n == "");
    myNumbers.RemoveAll(n => n == "");

    // Go through the winning numbers and add it to a hash set
    foreach (string item in winningNumbers) {
        if (int.TryParse(item, out int n)) {
            winners.Add(n);
        }
    }

    // Finds the amount of copies the current card has
    int loops = 1;

    if (copies.Count > 0) {
        loops += copies[0];
        copies.RemoveAt(0);
    }

    // Go through each number in the numbers that I have
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
        }
    }

    result += currentScore;
    copyResult += loops;
}

Console.WriteLine(result);
Console.WriteLine(copyResult);