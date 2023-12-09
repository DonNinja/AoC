namespace Day7 {
    internal class Program {
        class Hand {
            public string cards;
            public int bid;
            public int strength;

            public Hand(string cards, int bid, int strength) {
                this.cards = cards;
                this.bid = bid;
                this.strength = strength;
            }
        }


        static Dictionary<string, int> cardStrength = new() {
                {"T", 10 },
                {"J", 11 },
                {"Q", 12 },
                {"K", 13 },
                {"A", 14 },
            };

        static void Main(string[] args) {
            List<Hand> handValueList = new();
            string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day7\\input.txt";
            string[] data = File.ReadAllLines(filepath);

            foreach (string line in data) {
                bool addedHand = false;

                string[] handSplit = line.Split(" ");
                string hand = handSplit[0];
                int bid = int.Parse(handSplit[1]);

                //Console.WriteLine(bid);
                int strength = GetTypeStrength(hand);

                Hand handValue = new(hand, bid, strength);

                for (int i = 0; i < handValueList.Count; i++) {
                    int comparisonStrength = handValueList[i].strength;
                    string comparisonHand = handValueList[i].cards;

                    if (comparisonStrength > handValue.strength) {
                        addedHand = true;
                        handValueList.Insert(i, handValue);

                        break;
                    }
                    else if (comparisonStrength == handValue.strength) {
                        if (!IsStronger(handValue.cards, comparisonHand)) {
                            addedHand = true;
                            handValueList.Insert(i, handValue);
                            break;
                        }
                    }

                }

                if (!addedHand) {
                    handValueList.Add(handValue);
                }
            }

            int result = 0;

            for (int i = 0; i < handValueList.Count; i++) {
                Hand item = handValueList[i];
                result += item.bid * (i + 1);
                Console.WriteLine($"{item.cards} | {item.bid} | {item.strength}");
            }

            Console.WriteLine(result);
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

            //foreach (KeyValuePair<char, int> item in cards) {
            //    Console.WriteLine($"Card: {item.Key} | Amount: {item.Value}");
            //}

            //Console.WriteLine();

            // We can differentiate the different types based on the unique cards in the hand
            switch (cards.Count) {
                case 5:
                    //! This is only a high card hand

                    return 1;

                case 4:
                    //! This is only a single pair

                    return 2;

                case 3:
                    //! This case includes both two pair, and three of a kind

                    foreach (KeyValuePair<char, int> item in cards) {
                        //Console.WriteLine($"Card: {item.Key} | Amount: {item.Value}");
                        if (item.Value == 3) {
                            return 4;
                        }
                    }

                    return 3;

                case 2:
                    //! This case includes both 

                    foreach (KeyValuePair<char, int> item in cards) {
                        //Console.WriteLine($"Card: {item.Key} | Amount: {item.Value}");
                        if (item.Value == 4) {
                            return 6;
                        }
                    }

                    return 5;

                case 1:
                    //! This will always be five of a kind, or the highest value hand

                    return 7;

                default:
                    return 0;
            }
        }

        static bool IsStronger(string currentHand, string comparisonHand) {
            for (int i = 0; i < currentHand.Length; i++) {
                string currentCard = currentHand[i].ToString();
                string comparisonCard = comparisonHand[i].ToString();

                int currentCardValue = 0;
                int comparisonCardValue = 0;

                if (int.TryParse(currentCard, out currentCardValue)) { }
                else currentCardValue = cardStrength[currentCard];

                if (int.TryParse(comparisonCard, out comparisonCardValue)) { }
                else comparisonCardValue = cardStrength[comparisonCard];

                if (currentCardValue != comparisonCardValue) {
                    return currentCardValue > comparisonCardValue;
                }
            }

            return false;
        }
    }
}