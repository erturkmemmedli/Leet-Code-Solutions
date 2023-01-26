class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for path in paths:
            path_elements = path.split()
            directory = path_elements[0]
            for element in path_elements[1:]:
                i = element.index('(')
                hashmap[element[i+1:-1]].append(directory + '/' + element[:i])
        return [val for val in hashmap.values() if len(val) > 1]

"""
Follow Up:
Imagine you are given a real file system, how will you search files? DFS or BFS?
If the file content is very large (GB level), how will you modify your solution?
If you can only read the file by 1kb each time, how will you modify your solution?
What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
How to make sure the duplicated files you find are not false positive?


Version 1:
BFS can be used for great concurrency. Also, seek time would be greatly reduced as the files are co-located. Where as DFS would be requiring a lock on root node, if you are simultaneous processing the contents.

If the files are too large, its better to Navigate first to get a list of file paths and then process the hash-map.

Check the sizes of the files, if they match we need further processing.
Maintain a checksum for the similar sizes, hash functions like sha256(hashes hardly collide) can be used to calculate checksums.
If we can read only, 1Kb at a time, we can still use checksum for the blocks and calculate till the point they differ.
May be read 0.5 kb from file 1 and 0.5 kb from file2 to check if they differ.

import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.hexdigest()
'19197dc4d03829df858011c6c87600f994a858103bbc19005f20987aa19a97e2'
Time Complexty:

For navigating, the files O(n), where n is the total number of files.
For, calculating the checksums in case of similar sizes, we could approximate this as O( c + xb), where b is the number of blocks required to read till the files being compared differ, x is the constant for per-block overhead, and c is the constant for initialization and finalization.
Further O(n) time is required to loop over the hashmap(key = f(size, checksum till they branch)) and return the once having more than 1 file path.
Shloud consider to read the whole file content byte to byte.


Version 2:
Imagine you are given a real file system, how will you search files? DFS or BFS?
DFS. In this case the directory path could be large. DFS can reuse the shared the parent directory before leaving that directory. But BFS cannot.

If the file content is very large (GB level), how will you modify your solution?
In this case, not realistic to match the whole string of the content. So we use file signitures to judge if two files are identical. Signitures can include file size, as well as sampled contents on the same positions. They could have different file names and time stamps though.
Hashmaps are necessary to store the previous scanned file info. S = O(|keys| + |list(directory)|). The key and the directory strings are the main space consumption.

a. Sample to obtain the sliced indices in the strings stored in the RAM only once and used for all the scanned files. Accessing the strings is on-the-fly. But transforming them to hashcode used to look up in hashmap and storing the keys and the directories in the hashmap can be time consuming. The directory string can be compressed to directory id. The keys are hard to compress.
b. Use fast hashing algorithm e.g. MD5 or use SHA256 (no collisions found yet). If no worry about the collision, meaning the hashcode is 1-1. Thus in the hashmap, the storage consumption on key string can be replaced by key_hashcode, space usage compressed.

If you can only read the file by 1kb each time, how will you modify your solution?
That is the file cannot fit the whole ram. Use a buffer to read controlled by a loop; read until not needed or to the end. The sampled slices are offset by the times the buffer is called.

What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
T = O(|num_files||sample||directory_depth|) + O(|hashmap.keys()|)

How to make sure the duplicated files you find are not false positive?
Add a round of final check which checks the whole string of the content. T = O(|num_output_list||max_list_size||file_size|).


Version 3:
BFS vs DFS
BFS explores neighbors first. This means that files which are located close to each other are also accessed one after another. This is great e.g. for reducing HDD seek times due to space locality and is expected to be faster. For SSDs, larger number of small sequential reads can be grouped into smaller number of large reads.

Also, BFS is easier to parallelize and allows more fine-grained locking. DFS will require a lock on the root node.

Very large files and false positives
For very large files we should do the following comparisons in this order:

compare sizes, if not equal, then files are different and stop here!
hash them with a fast algorithm e.g. MD5 or use SHA256 (no collisions found yet), if not equal then stop here!
compare byte by byte to avoid false positives due to collisions.
Have you used an IDE in remote development mode?
For example, CLion has some options on how to compare the local files with the remote server files and then decides to synchronize or not.

Complexity
Runtime - Worst case (which is very unlikely to happen): O(N^2 * L) where L is the size of the maximum bytes that need to be compared
Space - Worst case: all files are hashed and inserted in the hashmap, so O(H^2*L), H is the hash code size and L is the filename size
"""
