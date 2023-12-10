namespace Day8 {
    internal class Program {
        static void Main(string[] args) {
            const string GOAL = "ZZZ";

            Dictionary<string, Tuple<string, string>> nodes = new();

            string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day8\\input.txt";
            string[] data = File.ReadAllLines(filepath);

            string instructions = data[0];

            int index = 0;
            int count = 1;

            for (int i = 2; i < data.Length; i++) {
                string line = data[i];

                string key = line.Split("=")[0].Trim();

                string[] value = line.Split("=")[1].Split(",");

                Tuple<string, string> destinations = new(value[0].Trim().Trim('('), value[1].Trim().Trim(')'));

                nodes[key] = destinations;
            }

            Tuple<string, string> currNode = nodes["AAA"];

            while (true) {
                char direction = instructions[index];

                string nextNode;
                if (direction == 'L') {
                    nextNode = currNode.Item1;
                }
                else {
                    nextNode = currNode.Item2;
                }

                if (nextNode == GOAL) break;
                else currNode = nodes[nextNode];

                index++;
                if (index == instructions.Length) {
                    index = 0;
                }

                count++;
            }

            Console.WriteLine(count);
        }
    }
}