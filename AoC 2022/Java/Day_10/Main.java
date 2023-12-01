package Day_10;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.*;

public class Main {
	static Dictionary<String, Integer> instructions = new Hashtable<String, Integer>();
	static Dictionary<String, Integer> registers = new Hashtable<String, Integer>();
	static String colourStart = "\u001B[";

	/**
	 * Prints an error string with the mentioned text colour, then returns it to
	 * white.
	 * 
	 * @param message    The {@code String} to be printed
	 * @param colourCode The code for the desired colour:
	 *                   {@link https://www.geeksforgeeks.org/how-to-print-colored-text-in-java-console/#:~:text=Color%20Name,%5Cu001B%5B47m}
	 */
	public static void printColouredText(String message, String colourCode) {
		String colour = colourStart + colourCode;
		System.err.println(String.format("%s", colour) + message);
		System.out.print(String.format("%s40m", colourStart));
		System.out.print(String.format("%s37m", colourStart));
	}

	public static void main(String[] args) {
		registers.put("x", 1);

		// Add the instruction that have been given in the project brief
		instructions.put("noop", 1);
		instructions.put("addx", 2);

		// ArrayList<Integer> cycleChecks = new ArrayList<Integer>();

		Scanner inputReader;

		try {
			File inputFile = new File("Day_10/Inputs/input.txt");
			inputFile.setReadOnly();

			inputReader = new Scanner(inputFile);
		} catch (FileNotFoundException e) {
			printColouredText(e.getStackTrace().toString(), "31m");
			return;
		}

		Part1(inputReader);

		inputReader.close();
	}

	static void Part1(Scanner inputReader) {
		Integer[] cycleChecks = { 20, 60, 100, 140, 180, 220 };

		Integer register = 1, cycle = 0, cycleIndex = 0;
		Integer actualResults = 0;

		while (inputReader.hasNextLine()) {
			String line = inputReader.nextLine();
			String[] lineSplit = line.split(" ");
			Integer cycleDuration = instructions.get(lineSplit[0]);
			cycle += cycleDuration;

			// System.out.println(String.format("Current command: %s", lineSplit[0]));

			if (cycleIndex < cycleChecks.length && cycle >= cycleChecks[cycleIndex]) {
				// System.out.println(String.format("Current actual cycle number is: %d",
				// cycle));

				// System.out.println();
				// printColouredText(String.format("\tRegister is %d at cycle %d\n\tAdding %d to the results",
						// register, cycleChecks[cycleIndex], register * cycleChecks[cycleIndex]), "32m");

				actualResults += (register * cycleChecks[cycleIndex]);

				// printColouredText(String.format("\t\tCurrent results are %d", actualResults), "32m");

				cycleIndex++;
			}

			Pattern checkAdd = Pattern.compile("add.");
			Matcher matcher = checkAdd.matcher(lineSplit[0]);

			if (matcher.matches()) {
				String registerName = lineSplit[0].subSequence(3, lineSplit[0].length()).toString();
				register += Integer.parseInt(lineSplit[1]);
				System.out.println(String.format("Register after adding %s is %d",
						lineSplit[1], register));
			}
		}

		printColouredText(String.format("The finished results are %d", actualResults), "42m");
	}
}
