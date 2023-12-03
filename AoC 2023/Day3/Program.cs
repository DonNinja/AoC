using System.Text.RegularExpressions;

namespace Day3 {
    internal class Program {
        static void Main(string[] args) {
            string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day3\\input2.txt";
            string[] data = File.ReadAllLines(filepath);
            Regex numRegex = new(@"0-9");

            for (int i = 0; i < data.Length; i++) {
                string line = data[i];
                for (int j = 0; j < line.Length; j++) {
                    if (LookAround(data, [i, j])) {

                    }
                }
            }
        }

        /// <summary>
        /// This looks around the current position
        /// </summary>
        /// <param name="data"></param>
        /// <param name="position"></param>
        /// <returns>Whether the position has an adjacent appropriate symbol</returns>
        static bool LookAround(string[] data, int[] position) {
            Regex symbolRegex = new Regex(@"\+\#\*");
            for (int i = -1; i <= 1; i++) {
                for (int j = -1; j <= 1; j++) {
                    try {
                        // This is fucking stupid
                        string letter = data[i][j].ToString();

                        if (symbolRegex.IsMatch(letter)) {
                            return true;
                        }
                    }
                    catch (IndexOutOfRangeException) {
                        // If it's out of range, it doesn't matter
                    }
                }
            }
            //Console.WriteLine();
            return false;
        }

        static int GetNumber(string str, int index) {
            string numStr = "";

            

            return 0;
        }
    }
}