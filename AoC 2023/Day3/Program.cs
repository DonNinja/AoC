using System.Text.RegularExpressions;

namespace Day3 {
    internal class Program {
        public static Regex symbolRegex = new Regex(@"\W");

        static void Main(string[] args) {
            string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day3\\input.txt";
            string[] data = File.ReadAllLines(filepath);
            Regex numRegex = new(@"0-9");
            bool foundNumber = false;
            int result = 0;
            int gearRatioResult = 0;

            for (int i = 0; i < data.Length; i++) {
                foundNumber = false;
                string line = data[i];

                for (int j = 0; j < line.Length; j++) {
                    string letter = line[j].ToString();

                    if (letter == "*")
                        gearRatioResult += GetGearRatios(data, [i, j]);

                    if (!foundNumber && LookAround(data, [i, j])) {
                        if (!new Regex(@"\d").IsMatch(letter))
                            continue;

                        foundNumber = true;

                        int gn = GetNumber(line, j);

                        //Console.WriteLine(string.Format("Found a part number: {0}", gn));

                        result += gn;
                    }
                    else if (foundNumber && symbolRegex.IsMatch(line[j].ToString())) {
                        foundNumber = false;
                    }
                }
            }

            Console.WriteLine(string.Format("The result should be: {0}", result));
            Console.WriteLine(string.Format("The gear ratio result should be: {0}", gearRatioResult));
        }

        /// <summary>
        /// This looks around the current position
        /// </summary>
        /// <param name="data"></param>
        /// <param name="position"></param>
        /// <returns>Whether the position has an adjacent appropriate symbol</returns>
        static bool LookAround(string[] data, int[] position) {
            for (int i = -1; i <= 1; i++) {
                for (int j = -1; j <= 1; j++) {
                    try {
                        // This is fucking stupid
                        string letter = data[position[0] + i][position[1] + j].ToString();

                        if (symbolRegex.IsMatch(letter) && letter != ".") {
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

        static int GetGearRatios(string[] data, int[] position) {
            List<int> gears = new();
            Regex numRegex = new Regex(@"\d");

            for (int i = -1; i <= 1; i++) {
                bool foundNumber = false;
                for (int j = -1; j <= 1; j++) {
                    try {
                        int line = position[0] + i;
                        int index = position[1] + j;
                        // This is fucking stupid
                        string letter = data[line][index].ToString();

                        if (!foundNumber && numRegex.IsMatch(letter)) {
                            int num = GetNumber(data[line], index);
                            foundNumber = true;
                            if (!gears.Contains(num)) {
                                gears.Add(num);
                            }
                        }
                        else {
                            foundNumber = false;
                        }
                    }
                    catch (IndexOutOfRangeException) {
                        // If it's out of range, it doesn't matter
                    }
                }
            }

            if (gears.Count != 2) {
                return 0;
            }

            return gears[0] * gears[1];
        }

        /// <summary>
        /// This gets the number
        /// </summary>
        /// <param name="str"></param>
        /// <param name="index"></param>
        /// <returns></returns>
        static int GetNumber(string str, int index) {
            string numStr = "";

            for (int i = index; i < str.Length; i++) {
                if (symbolRegex.IsMatch(str[i].ToString())) {
                    break;
                }
                numStr += str[i];
            }

            for (int i = index - 1; i >= 0; i--) {
                if (symbolRegex.IsMatch(str[i].ToString())) {
                    break;
                }
                numStr = str[i] + numStr;
            }

            return int.Parse(numStr);
        }
    }
}