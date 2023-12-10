string filepath = "E:\\OneDrive\\Projects\\Advent-of-Code\\AoC 2023\\Day6\\input.txt";
string[] data = File.ReadAllLines(filepath);

List<Tuple<int, long>> matches = new();

string time = data[0].Split(":")[1].Trim();
string distance = data[1].Split(":")[1].Trim();

List<string> durations = time.Split(" ").Where(n => n != "").ToList();
List<string> lengths = distance.Split(" ").Where(n => n != "").ToList();

string t = "";
foreach (var d in durations) {
    t += d;
}

int singleDuration = int.Parse(t);


string l = "";
foreach (var m in lengths) {
    l += m;
}

long singleRecord = long.Parse(l);

Tuple<int, long> longMatch = new(singleDuration, singleRecord);

int results = 0;

// Populate matches
for (int i = 0; i < durations.Count; i++) {
    matches.Add(new Tuple<int, long>(int.Parse(durations[i]), long.Parse(lengths[i])));
}


foreach (var match in matches) {
    int count = GetMatchCounts(match);

    if (results == 0) {
        results = count;
    }
    else {
        results *= count;
    }
}

Console.WriteLine(results);

Console.WriteLine(GetMatchCounts(longMatch));


int GetMatchCounts(Tuple<int, long> match) {
    int count = 0;

    int duration = match.Item1;
    long record = match.Item2;

    for (int speed = 0; speed <= duration; speed++) {
        int totalTime = duration - speed;

        if (speed > record / totalTime) {
            count++;
        }
        else if (count > 0) {
            break;
        }
    }

    return count;
}