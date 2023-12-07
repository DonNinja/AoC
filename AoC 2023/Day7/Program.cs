﻿namespace Day7 {
    internal class Program {

        static Dictionary<char, int> cardStrength = new() {
                                            {'T', 10 },
                                            {'J', 11 },
                                            {'Q', 12 },
                                            {'K', 13 },
                                            {'A', 14 },
                                        };

        static void Main(string[] args) {
            string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day7\\input2.txt";
            string[] data = File.ReadAllLines(filepath);

            foreach (string line in data) {
                string[] handSplit = line.Split(" ");
                string hand = handSplit[0];
                int bid = int.Parse(handSplit[1]);

                //Console.WriteLine(bid);
                GetTypeStrength(hand);
            }
        }

        /// <summary>
        ///Gets the strength of the given hand, based on preset parameters
        /// </summary>
        /// <param name="hand"></param>
        /// <returns>The strength of the hand</returns>
        static int GetTypeStrength(string hand) {
            Dictionary<char, int> cards = new();

            foreach (char card in hand) {
                if (cards.TryGetValue(card, out int value)) {
                    cards[card] = ++value;
                }
                else {
                    cards[card] = 1;
                }
            }

            if (cards.Count == 5) {
                return 1;
            }

            foreach (KeyValuePair<char, int> item in cards) {
                Console.WriteLine($"Card: {item.Key} | Amount: {item.Value}");
            }

            Console.WriteLine();

            switch (cards.Count) {
                case 5:
                    return 1;

                case 4:
                    return 2;

                case 3:
                    break;

                case 2:
                    break;

                case 1:
                    return 99999;

                default:
                    return 0;
            }

            return 0;
        }
    }
}