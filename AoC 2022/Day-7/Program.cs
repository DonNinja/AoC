using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day_7 {
    class DayFile {
        public Folder parent;
        public string name;
        public int size;


        public DayFile(Folder parent, string name, int size) {
            this.parent = parent;
            this.name = name;
            this.size = size;
        }
    }

    class Folder {
        public Folder parent;
        public string name;
        private List<DayFile> childFiles;
        private List<Folder> childFolders;

        public Folder(Folder parent, string name) {
            this.parent = parent;
            this.name = name;
            childFiles = new List<DayFile>();
            childFolders = new List<Folder>();
        }

        public void AddFile(DayFile file) {
            childFiles.Add(file);
        }

        public void AddFolder(Folder folder) {
            childFolders.Add(folder);
        }

        public int GetSize() {
            int results = 0;
            foreach (var file in childFiles) {
                results += file.size;
            }
            foreach (var folder in childFolders) {
                results += folder.GetSize();
            }

            return results;
        }
    }

    internal class Program {
        static void Main() {
            string filepath = "E:\\OneDrive\\Projects\\AoC\\AoC 2022\\Day-7\\input.txt";

            string[] data = File.ReadAllLines(filepath);

            //Part1(data);
            Console.WriteLine($"The results came in and are: {Part1(data)}");

            //Console.WriteLine("(Press enter to quit)");
            //Console.ReadLine();
        }

        static int Part1(string[] data) {
            int depth = 0;
            int results = 0;
            Dictionary<string, Folder> folders = new Dictionary<string, Folder>();
            Folder currentFolder = null;
            string folderName = "/";
            folders.Add(folderName, new Folder(null, folderName ));
            //string 
            foreach (string line in data) {
                string[] commands = line.Split(' ');
                switch (commands[0]) {
                    case "$":
                        // This will be a command
                        switch (commands[1]) {
                            case "cd":
                                if (commands[2] == "..") {
                                    if (currentFolder != null && currentFolder.parent != null) {
                                        currentFolder = currentFolder.parent;
                                        depth--;
                                        folderName = currentFolder.name;
                                    }
                                }
                                else if (commands[2] == "/") {
                                    folderName = "/";
                                    currentFolder = folders["/"];
                                    depth = 0;
                                }
                                else {
                                    folderName += commands[2] + "/";
                                    currentFolder = folders[folderName];
                                    depth++;
                                }
                                break;
                            default:
                                break;
                        }
                        break;
                    case "dir":
                        folderName += commands[1] + "/";
                        Folder newFolder = new Folder(currentFolder, folderName);
                        folders.Add(folderName, newFolder);
                        currentFolder.AddFolder(newFolder);
                        folderName = currentFolder.name;
                        break;
                    default:
                        if (int.TryParse(commands[0], out int size)) {
                            DayFile newFile = new DayFile(currentFolder, commands[1], size);
                            currentFolder.AddFile(newFile);
                        }
                        else {
                            Console.WriteLine($"Could not parse int for file {commands[1]}");
                        }
                        break;
                }
            }

            int totalSpace = 70000000;
            int freeSpace = totalSpace - folders["/"].GetSize();
            int updateSize = 30000000;
            int spaceNeeded = updateSize - freeSpace;
            int smallestSpace = 99999999;

            Console.WriteLine($"Total free space is {freeSpace}, which means we need at least {spaceNeeded}");

            // Find all folders under 100000 in size
            int max = 100000;
            foreach (string folderKey in folders.Keys) {
                int size = folders[folderKey].GetSize();
                if (size < max) {
                    results += size;
                }
                Console.WriteLine($"Size of {folderKey} is {size}");
                if (spaceNeeded - size < 0 && size < smallestSpace)
                    smallestSpace = size;
            }

            Console.WriteLine($"The smallest size folder would be {smallestSpace} in size");

            return results;
        }
    }
}
