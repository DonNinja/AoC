using System.Text.RegularExpressions;

namespace Day9 {
    internal class Program {
        static void Main(string[] args) {
            string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day9\\input.txt";
            string[] data = File.ReadAllLines(filepath);

            int result = 0;
            int loop = 0;

            foreach (var line in data) {
                loop++;

                List<int> numberList = [.. line.Split(' ').Select(int.Parse)];

                //! Uncomment this to solve part 2
                //numberList.Reverse();

                List<List<int>> listOfNumberLists = [numberList];

                List<int> currentList = numberList;

                while (currentList.Any(x => x != 0)) {
                    List<int> newList = new List<int>();

                    for (int i = 1; i < currentList.Count; i++) {
                        int difference = currentList[i] - currentList[i - 1];

                        newList.Add(difference);
                    }

                    listOfNumberLists.Add(newList);

                    currentList = newList;
                }

                listOfNumberLists[^1].Add(0);

                for (int i = listOfNumberLists.Count - 2; i >= 0; i--) {
                    currentList = listOfNumberLists[i];
                    List<int> prevList = listOfNumberLists[i + 1];

                    int newFinal = prevList[^1] + currentList[^1];

                    currentList.Add(newFinal);
                }

                int addition = listOfNumberLists[0][^1];

                result += addition;
            }

            Console.WriteLine(result);
        }


    }
}