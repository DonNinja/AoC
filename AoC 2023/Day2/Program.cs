namespace Day2 {
    internal class Program {
        static void Main(string[] args) {
            string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day2\\input.txt";
            string[] data = File.ReadAllLines(filepath);

            Dictionary<string, int> blockMaxes = new Dictionary<string, int>() {
                { "red", 12 },
                { "green", 13 },
                { "blue", 14 },
            };


            int result = 0;

            foreach (string line in data) {
                bool add = true;

                string[] gameSplit = line.Split(":");

                string[] game = gameSplit[0].Split(" ");
                int gameNumber = int.Parse(game[1]);

                string[] draws = gameSplit[1].Split(";");
                foreach (string hand in draws) {
                    string[] handSplit = hand.Split(",");
                    foreach (string quantity in handSplit) {
                        string trimmedQuantity = quantity.Trim();

                        string[] splitQuantity = trimmedQuantity.Split(" ");

                        int total = int.Parse(splitQuantity[0]);
                        string colour = splitQuantity[1];
                        if (total > blockMaxes[colour]) {
                            add = false;
                        }
                    }
                }
                if (add) {
                    //Console.WriteLine(string.Format("Game {0} will be added", gameNumber));
                    result += gameNumber;
                }
            }

            Console.WriteLine(string.Format("The total result of games that have been added are: {0}", result));

        }
    }
}