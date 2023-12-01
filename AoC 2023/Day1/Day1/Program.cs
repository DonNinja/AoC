using System;
using System.Text.RegularExpressions;

namespace Day1 {
    internal class Program {
        static void Main(string[] args) {
            string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day1\\input.txt";
            string[] data = File.ReadAllLines(filepath);
            Regex numRegex = new Regex("0-9");
            char[] number = new char[2] { 'a', 'a' };
            string[] numList = { "1", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
            string word = "";

            int results = 0;

            foreach (string line in data) {
                foreach (char letter in line) {
                    word += letter;
                    int num = letter - '0';
                    if (num > 0 && num <= 9) {
                        Fill(letter, ref number, ref word);
                    }
                    else {
                        for (int i = 0; i < numList.Length; i++) {
                            string item = numList[i];

                            if (Regex.Match(word, item).Success) {
                                Fill(char.Parse(i.ToString()), ref number, ref word);
                                break;
                            }
                        }
                    }
                }
                string together = number[0].ToString() + number[1].ToString();

                //Console.WriteLine(string.Format("Number to add will be {0}", together));

                results += int.Parse(together);

                // Reset everything
                number[0] = 'a';
                number[1] = 'a';
                word = "";
            }

            Console.WriteLine(string.Format("Total is: {0}", results));
        }

        /// <summary>
        /// Fills the referenced char array called number with the given letter
        /// </summary>
        /// <param name="letter">Given letter</param>
        /// <param name="number">Referenced number array</param>
        static void Fill(char letter, ref char[] number, ref string word) {
            if (number[0] == 'a') {
                number[0] = letter;
            }
            number[1] = letter;
            word = "";
        }
    }
}